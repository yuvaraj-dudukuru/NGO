"""
Mini Challenge — MartPro Retail Feature Engineering

You are a data analyst at "MartPro", a retail chain. Transform a raw, messy
sales export into a dashboard-ready analytical dataset with engineered features
and KPIs, then summarize the insights.

All names, emails, and values are fictional sample data for demonstration only.
"""

import pandas as pd
import numpy as np


def build_raw_data():
    """Return the raw, messy sales export."""
    return pd.DataFrame({
        "OrderID": [1, 2, 3, 4, 5, 6, 7, 8],
        "Customer": ["  asha sharma", "RAVI KUMAR", "imran khan", "asha sharma",
                     "DIVYA rao", "ravi kumar", "Karan MEHTA", "asha sharma"],
        "Email": ["asha@gmail.com", "ravi@company.com", "imran@yahoo.com",
                  "asha@gmail.com", "divya@company.com", "ravi@company.com",
                  "karan@gmail.com", "asha@gmail.com"],
        "OrderDate": ["2026-01-12", "2026-02-18", "2026-03-22", "2026-04-15",
                      "2026-05-20", "2026-06-01", "2026-06-08", "2026-06-15"],
        "Category": ["Electronics", "Grocery", "Electronics", "Clothing",
                     "Grocery", "Electronics", "Clothing", "Electronics"],
        "Units": [2, 12, 1, 5, 9, 3, 4, 1],
        "UnitPrice": [30000, 200, 60000, 1500, 250, 25000, 1200, 45000],
        "UnitCost": [22000, 150, 45000, 900, 180, 18000, 800, 33000],
    })


def transform(df):
    """Step 1 - Clean text and parse dates so the raw export is trustworthy.

    The Customer column has stray spaces and mixed case ("  asha sharma",
    "RAVI KUMAR"). .str.strip() removes surrounding spaces and .str.title()
    normalises capitalisation, so the same person is no longer counted as two.
    """
    df["Customer"] = df["Customer"].str.strip().str.title()
    # Convert the date *text* into real datetimes so we can extract month/quarter.
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    return df


def derived_metrics(df):
    """Step 2 - Engineer the money features (Revenue, Cost, Profit, Margin%)."""
    df["Revenue"] = df["Units"] * df["UnitPrice"]   # total sales value of the order
    df["Cost"] = df["Units"] * df["UnitCost"]       # total cost of goods sold
    df["Profit"] = df["Revenue"] - df["Cost"]       # money kept after cost
    df["Margin%"] = (df["Profit"] / df["Revenue"] * 100).round(1)  # profit as % of sales
    return df


def date_features(df):
    """Step 3 - Pull calendar features out of the parsed date for trend analysis."""
    df["Month"] = df["OrderDate"].dt.month_name()   # e.g. "January" - for monthly views
    df["Quarter"] = df["OrderDate"].dt.quarter      # 1-4 - for quarterly reporting
    return df


def text_features(df):
    """Step 4 - Derive features from text columns (name and email).

    .str.split(" ").str[0] takes the first token of the name (the first name).
    .str.split("@").str[1] takes the part after '@' (the email domain), which we
    use to label corporate (company.com) vs personal accounts - a B2B/B2C split.
    """
    df["FirstName"] = df["Customer"].str.split(" ").str[0]
    df["EmailDomain"] = df["Email"].str.split("@").str[1]
    df["CustomerType"] = np.where(
        df["EmailDomain"] == "company.com", "Corporate", "Personal"
    )
    return df


def category_features(df):
    """Step 5 - Bin revenue into size bands and flag high-margin orders."""
    # pd.cut buckets continuous Revenue into 3 readable bands.
    df["OrderSize"] = pd.cut(
        df["Revenue"],
        bins=[0, 5000, 50000, 1000000],            # <=5k Small, <=50k Medium, else Large
        labels=["Small", "Medium", "Large"],
    )
    # Yes/No flag for orders with margin >= 25%.
    df["HighMargin"] = np.where(df["Margin%"] >= 25, "Yes", "No")
    return df


def aggregated_kpis(df):
    """Step 6 - Add per-customer totals to every row.

    transform("sum"/"count") returns a value for EACH row (not one row per group),
    so each order also carries its customer's lifetime spend and order count -
    handy for sorting or filtering without a separate summary table.
    """
    df["TotalSpend"] = df.groupby("Customer")["Revenue"].transform("sum")
    df["OrderCount"] = df.groupby("Customer")["OrderID"].transform("count")
    return df


def validate(df):
    """7. Confirm data quality."""
    missing = int(df.isnull().sum().sum())
    negative_profit = int((df["Profit"] < 0).sum())
    margin_out = int(((df["Margin%"] < 0) | (df["Margin%"] > 100)).sum())

    print("=" * 70)
    print("Step 7 - Validation")
    print("=" * 70)
    print("Missing values:", missing)
    print("Negative profit rows:", negative_profit)
    print("Margin out of range:", margin_out)
    assert missing == 0 and negative_profit == 0 and margin_out == 0, \
        "Validation failed!"
    print("All validation checks passed.")


def summarize(df):
    """8. Insights + recommendations."""
    print("\n" + "=" * 70)
    print("Step 8 - Insights")
    print("=" * 70)

    profit_by_cat = df.groupby("Category")["Profit"].sum().sort_values(
        ascending=False
    )
    print("\nProfit by category:")
    print(profit_by_cat)

    top_customer = df.groupby("Customer")["Revenue"].sum().idxmax()
    print("\nTop customer:", top_customer)

    print("\nRevenue: Corporate vs Personal:")
    print(df.groupby("CustomerType")["Revenue"].sum())

    # Stretch: average margin per customer
    print("\nAverage margin% per customer:")
    print(df.groupby("Customer")["Margin%"].mean().round(1)
          .sort_values(ascending=False))

    print("\n" + "-" * 70)
    print("Recommendations")
    print("-" * 70)
    recs = [
        "Prioritize Electronics inventory - it is by far the most profitable "
        "category, driven by high-value laptop orders.",
        f"Nurture top customers like {top_customer} with loyalty offers "
        "(highest TotalSpend, repeat Electronics orders).",
        "Develop targeted strategies for the Corporate (company.com) vs "
        "Personal segments - a B2B vs B2C play.",
        "Promote high-margin products: most high-value orders are Large, "
        "HighMargin Electronics.",
    ]
    for i, rec in enumerate(recs, 1):
        print(f"{i}. {rec}")


def main():
    df = build_raw_data()
    df = transform(df)
    df = derived_metrics(df)
    df = date_features(df)
    df = text_features(df)
    df = category_features(df)
    df = aggregated_kpis(df)

    print("=" * 70)
    print("Dashboard-ready dataset (key columns)")
    print("=" * 70)
    print(df[[
        "OrderID", "Customer", "Category", "Revenue", "Profit", "Margin%",
        "CustomerType", "OrderSize", "HighMargin", "TotalSpend", "OrderCount",
    ]])

    validate(df)
    summarize(df)
    return df


if __name__ == "__main__":
    main()
