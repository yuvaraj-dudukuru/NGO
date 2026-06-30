"""
============================================================================
EDA Case Study 2 — Sales Dataset
============================================================================
Goal : Analyse a regional sales dataset to find which regions and products
       drive revenue, check for unusually large sales, and recommend actions.

EDA workflow used here:
    1. Inspect the data (head) and engineer a Revenue column
    2. Statistics and group analysis (totals by region / product)
    3. Outlier / spread check on Revenue
    4. Findings, insights and recommendations

Run:
    python case_study_2_sales.py
============================================================================
"""

import pandas as pd


# --------------------------------------------------------------------------
# 19.1  THE DATASET AND INSPECTION
# --------------------------------------------------------------------------
# Each row is one sales record: which region, which product, units sold and
# unit price.
sales = pd.DataFrame({
    "Region":  ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Product": ["A", "B", "A", "C", "C", "A", "B", "A"],
    "Units":   [20, 35, 50, 15, 40, 25, 30, 60],
    "Price":   [500, 300, 500, 999, 999, 500, 300, 500],
})

# Feature engineering: Revenue = Units * Price (money earned per record).
sales["Revenue"] = sales["Units"] * sales["Price"]

# Quick look at the first rows to confirm Revenue was computed correctly.
print("First rows (head):")
print(sales.head())


# --------------------------------------------------------------------------
# 19.2  STATISTICS AND GROUP ANALYSIS
# --------------------------------------------------------------------------
# Total revenue across every record -> the headline business number.
print("\nTotal revenue:", sales["Revenue"].sum())

# groupby("Region") + sum -> revenue contributed by each region.
# sort_values(ascending=False) lists the strongest market first.
print("\nRevenue by region (highest first):")
print(sales.groupby("Region")["Revenue"].sum().sort_values(ascending=False))

# Same idea grouped by Product -> which products earn the most.
print("\nRevenue by product (highest first):")
print(sales.groupby("Product")["Revenue"].sum().sort_values(ascending=False))


# --------------------------------------------------------------------------
# 19.3  OUTLIER CHECK
# --------------------------------------------------------------------------
# describe() on Revenue shows the spread (min, mean, max). A max far above the
# mean hints at a stand-out high-value sale worth investigating.
print("\nRevenue distribution (outlier check):")
print(sales["Revenue"].describe().round(0))


# --------------------------------------------------------------------------
# 19.4  FINDINGS AND CONCLUSIONS
# --------------------------------------------------------------------------
print("""
------------------------- FINDINGS & CONCLUSIONS -------------------------
Finding 1: North generates the most revenue (49,960); South the least (23,000).
    Insight: North is the strongest market; South is underperforming.
    (Total revenue across all records = 151,945.)

Finding 2: Product A drives the most revenue (77,500) via high volume;
    Product C earns strongly (54,945) via high price.
    Insight: A is a volume product, C is a premium product.

Finding 3: The highest single sale (39,960 - North / Product C) stands out.
    Insight: Premium products sell well in the North.

Recommendation: Investigate why South lags and replicate North's success there;
    keep promoting Product A for volume and Product C as a premium offering.
--------------------------------------------------------------------------
""")
