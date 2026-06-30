"""
Business Analytics Case Study 3 — Customer Growth Analysis
==========================================================

Business context:
    A subscription business wishes to analyze its customer growth over the year,
    including the rate of new customer acquisition.

Objective:
    Analyze monthly new and cumulative customers to assess the growth trend.

Run:
    python customer_growth_analysis.py

Requires:
    pandas
"""

import pandas as pd


def build_dataset() -> pd.DataFrame:
    """Return monthly new-customer counts for the year."""
    return pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "NewCustomers": [100, 120, 130, 125, 150, 160,
                         175, 190, 210, 230, 260, 300],
    })


def analyze(df: pd.DataFrame) -> pd.DataFrame:
    """Add cumulative totals and month-over-month growth, then print."""
    # Running total of customers over time.
    df["TotalCustomers"] = df["NewCustomers"].cumsum()

    # Month-over-month percentage change in new acquisitions.
    df["GrowthRate%"] = (df["NewCustomers"].pct_change() * 100).round(1)

    print(df)
    print("\nTotal customers by December:", df["TotalCustomers"].iloc[-1])
    return df


def main() -> None:
    df = build_dataset()
    analyze(df)


if __name__ == "__main__":
    main()
