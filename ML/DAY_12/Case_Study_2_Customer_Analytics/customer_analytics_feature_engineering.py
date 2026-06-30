"""
Feature Engineering Case Study 2 — Customer Analytics
=====================================================
Goal: Create advanced analytical features (RFM) for customer segmentation.

What is RFM?
    A classic marketing model that scores customers on three behaviours:
        * Recency   - how recently they last bought (lower = more engaged)
        * Frequency - how often they buy (higher = more loyal)
        * Monetary  - how much they spend in total (higher = more valuable)
    We engineer all three from a flat order log, then bucket customers into
    Bronze/Silver/Gold loyalty tiers.

Run:
    python customer_analytics_feature_engineering.py
"""

import pandas as pd


def build_raw_data():
    """Return the raw order log - one row per order (a customer may repeat)."""
    return pd.DataFrame({
        "Customer": ["Asha", "Ravi", "Asha", "Imran", "Asha", "Ravi", "Divya"],
        "Amount": [25000, 1500, 30000, 8000, 12000, 2000, 45000],
        "OrderDate": pd.to_datetime([
            "2026-01-05", "2026-02-10", "2026-03-15",
            "2026-04-20", "2026-05-25", "2026-06-01", "2026-06-10",
        ]),
    })


def engineer_features(orders, today):
    """Collapse the order log into one row per customer with RFM + a segment.

    `today` is the reference date Recency is measured against (passed in rather
    than read from the clock so results are reproducible).
    """
    # Aggregate every customer's orders into Monetary (TotalSpend), Frequency
    # (number of orders), average order value, and the date of their last order.
    customer = orders.groupby("Customer").agg(
        TotalSpend=("Amount", "sum"),      # Monetary
        Frequency=("Amount", "count"),     # Frequency
        AvgOrder=("Amount", "mean"),
        LastPurchase=("OrderDate", "max"),
    ).reset_index()

    customer["AvgOrder"] = customer["AvgOrder"].round(0)

    # Recency = days since the last purchase (smaller is better/more recent).
    customer["Recency"] = (today - customer["LastPurchase"]).dt.days

    # Loyalty tier from total spend: pd.cut maps each customer into a band.
    customer["Segment"] = pd.cut(
        customer["TotalSpend"],
        bins=[0, 10000, 40000, 1000000],          # <=10k, <=40k, above 40k
        labels=["Bronze", "Silver", "Gold"],
    )
    return customer


def main():
    orders = build_raw_data()
    today = pd.Timestamp("2026-06-18")   # fixed "as of" date for reproducibility

    customer = engineer_features(orders, today)

    print("=" * 70)
    print("Customer analytics table (RFM + loyalty segment)")
    print("=" * 70)
    print(customer)

    # Expected insight:
    #   Asha buys most often and spends the most (Gold); Divya is a single large
    #   purchase (also high value). Recency flags who may be drifting away and is
    #   worth a re-engagement nudge.


if __name__ == "__main__":
    main()
