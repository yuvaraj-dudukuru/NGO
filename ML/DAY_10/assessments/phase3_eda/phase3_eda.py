"""
================================================================================
PHASE 3 — EXPLORATORY DATA ANALYSIS (EDA)
================================================================================
Goal: With CLEAN data, discover the patterns that answer the business questions.

Day 6 techniques used:
    - Descriptive statistics
    - Categorical analysis (value_counts)
    - Group analysis (groupby + sum)
    - Relationship analysis (correlation)
    - Post-cleaning outlier re-check
================================================================================
"""

import numpy as np
import pandas as pd


def get_clean_data():
    """Rebuild + clean the dataset (Phase 1 + Phase 2) so this file is standalone."""
    df = pd.DataFrame({
        "OrderID":   [1001, 1002, 1003, 1003, 1005, 1006, 1007, 1008],
        "Customer":  ["asha", "RAVI", "Imran", "Imran", "Sneha", "Karan", "Meena", "Tara"],
        "City":      ["Pune", "mumbai", "Pune", "Pune", "Delhi", "Mumbai", "delhi", "Pune"],
        "Category":  ["Electronics", "Clothing", "Electronics", "Electronics",
                      "Grocery", "Electronics", "Clothing", "Grocery"],
        "Amount":    [25000, np.nan, 18000, 18000, 1200, 999999, 3200, 1500],
        "Quantity":  [2, 3, 1, 1, 5, 1, -2, 4],
        "OrderDate": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02",
                      "2026-05-03", "2026-05-03", "2026-05-04", "2026-05-05"],
    })
    df = df.drop_duplicates(subset=["OrderID"]).reset_index(drop=True)
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["Customer"] = df["Customer"].str.strip().str.title()
    df["City"] = df["City"].str.strip().str.title()
    median_qty = df.loc[df["Quantity"] > 0, "Quantity"].median()
    df["Quantity"] = df["Quantity"].astype(float)   # median may be a decimal (2.5)
    df.loc[df["Quantity"] < 0, "Quantity"] = median_qty
    Q1, Q3 = df["Amount"].quantile([0.25, 0.75])
    upper = Q3 + 1.5 * (Q3 - Q1)
    df.loc[df["Amount"] > upper, "Amount"] = np.nan
    df["Amount"] = df["Amount"].fillna(df["Amount"].median())
    return df


df = get_clean_data()

# ------------------------------------------------------------------------------
# 7.1  DESCRIPTIVE STATISTICS  (now meaningful — outlier is gone)
# ------------------------------------------------------------------------------
print("7.1  Descriptive statistics (clean data):")
print(df[["Amount", "Quantity"]].describe().round(1))

# ------------------------------------------------------------------------------
# 7.2  CATEGORICAL ANALYSIS  (how many orders per group?)
# ------------------------------------------------------------------------------
# value_counts() counts how often each category/city appears.
print("\n7.2  Orders per category:")
print(df["Category"].value_counts())
print("\nOrders per city:")
print(df["City"].value_counts())

# ------------------------------------------------------------------------------
# 7.3  GROUP ANALYSIS  (which groups bring the most MONEY?)
# ------------------------------------------------------------------------------
# groupby(col)["Amount"].sum() = total revenue per group.
# This directly answers management's core question.
print("\n7.3  Total revenue by category:")
print(df.groupby("Category")["Amount"].sum().sort_values(ascending=False))
print("\nTotal revenue by city:")
print(df.groupby("City")["Amount"].sum().sort_values(ascending=False))

# ------------------------------------------------------------------------------
# 7.4  RELATIONSHIP ANALYSIS  (does buying more = spending more?)
# ------------------------------------------------------------------------------
# corr() returns a number from -1 to +1. Near 0 = weak/no linear relationship.
# Here it may be WEAK: pricey Electronics sell in small quantities, while cheap
# Grocery sells in bulk. REMEMBER: correlation is NOT causation.
print("\n7.4  Correlation between Quantity and Amount:")
print(round(df["Quantity"].corr(df["Amount"]), 2))

# ------------------------------------------------------------------------------
# 7.5  POST-CLEANING OUTLIER CHECK
# ------------------------------------------------------------------------------
# Validation-after-cleaning principle: confirm no extreme values remain.
print("\n7.5  Amount distribution re-check (max should be reasonable now):")
print(df["Amount"].describe())

# ------------------------------------------------------------------------------
# 7.6  EDA FINDINGS
# ------------------------------------------------------------------------------
print("\n7.6  EDA FINDINGS")
print("""
- Electronics is the top REVENUE category; Pune is the most ACTIVE city.
- Grocery sells in higher QUANTITIES but lower amounts; Electronics is reverse.
- After cleaning, the data is consistent and ready to visualize (Phase 4).
""")
