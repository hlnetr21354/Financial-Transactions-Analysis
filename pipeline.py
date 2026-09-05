"""Orchestrates the full load -> clean -> transform -> export pipeline.

    cards_raw, users_raw, mcc_codes_df, txn_raw, fraud_label_df   (load)
        -> cards_df, user_df                                     (clean)
        -> txn_df -> merchant_df, txn_error_df, txn_label_df      (transform)
        -> transformed_data/*.csv                                 (export)

Run directly (`python pipeline.py`) or import `run_pipeline()` from the
notebook to get the same tables without re-typing the transform logic.
"""

from src.clean import clean_cards, clean_users
from src.export import export_tables
from src.load import load_cards, load_fraud_labels, load_mcc_codes, load_transactions, load_users
from src.transform import (
    add_is_domestic,
    build_merchant_table,
    drop_errors_column,
    drop_merchant_columns,
    extract_transaction_errors,
    join_fraud_labels,
)


def run_pipeline() -> dict:
    # cards_df = clean_cards(load_cards())
    # user_df = clean_users(load_users())
    # mcc_codes_df = load_mcc_codes()
    fraud_label_df = load_fraud_labels()

    txn_df = load_transactions()
    txn_df = add_is_domestic(txn_df)

    merchant_df = build_merchant_table(txn_df)
    txn_df = drop_merchant_columns(txn_df)

    txn_error_df = extract_transaction_errors(txn_df)
    txn_df = drop_errors_column(txn_df)

    txn_label_df = join_fraud_labels(txn_df, fraud_label_df)

    tables = {
        # "cards": cards_df,
        # "users": user_df,
        # "mcc_codes": mcc_codes_df,
        # "fraud_labels": fraud_label_df,
        "merchants": merchant_df,
        # "transaction_errors": txn_error_df,
        "transactions": txn_label_df,
    }

    export_tables({
        # "cards_data.csv": cards_df,
        # "users_data.csv": user_df,
        # "mcc_codes.csv": mcc_codes_df,
        # "fraud_labels.csv": fraud_label_df,
        "merchants_data.csv": merchant_df,
        # "transaction_errors.csv": txn_error_df,
        "transactions_data.csv": txn_label_df,
    })

    return tables


if __name__ == "__main__":
    run_pipeline()
