"""
Business Analytics Case Study 1 — Retail Sales Analysis
=======================================================

Business context:
    A retail manager requires an analysis of monthly sales over a year to
    assess the trend, identify the strongest periods, and detect seasonality.

Objective:
    Analyze monthly sales to identify the trend and the peak period.

Run:
    python retail_sales_analysis.py

Requires:
    pandas
"""

import pandas as pd


def build_dataset() -> pd.DataFrame:
    """Return one year of monthly retail sales."""
    df = pd.DataFrame({
        "Month": pd.to_datetime([
            "2025-01-01", "2025-02-01", "2025-03-01", "2025-04-01",
            "2025-05-01", "2025-06-01", "2025-07-01", "2025-08-01",
            "2025-09-01", "2025-10-01", "2025-11-01", "2025-12-01",
        ]),
        "Sales": [200, 210, 220, 215, 230, 225, 240, 235, 260, 290, 350, 420],
    })
    # Extract a readable month label from the datetime column.
    df["MonthName"] = df["Month"].dt.month_name()
    return df


def analyze(df: pd.DataFrame) -> None:
    """Print the headline metrics for the retail sales analysis."""
    print("Total annual sales:", df["Sales"].sum())
    print("Average monthly sales:", round(df["Sales"].mean(), 1))

    # idxmax / idxmin return the index label of the largest / smallest value;
    # .loc then looks up the corresponding month name.
    print("Peak month:", df.loc[df["Sales"].idxmax(), "MonthName"])
    print("Lowest month:", df.loc[df["Sales"].idxmin(), "MonthName"])

    # Compare the second half of the year to the first half to expose the trend.
    first_half = df["Sales"][:6].sum()
    second_half = df["Sales"][6:].sum()
    print("First half total:", first_half, "| Second half total:", second_half)


def main() -> None:
    df = build_dataset()
    analyze(df)


if __name__ == "__main__":
    main()
