"""
================================================================================
ADVANCED PRACTICE ASSESSMENT — mini end-to-end project (12-row messy sales)
================================================================================
Follows the seven phases of the worked example:
    1. Clean fully (missing, duplicates, types, text, invalid values, outliers)
    2. EDA (statistics, groupby by city & category, correlation)
    3. Four+ visualizations (bar, histogram, box, scatter/heatmap)
    4. SQLite + three business queries
    5. Insight ladder for three findings
    6. Complete EDA report (written separately in EDA_REPORT.md)

Running this generates: sales_clean.csv  +  charts/*.png  (dpi=300).
================================================================================
"""

import os
import sqlite3
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

HERE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(HERE, "charts")
os.makedirs(CHARTS, exist_ok=True)

# ---- Raw messy 12-row dataset ------------------------------------------------
# Problems planted: duplicate (OrderID 404), missing Amount, invalid Quantity
# (-4), outlier Amount (888888), messy text/case, OrderDate as text.
raw = pd.DataFrame({
    "OrderID":   [401, 402, 403, 404, 404, 406, 407, 408, 409, 410, 411, 412],
    "Customer":  ["  neha", "ROHIT", "sara ", "amit", "amit", "Priya",
                  "VIKAS", "tina", "Mohit ", "  zoya", "Arjun", "kavya"],
    "City":      ["Pune", "mumbai", "Delhi", "Pune", "Pune", "Mumbai",
                  "delhi", "Pune", "mumbai", "Delhi", "Mumbai", "pune"],
    "Category":  ["Electronics", "Grocery", "Clothing", "Electronics", "Electronics",
                  "Grocery", "Clothing", "Electronics", "Grocery", "Clothing",
                  "Electronics", "Grocery"],
    "Amount":    [60000, 1500, 2800, 47000, 47000, 1900, 3500, 55000,
                  np.nan, 4100, 888888, 1700],
    "Quantity":  [1, 7, 2, 1, 1, 5, 2, 1, 6, 3, -4, 8],
    "OrderDate": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-03", "2026-05-03",
                  "2026-05-04", "2026-05-05", "2026-05-06", "2026-05-07", "2026-05-08",
                  "2026-05-09", "2026-05-10"],
})

# ============================================================================
# PHASE 1 — CLEAN
# ============================================================================
print("=== PHASE 1: CLEAN ===")
df = raw.copy()
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates(subset=["OrderID"]).reset_index(drop=True)   # drop dup 404
df["OrderDate"] = pd.to_datetime(df["OrderDate"])                    # fix type
df["Customer"] = df["Customer"].str.strip().str.title()             # text
df["City"] = df["City"].str.strip().str.title()

# invalid quantity (-4) -> median of valid; cast to float (median may be decimal)
mq = df.loc[df["Quantity"] > 0, "Quantity"].median()
df["Quantity"] = df["Quantity"].astype(float)
df.loc[df["Quantity"] < 0, "Quantity"] = mq

# outlier + missing Amount: inspect via IQR, then median-fill both
Q1, Q3 = df["Amount"].quantile([0.25, 0.75])
upper = Q3 + 1.5 * (Q3 - Q1)
print("IQR upper fence:", round(upper, 1))
print("Outlier(s):\n", df[df["Amount"] > upper][["OrderID", "Amount"]], sep="")
df.loc[df["Amount"] > upper, "Amount"] = np.nan
df["Amount"] = df["Amount"].fillna(df["Amount"].median())

assert df.isnull().sum().sum() == 0 and df.duplicated(subset=["OrderID"]).sum() == 0
assert (df["Quantity"] > 0).all()
print("Validation passed. Clean shape:", df.shape)
df.to_csv(os.path.join(HERE, "sales_clean.csv"), index=False)
print("Saved sales_clean.csv")

