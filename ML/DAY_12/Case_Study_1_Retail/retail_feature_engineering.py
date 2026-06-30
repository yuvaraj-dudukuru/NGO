"""
Feature Engineering Case Study 1 — Retail
=========================================
Goal: Transform a raw retail sales table into a *dashboard-ready* dataset.

What is feature engineering?
    Creating new, more useful columns ("features") from the raw ones. A raw row
    only knows Units, UnitPrice and UnitCost; a dashboard needs Revenue, Profit,
    margins, the month name, and easy-to-read category bands. We derive all of
    those here.

Run:
    python retail_feature_engineering.py
"""

import pandas as pd
import numpy as np


def build_raw_data():
    """Return the raw retail sales table (the 6 columns we start from).

    Hard-coded so the script is self-contained and reproducible.
    """
    return pd.DataFrame({
        "OrderID": [1, 2, 3, 4, 5],
        "OrderDate": pd.to_datetime([
            "2026-01-15", "2026-02-20", "2026-03-10",
            "2026-04-05", "2026-05-18",
        ]),
        "Category": ["Electronics", "Grocery", "Electronics", "Clothing", "Grocery"],
        "Units": [2, 10, 1, 5, 8],
        "UnitPrice": [30000, 200, 60000, 1500, 250],   # what the customer pays each
        "UnitCost": [22000, 150, 45000, 900, 180],     # what it costs us each
    })


def engineer_features(retail):
    """Add 7 engineered features to the raw retail table.

    Each new column answers a business question the raw data cannot answer on its own.
    """
    # Money features: scale per-unit figures up by quantity sold.
    retail["Revenue"] = retail["Units"] * retail["UnitPrice"]   # total sales value
    retail["Cost"] = retail["Units"] * retail["UnitCost"]       # total cost of goods
    retail["Profit"] = retail["Revenue"] - retail["Cost"]       # what we actually keep

    # Profitability ratio: profit as a % of revenue (round to 1 dp for readability).
    retail["ProfitMargin%"] = (retail["Profit"] / retail["Revenue"] * 100).round(1)

    # Date feature: pull the month *name* out of the date for grouping/trend charts.
    retail["Month"] = retail["OrderDate"].dt.month_name()

    # Binning: turn continuous Revenue into 3 labelled bands so non-analysts can
    # read "Large order" instead of interpreting a raw number. pd.cut assigns each
    # row to the bin its Revenue falls into.
    retail["OrderSize"] = pd.cut(
        retail["Revenue"],
        bins=[0, 5000, 50000, 1000000],          # boundaries: <=5k, <=50k, above
        labels=["Small", "Medium", "Large"],
    )

    # Flag feature: a simple Yes/No marker for high-margin orders (>= 25%).
    # np.where(condition, value_if_true, value_if_false) is a vectorised if/else.
    retail["HighMargin"] = np.where(retail["ProfitMargin%"] >= 25, "Yes", "No")
    return retail


def main():
    # Build the raw table, then enrich it with the engineered features.
    retail = build_raw_data()
    retail = engineer_features(retail)

    print("=" * 70)
    print("Dashboard-ready dataset")
    print("=" * 70)
    # Show only the columns a dashboard would use (hide the intermediate ones).
    print(retail[[
        "OrderID", "Category", "Revenue", "Profit", "ProfitMargin%",
        "Month", "OrderSize", "HighMargin",
    ]])

    # A quick payoff: now that Profit exists, one groupby answers "which category
    # earns us the most money?" - impossible from the raw table alone.
    print("\n" + "=" * 70)
    print("Quick analysis: total profit by category")
    print("=" * 70)
    print(retail.groupby("Category")["Profit"].sum().sort_values(ascending=False))


if __name__ == "__main__":
    main()
