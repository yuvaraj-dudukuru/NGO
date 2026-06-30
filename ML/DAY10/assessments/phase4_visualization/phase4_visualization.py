"""
================================================================================
PHASE 4 — VISUALIZATION
================================================================================
Goal: COMMUNICATE the Phase 3 findings visually (Matplotlib Day 7 + Seaborn Day 8).

Discipline: every chart is chosen to answer ONE specific question, never for
decoration. For each chart we note: WHY chosen, WHAT it reveals, and the
BUSINESS interpretation.

This script SAVES each chart as a .png in this folder (so it works even without
a screen) AND shows them if a display is available.
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # 'Agg' backend = save to file without a display.
import matplotlib.pyplot as plt
import seaborn as sns


def get_clean_data():
    """Rebuild + clean the dataset so this file runs standalone (see Phase 2)."""
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
    mq = df.loc[df["Quantity"] > 0, "Quantity"].median()
    df["Quantity"] = df["Quantity"].astype(float)   # median may be a decimal (2.5)
    df.loc[df["Quantity"] < 0, "Quantity"] = mq
    Q1, Q3 = df["Amount"].quantile([0.25, 0.75])
    upper = Q3 + 1.5 * (Q3 - Q1)
    df.loc[df["Amount"] > upper, "Amount"] = np.nan
    df["Amount"] = df["Amount"].fillna(df["Amount"].median())
    return df


df = get_clean_data()
sns.set_theme(style="whitegrid")   # clean, professional default styling.


def save(fig_name):
    """Save the current figure and close it (frees memory)."""
    plt.tight_layout()
    plt.savefig(fig_name, dpi=120)
    plt.close()
    print("saved:", fig_name)


# 8.1  BAR CHART — Revenue by Category --------------------------------------
# WHY: bars compare distinct categories. REVEALS: top-earning category.
cat_rev = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
plt.figure()
sns.barplot(x=cat_rev.index, y=cat_rev.values)
plt.title("Total Revenue by Category"); plt.xlabel("Category"); plt.ylabel("Revenue")
save("chart_01_revenue_by_category.png")

# 8.2  BAR CHART — Revenue by City ------------------------------------------
# REVEALS: strongest vs weakest markets.
city_rev = df.groupby("City")["Amount"].sum().sort_values(ascending=False)
plt.figure()
sns.barplot(x=city_rev.index, y=city_rev.values)
plt.title("Total Revenue by City"); plt.xlabel("City"); plt.ylabel("Revenue")
save("chart_02_revenue_by_city.png")

# 8.3  HISTOGRAM — Distribution of Order Amounts ----------------------------
# WHY: a histogram shows the spread of ONE numeric variable. REVEALS: skew —
# whether revenue rides on a few big orders.
plt.figure()
sns.histplot(df["Amount"], bins=6, kde=True)
plt.title("Distribution of Order Amounts"); plt.xlabel("Amount"); plt.ylabel("Count")
save("chart_03_amount_distribution.png")

# 8.4  BOX PLOT — Amount by Category (outlier check) ------------------------
# WHY: box plots show spread + flag outliers automatically. REVEALS: which
# category has the highest/most variable order values.
plt.figure()
sns.boxplot(data=df, x="Category", y="Amount")
plt.title("Order Amount by Category")
save("chart_04_amount_by_category_box.png")

# 8.5  SCATTER — Quantity vs Amount -----------------------------------------
# WHY: scatter shows the relationship between TWO numeric variables.
# hue colors points by category to expose the two buying patterns.
plt.figure()
sns.scatterplot(data=df, x="Quantity", y="Amount", hue="Category")
plt.title("Quantity vs Amount by Category")
save("chart_05_quantity_vs_amount.png")

# 8.6  HEATMAP — Correlation ------------------------------------------------
# WHY: a heatmap visualizes the correlation matrix at a glance.
corr = df[["Amount", "Quantity"]].corr()
plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
save("chart_06_correlation_heatmap.png")

print("\nAll 6 charts saved as PNG files in this folder.")
