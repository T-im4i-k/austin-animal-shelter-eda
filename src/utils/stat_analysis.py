"""Statistical analysis utilities for pandas Series."""

import pandas as pd
from IPython.display import display


def iqr_detect_outliers(X: pd.Series) -> tuple[pd.Series, pd.Series]:
    """Detect lower and upper outliers using the IQR method."""
    Q1, Q3 = X.quantile([0.25, 0.75])
    IQR = Q3 - Q1
    lower_outliers = X < Q1 - 1.5 * IQR
    upper_outliers = X > Q3 + 1.5 * IQR
    return lower_outliers, upper_outliers


def num_statistics(X: pd.Series):
    """Display summary statistics, dispersion, and outlier counts for a Series."""
    print(f"=== {X.name} statistics ===\n")
    min_, max_ = X.min(), X.max()
    Q1, Q2, Q3 = X.quantile([0.25, 0.5, 0.75])
    std = X.std()
    print(f"{X.name} distribution metrics:\n")
    display(
        pd.Series(data=[min_, Q1, Q2, Q3, max_], index=["min", "Q1", "Q2", "Q3", "max"])
    )
    print(f"{X.name} dispersion metrics:\n")
    display(pd.Series(data=[max_ - min_, std, Q3 - Q1], index=["range", "std", "IQR"]))
    lower_outliers, upper_outliers = iqr_detect_outliers(X)
    outliers = lower_outliers | upper_outliers
    print(f"{X.name} outliers metrics:")
    display(
        pd.Series(
            data=[outliers.sum(), lower_outliers.sum(), upper_outliers.sum()],
            index=["outliers count", "lower outliers", "upper outliers"],
        )
    )


def cond_prob_table(x: pd.Series, y: pd.Series) -> None:
    """Display conditional probability tables between two Series."""
    print(f"=== Conditional probabilities {x.name} <-> {y.name} ===\n")
    x_given_y = pd.crosstab(y, x, normalize="index") * 100
    y_given_x = pd.crosstab(x, y, normalize="index") * 100
    print(f"P({y.name}|{x.name}) in %:")
    display(y_given_x.round(1))
    print(f"P({x.name}|{y.name}) in %:")
    display(x_given_y.round(1))
    print("\n")


def prob_a_if_b(a_data: pd.Series, b_data: pd.Series) -> None:
    """Show conditional probability of one Series given another."""
    print(f"=== Probability of {a_data.name} given {b_data.name} ===\n")
    prob_table = pd.crosstab(a_data, b_data, normalize="columns") * 100
    print("Conditional probability table (in %):")
    display(prob_table.round(1))
    print("\n")