# ============================================================================
# PHASE 2 — EDA
# ============================================================================
print("\n=== PHASE 2: EDA ===")
print(df[["Amount", "Quantity"]].describe().round(1))
rev_cat = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
rev_city = df.groupby("City")["Amount"].sum().sort_values(ascending=False)
print("\nRevenue by category:\n", rev_cat, sep="")
print("\nRevenue by city:\n", rev_city, sep="")
print("\nCorrelation (Quantity vs Amount):", round(df["Quantity"].corr(df["Amount"]), 2))

# ============================================================================
# PHASE 3 — VISUALIZE  (bar, histogram, box, scatter, heatmap)
# ============================================================================
print("\n=== PHASE 3: VISUALIZE ===")
sns.set_theme(style="whitegrid")


def save(name):
    plt.tight_layout(); plt.savefig(os.path.join(CHARTS, name), dpi=300); plt.close()


plt.figure(); sns.barplot(x=rev_cat.index, y=rev_cat.values)
plt.title("Revenue by Category"); plt.xlabel("Category"); plt.ylabel("Revenue (Rs.)")
save("01_revenue_by_category.png")

plt.figure(); sns.histplot(df["Amount"], bins=6, kde=True)
plt.title("Distribution of Order Amounts"); plt.xlabel("Amount (Rs.)"); plt.ylabel("Count")
save("02_amount_distribution.png")

plt.figure(); sns.boxplot(data=df, x="Category", y="Amount")
plt.title("Order Amount by Category"); plt.xlabel("Category"); plt.ylabel("Amount (Rs.)")
save("03_amount_by_category_box.png")

plt.figure(); sns.scatterplot(data=df, x="Quantity", y="Amount", hue="Category", s=120)
plt.title("Quantity vs Amount by Category"); plt.xlabel("Quantity"); plt.ylabel("Amount (Rs.)")
save("04_quantity_vs_amount.png")

plt.figure(); sns.heatmap(df[["Amount", "Quantity"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
save("05_correlation_heatmap.png")
print("Saved 5 charts to charts/ (dpi=300)")

# ============================================================================
# PHASE 4 — SQL  (three business queries)
# ============================================================================
print("\n=== PHASE 4: SQL ===")
conn = sqlite3.connect(":memory:")
df.to_sql("sales", conn, index=False, if_exists="replace")
print("Q1 Top revenue category:\n",
      pd.read_sql("SELECT Category, SUM(Amount) AS Rev FROM sales "
                  "GROUP BY Category ORDER BY Rev DESC", conn), sep="")
print("\nQ2 Top city by revenue:\n",
      pd.read_sql("SELECT City, SUM(Amount) AS Rev FROM sales "
                  "GROUP BY City ORDER BY Rev DESC", conn), sep="")
print("\nQ3 High-value orders (> 10000):\n",
      pd.read_sql("SELECT Customer, Category, Amount FROM sales "
                  "WHERE Amount > 10000 ORDER BY Amount DESC", conn), sep="")
conn.close()

# ============================================================================
# PHASE 5 — INSIGHT LADDER  (three findings)
# ============================================================================
print("\n=== PHASE 5: INSIGHTS ===")
print("""
1. OBS: Electronics has the highest total revenue.
   FIND: A few large Electronics orders create most revenue.
   INSIGHT: Revenue depends on a handful of high-value sales.
   RECOMMEND: Protect Electronics stock and key buyers.

2. OBS: Grocery has high quantities but low amounts (negative corr).
   FIND: Buying more units goes with lower spend.
   INSIGHT: Grocery is a footfall driver, not a profit centre.
   RECOMMEND: Use Grocery promos to attract, then upsell Electronics.

3. OBS: One order was 888888 and one quantity was -4 (both fixed).
   FIND: Multiple data-entry errors reached the export.
   INSIGHT: Entry-side validation is weak.
   RECOMMEND: Add range checks on Amount and Quantity at entry.
""")
print("DONE. See EDA_REPORT.md for the full written report.")
