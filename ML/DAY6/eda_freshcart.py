"""
FreshCart Orders — Exploratory Data Analysis (EDA)
==================================================

Role  : Junior Data Analyst, FreshCart (online grocery delivery)
Goal  : Explore the orders dataset, find patterns, detect anomalies,
        explore relationships, and recommend actions to grow the business.

Run:
    python eda_freshcart.py
"""

import pandas as pd


# ----------------------------------------------------------------------
# 0. Create the dataset (simulates a cleaned, loaded file)
# ----------------------------------------------------------------------
orders = pd.DataFrame({
    "OrderID": range(1, 13),
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Delhi",
             "Mumbai", "Pune", "Delhi", "Mumbai", "Pune", "Delhi"],
    "Category": ["Fruits", "Dairy", "Fruits", "Snacks", "Dairy", "Fruits",
                 "Snacks", "Dairy", "Fruits", "Snacks", "Dairy", "Snacks"],
    "Items": [8, 15, 6, 20, 12, 9, 25, 10, 7, 30, 14, 18],
    "OrderValue": [400, 900, 320, 1200, 700, 480, 1500, 600, 380, 5000, 820, 1100],
    "DeliveryMins": [25, 40, 22, 55, 35, 28, 60, 33, 24, 75, 38, 50],
})


def section(title):
    """Pretty header to keep console output readable."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ----------------------------------------------------------------------
# 1. Explore the dataset
# ----------------------------------------------------------------------
def explore(df):
    section("1. EXPLORE THE DATASET")
    print(f"Shape (rows, cols): {df.shape}")
    print("\n--- info() ---")
    df.info()
    print("\n--- describe() ---")
    print(df.describe().round(1))


# ----------------------------------------------------------------------
# 2. Statistics: mean vs median + skew interpretation
# ----------------------------------------------------------------------
def statistics(df):
    section("2. STATISTICS (mean vs median, skew)")
    for col in ["OrderValue", "DeliveryMins"]:
        mean = df[col].mean()
        median = df[col].median()
        if mean > median * 1.05:
            skew = "RIGHT-skewed (mean > median; pulled up by large values)"
        elif mean < median * 0.95:
            skew = "LEFT-skewed (mean < median; pulled down by small values)"
        else:
            skew = "roughly symmetric (mean ~ median)"
        print(f"{col:13s} -> mean = {mean:8.1f} | median = {median:8.1f} | {skew}")


# ----------------------------------------------------------------------
# 3. Identify patterns
# ----------------------------------------------------------------------
def patterns(df):
    section("3. PATTERNS")

    print("--- Orders per city (value_counts) ---")
    city_counts = df["City"].value_counts()
    print(city_counts)
    print(f"\nCity with the MOST orders: {city_counts.idxmax()} ({city_counts.max()} orders)")

    print("\n--- Average order value per category (groupby) ---")
    cat_value = df.groupby("Category")["OrderValue"].mean().round(0).sort_values(ascending=False)
    print(cat_value)
    print(f"\nCategory with HIGHEST avg order value: {cat_value.idxmax()} (Rs {cat_value.max():.0f})")

    print("\n--- Average delivery time per city ---")
    city_delivery = df.groupby("City")["DeliveryMins"].mean().round(1).sort_values()
    print(city_delivery)


# ----------------------------------------------------------------------
# 4. Detect anomalies (IQR method on OrderValue)
# ----------------------------------------------------------------------
def detect_outliers(df):
    section("4. OUTLIER DETECTION (IQR method on OrderValue)")
    q1 = df["OrderValue"].quantile(0.25)
    q3 = df["OrderValue"].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    print(f"Q1 = {q1:.1f} | Q3 = {q3:.1f} | IQR = {iqr:.1f}")
    print(f"Acceptable range: {lower:.1f}  to  {upper:.1f}")

    outliers = df[(df["OrderValue"] < lower) | (df["OrderValue"] > upper)]
    if outliers.empty:
        print("No outliers detected.")
    else:
        print("\nOutlier(s) found:")
        print(outliers[["OrderID", "City", "Category", "Items", "OrderValue"]])
    return outliers


# ----------------------------------------------------------------------
# 5. Explore relationships (correlation)
# ----------------------------------------------------------------------
def relationships(df):
    section("5. RELATIONSHIPS (correlation)")

    c_value = df["Items"].corr(df["OrderValue"])
    c_delivery = df["Items"].corr(df["DeliveryMins"])

    print(f"Items vs OrderValue   : {c_value:+.2f}")
    print(f"Items vs DeliveryMins : {c_delivery:+.2f}")

    def interpret(name, r):
        strength = ("very strong" if abs(r) >= 0.8 else
                    "strong" if abs(r) >= 0.6 else
                    "moderate" if abs(r) >= 0.4 else
                    "weak")
        direction = "positive" if r > 0 else "negative"
        print(f"  - {name}: {strength} {direction} correlation.")

    interpret("Items vs OrderValue", c_value)
    interpret("Items vs DeliveryMins", c_delivery)
    print("  => More items generally means a higher bill AND a longer delivery time.")

    # Stretch goal: full correlation matrix
    print("\n--- Full correlation matrix (stretch goal) ---")
    print(df.corr(numeric_only=True).round(2))


# ----------------------------------------------------------------------
# Stretch goal: ideal market (high value + fast delivery)
# ----------------------------------------------------------------------
def ideal_market(df):
    section("STRETCH: IDEAL MARKET (high value + fast delivery)")
    summary = df.groupby("City").agg(
        AvgOrderValue=("OrderValue", "mean"),
        AvgDeliveryMins=("DeliveryMins", "mean"),
        Orders=("OrderID", "count"),
    ).round(1)
    print(summary)
    # Rank: high value is good (descending), fast delivery is good (ascending)
    summary["ValueRank"] = summary["AvgOrderValue"].rank(ascending=False)
    summary["SpeedRank"] = summary["AvgDeliveryMins"].rank(ascending=True)
    summary["Score"] = summary["ValueRank"] + summary["SpeedRank"]
    best = summary["Score"].idxmin()
    print(f"\nIdeal market (best blend of value + speed): {best}")


# ----------------------------------------------------------------------
# 6 & 7. Insights ladder + EDA report
# ----------------------------------------------------------------------
def report(df, outliers):
    section("6 & 7. EDA REPORT (executive summary, findings, recommendations)")

    n_orders = len(df)
    n_cities = df["City"].nunique()
    n_cats = df["Category"].nunique()
    mean_val = df["OrderValue"].mean()
    median_val = df["OrderValue"].median()

    print(f"""
