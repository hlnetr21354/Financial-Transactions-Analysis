"""Raw data loading for the financial transactions dataset."""

import json
import time
from pathlib import Path

import duckdb
import pandas as pd

# src/ -> Financial-Transactions-Analysis/ -> project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"


def load_cards(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    return pd.read_csv(data_dir / "cards_data.csv")


def load_users(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    return pd.read_csv(data_dir / "users_data.csv")


def load_mcc_codes(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    with open(data_dir / "mcc_codes.json", encoding="utf8") as json_file:
        mcc_codes = json.load(json_file)
    return pd.DataFrame(mcc_codes.items(), columns=["mcc_code", "description"])


def load_transactions(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load + clean transactions_data.csv (13.3M rows, ~1.2GB) in one DuckDB query.

    Replaces pd.read_csv + separate $-strip/fillna/dtype-cast steps with a single
    vectorized, multi-threaded pass over the CSV. sample_size is raised so DuckDB's
    CSV auto-detection sees a quoted, embedded-comma value (in 'errors', e.g.
    "Insufficient Balance,Technical Glitch") within its sample and picks the right
    quote char itself -- passing quote/escape explicitly instead forces DuckDB into
    a much slower single-threaded parser (370s vs <1s here).
    """
    csv_path = (data_dir / "transactions_data.csv").as_posix()
    t0 = time.time()
    txn_rel = duckdb.sql(f"""
        WITH txn_raw AS (
            SELECT
                id,
                CAST(date AS TIMESTAMP)                                    AS date,
                client_id,
                card_id,
                CAST(REPLACE(amount, '$', '') AS DOUBLE)                    AS amount,
                use_chip,
                merchant_id,
                merchant_city,
                CASE WHEN merchant_city = 'ONLINE' THEN 'ONLINE'
                    ELSE merchant_state END                                AS merchant_state,
                COALESCE(REPLACE(CAST(zip AS VARCHAR), '.0', ''), 'Unknown')    AS zip,
                mcc,
                COALESCE(errors, 'none')                                     AS errors
            FROM read_csv_auto('{csv_path}', sample_size=200000)
        )
        SELECT
            *,
            CASE WHEN
                    zip != 'Unknown'
                THEN
                    CONCAT_WS('_', CAST(merchant_id AS TEXT), CAST(zip AS TEXT))
                ELSE
                    CONCAT_WS(
                        '_',
                        CAST(merchant_id AS TEXT),
                        REPLACE(merchant_city, ' ', '_'),
                        REPLACE(merchant_state, ' ', '_')
                    )
            END AS merchant_branch_key
        FROM txn_raw
    """)
    # Materialize via Arrow (split_blocks + self_destruct) instead of .df() directly:
    # on lower-RAM machines, pandas' block-consolidation step when building a
    # DataFrame straight from DuckDB's result can fail with a MemoryError even
    # though the query itself finishes in under a second. Going through Arrow
    # avoids that extra copy.
    txn_df = txn_rel.arrow().read_all().to_pandas(split_blocks=True, self_destruct=True)
    print(f"Loaded & cleaned transactions_data.csv in {time.time() - t0:.1f}s -> {txn_df.shape}")
    return txn_df


def load_fraud_labels(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    # Kept as plain json.load()/pd.DataFrame: this step was never the actual
    # bottleneck (it's a simple flat dict), and DuckDB's JSON reader needs the
    # whole 300MB+ object to fit as one in-memory MAP value to flatten it with
    # UNNEST, which is a poor fit for this machine's RAM.
    with open(data_dir / "train_fraud_labels.json") as f:
        fraud_label = json.load(f)
    return pd.DataFrame(list(fraud_label["target"].items()), columns=["transaction_id", "fraud_label"])
