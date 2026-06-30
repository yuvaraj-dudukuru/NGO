"""
Business Analytics Case Study 4 — Inventory Analysis
====================================================

Business context:
    A retailer wishes to analyze product demand over the year to plan inventory,
    particularly for seasonal stock requirements.

Objective:
    Analyze monthly product demand to identify the seasonal pattern and inform
    inventory planning.

Run:
    python inventory_analysis.py

Requires:
    pandas
"""

import pandas as pd


def build_dataset() -> pd.DataFrame:
    """Return monthly product demand for the year."""
    return pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "Demand": [500, 480, 510, 530, 600, 650,
                   620, 580, 700, 850, 1100, 1400],
    })


def analyze(df: pd.DataFrame) -> pd.DataFrame:
    """Flag above-average months and report the peak."""
    avg_demand = df["Demand"].mean()
    print("Average monthly demand:", round(avg_demand, 0))

    # Flag months whose demand exceeds the yearly average.
    df["HighDemand"] = df["Demand"] > avg_demand
    high_demand_months = df.loc[df["HighDemand"], "Month"].tolist()
    print("High-demand months:", high_demand_months)

    # The single peak-demand month.
    print("Peak demand month:", df.loc[df["Demand"].idxmax(), "Month"])
    return df


def main() -> None:
    df = build_dataset()
    analyze(df)


if __name__ == "__main__":
    main()
