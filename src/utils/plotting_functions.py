"""Plotting utilities for common data visualizations using seaborn and plotly."""

import seaborn as sns
import pandas as pd
import plotly.express as px


def plot_bar(x, y, ax, xlabel: str, ylabel: str, color, **kwargs):
    """Draw a vertical bar plot with labeled axes."""
    ax = sns.barplot(x=x, y=y, ax=ax, color=color, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax


def plot_bar_with_perc(x, y, ax, xlabel: str, ylabel: str, color, **kwargs):
    """Draw a vertical bar plot with percentage labeles."""
    ax = sns.barplot(x=x, y=y, ax=ax, color=color, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    for patch in ax.patches:
        patch_x = patch.get_width()
        path_y = patch.get_y() + patch.get_height() / 2
        perc = patch_x
        ax.text(patch_x, path_y, f" {perc:.1f}%", ha="left", va="center")

    return ax


def plot_bar_with_trend(
    x, y, ax, xlabel: str, ylabel: str, bar_color, trend_color, **kwargs
):
    """Draw a bar plot with an overlaid trend line."""
    ax = plot_bar(x, y, ax=ax, xlabel=xlabel, ylabel=ylabel, color=bar_color, **kwargs)
    xbar = [patch.get_x() + patch.get_width() / 2 for patch in ax.patches]
    ybar = [patch.get_height() for patch in ax.patches]
    ax.plot(
        xbar,
        ybar,
        linestyle="-",
        marker="o",
        lw=2,
        color=trend_color,
        label="Trend line",
    )
    return ax


def plot_hist(data: pd.Series, ax, xlabel: str, ylabel: str, color, **kwargs):
    """Draw a histogram for a Series."""
    ax = sns.histplot(x=data, ax=ax, color=color, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax


def plot_hist_with_kde(
    data: pd.Series, ax, xlabel: str, ylabel: str, hist_color, kde_color, **kwargs
):
    """Draw a histogram with a kernel density estimate overlay."""
    ax = plot_hist(
        data, ax=ax, xlabel=xlabel, ylabel=ylabel, color=hist_color, kde=True, **kwargs
    )
    kde_line = ax.lines[0]
    kde_line.set_color(kde_color)
    kde_line.set_lw(2)
    kde_line.set_label("Kernel density")
    return ax


def plot_vcount(data: pd.Series, ax, xlabel: str, ylabel: str, color, **kwargs):
    """Draw a vertical count plot for categorical data."""
    ax = sns.countplot(x=data, ax=ax, color=color, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax


def plot_hcount(data: pd.Series, ax, xlabel: str, ylabel: str, color, **kwargs):
    """Draw a horizontal count plot for categorical data."""
    ax = sns.countplot(y=data, ax=ax, color=color, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax


def plot_count_with_labels(
    data: pd.Series, ax, xlabel: str, ylabel: str, color, **kwargs
):
    """Draw a horizontal count plot with value and percentage labels."""
    ax = plot_hcount(data, ax=ax, xlabel=xlabel, ylabel=ylabel, color=color, **kwargs)
    for patch in ax.patches:
        x = patch.get_width()
        y = patch.get_y() + patch.get_height() / 2
        perc = (x / data.size) * 100
        ax.text(x, y, f" {int(x)} ({perc:.1f}%)", ha="left", va="center")

    return ax


def plot_count_with_trend(
    data: pd.Series, ax, xlabel: str, ylabel: str, bar_color, trend_color, **kwargs
):
    """Draw a vertical count plot with an overlaid trend line."""
    ax = plot_vcount(
        data, ax=ax, xlabel=xlabel, ylabel=ylabel, color=bar_color, **kwargs
    )
    xbar = [patch.get_x() + patch.get_width() / 2 for patch in ax.patches]
    ybar = [patch.get_height() for patch in ax.patches]
    ax.plot(
        xbar,
        ybar,
        linestyle="-",
        marker="o",
        lw=2,
        color=trend_color,
        label="Trend line",
    )
    return ax


def plot_box(data: pd.Series, ax, xlabel: str, ylabel: str, color, **kwargs):
    """Draw a boxplot for a Series."""
    ax = sns.boxplot(x=data, ax=ax, color=color, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax


def plot_viloin_cat(
    x: pd.Series, y: pd.Series, ax, xlabel: str, ylabel: str, color, **kwargs
):
    """Draw a violin plot for categorical and numeric data."""
    ax = sns.violinplot(x=x, y=y, ax=ax, color=color, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax


def plot_donut(data: pd.Series, ax, xlabel: str, ylabel: str, order=None, **kwargs):
    """Draw a donut (pie) chart for categorical data."""
    counts = data.value_counts()
    if order is not None:
        counts = counts.iloc[order]

    ax.pie(counts, labels=counts.index, wedgeprops=dict(width=0.4), **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax


def plot_parallel_cat(
    df: pd.DataFrame, lhs_col: str, rhs_col: str, title: str, palette, **kwargs
):
    """Draw a parallel categories plot for two categorical columns."""
    lhs_num = df[lhs_col].cat.codes
    n_colors = df[lhs_col].nunique()
    palette = palette.as_hex()[:n_colors]

    fig = px.parallel_categories(
        df,
        dimensions=[lhs_col, rhs_col],
        title=title,
        color=lhs_num,
        color_continuous_scale=palette,
        **kwargs,
    )

    fig.update_traces(
        hoverinfo="all", hoveron="category", selector=dict(type="parcats")
    )
    fig.update_layout(coloraxis_showscale=False)
    return fig


def plot_sunburst(
    data: pd.DataFrame, cat_col: str, sub_cat_col: str, title: str, palette, **kwargs
):
    """Draw a sunburst plot for hierarchical categorical data."""
    fig = px.sunburst(
        data,
        path=[cat_col, sub_cat_col],
        color_discrete_sequence=palette.as_hex(),
        title=title,
        **kwargs,
    )

    return fig


def plot_heatmap(
    data: pd.DataFrame, ax, xlabel: str, ylabel: str, cmap="Blues", **kwargs
):
    """Draw a heatmap for a DataFrame."""
    ax = sns.heatmap(data, ax=ax, cmap=cmap, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    return ax