EXECUTIVE SUMMARY
-----------------
Analyzed {n_orders} recent FreshCart orders across {n_cities} cities and {n_cats}
categories. Orders are fairly balanced across cities. Order value is right-
skewed (mean Rs {mean_val:.0f} vs median Rs {median_val:.0f}) due to one very large
outlier order. Order size (items) drives both revenue and delivery time.

KEY FINDINGS
------------
1. Balanced demand: each city contributes a similar number of orders.
2. Right-skewed revenue: a single large order (Order 10, Rs 5,000 in Mumbai)
   inflates the mean well above the median.
3. The IQR method flags Order 10 as a clear statistical outlier.
4. Items strongly correlate with OrderValue (more items -> higher bill).
5. Items also correlate with DeliveryMins (more items -> slower delivery).
6. Snacks tends to show the highest average order value.

INSIGHT LADDER (observation -> insight -> recommendation)
---------------------------------------------------------
Finding A
  Observation : Order 10 (Rs 5,000, 30 items) is a statistical outlier.
  Insight     : This is likely a bulk / high-value customer, not a data error.
  Recommendation: Verify the order, then nurture this customer with a loyalty
                  or B2B/bulk program instead of treating it as noise.

Finding B
  Observation : DeliveryMins rises with the number of items; the biggest order
                took 75 mins.
  Insight     : Large (often Snacks-heavy) orders are the slowest to fulfill,
                hurting customer experience.
  Recommendation: Optimize picking/packing and routing for large orders
                  (dedicated pickers, batching) to cut long delivery times.

RECOMMENDATIONS (summary)
-------------------------
- Investigate and retain the large outlier customer (bulk/loyalty offer).
- Streamline fulfillment for large orders to reduce delivery delays.
- Run promotions that increase items per order; more items = more revenue.
- Monitor Snacks demand and delivery SLAs as order sizes grow.
""")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    explore(orders)
    statistics(orders)
    patterns(orders)
    outliers = detect_outliers(orders)
    relationships(orders)
    ideal_market(orders)
    report(orders, outliers)


if __name__ == "__main__":
    main()
