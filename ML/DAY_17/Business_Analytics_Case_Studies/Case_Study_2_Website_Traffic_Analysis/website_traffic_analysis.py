"""
Business Analytics Case Study 2 — Website Traffic Analysis
==========================================================

Business context:
    A digital business wishes to analyze its daily website traffic to identify
    growth, weekday patterns, and peak periods.

Objective:
    Analyze daily website visitors to identify the trend and the weekday pattern.

Run:
    python website_traffic_analysis.py

Requires:
    pandas
"""

import pandas as pd


def build_dataset() -> pd.DataFrame:
    """Return two weeks of daily visitor counts."""
    df = pd.DataFrame({
        "Date": pd.to_datetime(pd.date_range("2025-06-02", periods=14, freq="D")),
        "Visitors": [
            1200, 1350, 1300, 1400, 1800, 1900, 1100,
            1300, 1450, 1400, 1500, 1950, 2050, 1200,
        ],
    })
    # Extract the weekday name (Monday, Tuesday, ...) for the weekly pattern.
    df["DayName"] = df["Date"].dt.day_name()
    return df


def analyze(df: pd.DataFrame) -> None:
    """Print the weekday pattern and the smoothed trend."""
    # Average visitors per weekday reveals the weekly seasonal pattern.
    weekday_avg = df.groupby("DayName")["Visitors"].mean().round(0)
    print("Average visitors by day of week:")
    print(weekday_avg)

    # A 7-day moving average spans a full week, removing weekly fluctuation
    # and exposing the underlying trend.
    df["MovingAvg_7"] = df["Visitors"].rolling(window=7).mean()
    print("\nFirst and last 7-day moving averages:")
    print(df["MovingAvg_7"].dropna().iloc[[0, -1]])


def main() -> None:
    df = build_dataset()
    analyze(df)


if __name__ == "__main__":
    main()
