"""Derived tables and column-level transforms built on top of txn_df."""

import time

import duckdb
import pandas as pd


def add_is_domestic(txn_df: pd.DataFrame) -> pd.DataFrame:
    """Flag transactions as domestic vs. foreign.

    Every 'Unknown' zip other than ONLINE turned out to be a transaction from a
    foreign merchant, where merchant_state holds a country name instead of a
    2-letter US state code -- that length check is what this flag is based on.
    """
    txn_df = txn_df.copy()
    txn_df["is_domestic"] = txn_df["merchant_state"].str.len() <= 2
    return txn_df


def build_merchant_table(txn_df: pd.DataFrame) -> pd.DataFrame:
    """Extract the merchant-branch dimension table out of txn_df."""
    return (
        txn_df[["merchant_branch_key", "merchant_id", "zip", "merchant_city", "merchant_state"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )


def drop_merchant_columns(txn_df: pd.DataFrame) -> pd.DataFrame:
    """Drop the merchant columns now that they live in the merchant table."""
    return txn_df.drop(columns=["merchant_id", "zip", "merchant_city", "merchant_state"])


def extract_transaction_errors(txn_df: pd.DataFrame) -> pd.DataFrame:
    """Long-format (transaction id, error type) table for transactions with errors."""
    txn_error = txn_df.loc[txn_df["errors"] != "none", ["id", "errors"]].copy()
    txn_error["errors"] = txn_error["errors"].str.split(",")
    return txn_error.explode("errors")


def drop_errors_column(txn_df: pd.DataFrame) -> pd.DataFrame:
    """Drop 'errors' now that it lives in the separate errors table."""
    return txn_df.drop(columns=["errors"])


def join_fraud_labels(txn_df: pd.DataFrame, fraud_label_df: pd.DataFrame) -> pd.DataFrame:
    """Left-join fraud labels onto transactions via DuckDB (faster than a pandas
    merge at this row count)."""
    t0 = time.time()
    join_rel = duckdb.sql("""
        SELECT t.*, f.fraud_label
        FROM txn_df t
        LEFT JOIN fraud_label_df f
          ON CAST(t.id AS VARCHAR) = f.transaction_id
    """)
    # Same Arrow materialization as the load step, to avoid a pandas OOM when
    # building the joined 13.3M-row DataFrame on lower-RAM machines.
    txn_label_df = join_rel.arrow().read_all().to_pandas(split_blocks=True, self_destruct=True)
    print(f"Joined in {time.time() - t0:.1f}s -> {txn_label_df.shape}")
    return txn_label_df
