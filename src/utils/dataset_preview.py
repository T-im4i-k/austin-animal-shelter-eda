"""Concise utilities for DataFrame preview in notebooks."""

import pandas as pd
from IPython.display import display


def dataset_preview(df_name: str, df_date: pd.DataFrame) -> None:
    """Display a quick head/tail sample of the DataFrame."""
    print(f"=== {df_name} dataset preview ===\n")
    print(f"{df_name} head:")
    display(df_date.head(3))
    print(f"{df_name} tail:")
    display(df_date.tail(3))
    print("\n")


def dataset_shape(df_name: str, df_data: pd.DataFrame) -> None:
    """Print the DataFrame's row and column count."""
    print(
        f"{df_name} dataframe shape: {df_data.shape[0]} rows, {df_data.shape[1]} columns"
    )


def dataset_columns_dtypes(df_name: str, df_data: pd.DataFrame) -> None:
    """Show column data types for schema verification."""
    print(f"=== {df_name} datatypes ===\n")
    display(df_data.dtypes)
    print("\n")


def dataset_columns_nunique(df_name: str, df_data: pd.DataFrame) -> None:
    """Display unique value counts per column."""
    print(f"=== {df_name} number of unique values ===\n")
    display(df_data.nunique())
    print("\n")


def dataset_columns_nnan(df_name: str, df_data: pd.DataFrame) -> None:
    """Report NaN counts per column for missing data overview."""
    print(f"=== {df_name} number of NaN values ===\n")
    display(df_data.isna().sum())
    print("\n")
