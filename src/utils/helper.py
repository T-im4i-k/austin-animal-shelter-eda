"""Helper utilities for categorical data processing."""

import pandas as pd


def small_cat_group(data: pd.Series, group_name: str, threshold=0.015) -> pd.Series:
    """Group infrequent categories in a Series under a common label."""
    counts = data.value_counts(normalize=True)
    small = counts[counts < threshold].index
    grouped = data.where(~data.isin(small), group_name)
    return grouped
