"""Cleaning rules for the raw cards/users tables."""

import pandas as pd

USER_CURRENCY_COLUMNS = ["per_capita_income", "yearly_income", "total_debt"]


def _strip_currency(series: pd.Series) -> pd.Series:
    return series.str.replace("$", "", regex=False).astype(float)


def clean_cards(cards_df: pd.DataFrame) -> pd.DataFrame:
    cards_df = cards_df.copy()
    cards_df["credit_limit"] = _strip_currency(cards_df["credit_limit"])
    return cards_df


def clean_users(user_df: pd.DataFrame) -> pd.DataFrame:
    user_df = user_df.copy()
    for col in USER_CURRENCY_COLUMNS:
        user_df[col] = _strip_currency(user_df[col])
    return user_df
