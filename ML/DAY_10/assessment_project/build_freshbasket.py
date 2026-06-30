"""
================================================================================
FreshBasket — END-TO-END ANALYSIS PIPELINE  (Day 10 Assessment Project)
================================================================================
Junior analyst deliverable. This single script reproduces the WHOLE project:

    Step 1  Load & inspect        (Day 4)
    Step 2  Clean                 (Day 5)
    Step 3  Explore (EDA)         (Day 6)
    Step 4  Visualize             (Day 7/8)  -> saves PNGs at dpi=300
    Step 5  SQL analysis          (Day 9)
    Step 6  Insights              (insight ladder)
    Step 7  (report is written separately in EDA_REPORT.md)

Running this file produces two of the five deliverables automatically:
    * freshbasket_clean.csv          (the clean dataset)
    * charts/*.png                   (the saved visualizations, dpi=300)

The Jupyter notebook (freshbasket_analysis.ipynb) contains the SAME code split
into labelled cells with Markdown explanations.
================================================================================
"""

import os
import sqlite3
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")               # save charts without needing a display
import matplotlib.pyplot as plt
import seaborn as sns

HERE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(HERE, "charts")
os.makedirs(CHARTS, exist_ok=True)


# ==============================================================================
# STEP 1 — LOAD DATASET & FIRST INSPECTION  (Day 4)
# ==============================================================================
data = pd.DataFrame({
    "OrderID":   [201, 202, 203, 203, 205, 206, 207, 208, 209, 210],
    "Customer":  ["  ravi", "ASHA", "imran", "imran", "Divya",
                  "KARAN", "meena ", "Sahil", "tara", "Asha"],
    "City":      ["Pune", "mumbai", "Pune", "Pune", "Delhi",
                  "Mumbai", "delhi", "Pune", "Mumbai", "mumbai"],
    "Category":  ["Electronics", "Grocery", "Electronics", "Electronics", "Grocery",
                  "Clothing", "Grocery", "Electronics", "Clothing", "Grocery"],
    "Amount":    [45000, 1200, 38000, 38000, np.nan, 2500, 999999, 52000, 3200, 1500],
    "Quantity":  [1, 8, 1, 1, 6, 2, -3, 1, 2, 5],
    "OrderDate": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02", "2026-05-03",
                  "2026-05-04", "2026-05-05", "2026-05-06", "2026-05-07", "2026-05-08"],
})

print("=" * 70, "\nSTEP 1 — LOAD & INSPECT\n", "=" * 70, sep="")
print("\nhead():")
print(data.head())
print("\nshape:", data.shape)            # (10, 7)
print("\ninfo():")
data.info()
print("\ndescribe():")
print(data.describe())
print("""
Red flags spotted:
  - Amount max 999999  -> outlier (data-entry typo)
  - Quantity min -3     -> impossible value
  - Amount has 1 missing (OrderID 205)
  - OrderID 203 appears twice -> duplicate
  - Customer/City have mixed case & stray spaces
  - OrderDate is text, not a real date
""")


# ==============================================================================
# STEP 2 — CLEAN DATASET  (Day 5)
# ==============================================================================
print("=" * 70, "\nSTEP 2 — CLEAN\n", "=" * 70, sep="")
df = data.copy()

# 2a. Remove the duplicate on the business key (OrderID 203).
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates(subset=["OrderID"]).reset_index(drop=True)
print("Shape after dedup:", df.shape)        # (9, 7)

# 2b. Fix data type: OrderDate text -> real datetime.
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# 2c. Standardize text: strip spaces, consistent Title casing.
df["Customer"] = df["Customer"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# 2d. Validate Quantity: -3 is impossible -> replace with median of valid values.
median_qty = df.loc[df["Quantity"] > 0, "Quantity"].median()
df["Quantity"] = df["Quantity"].astype(float)   # median can be a decimal
df.loc[df["Quantity"] < 0, "Quantity"] = median_qty

# 2e. Handle outlier + missing Amount. Inspect first with the IQR rule.
Q1, Q3 = df["Amount"].quantile([0.25, 0.75])
upper = Q3 + 1.5 * (Q3 - Q1)
print("IQR upper fence for Amount:", round(upper, 1))
print("Flagged as outlier:")
print(df[df["Amount"] > upper][["OrderID", "Amount"]])
# 999999 is a clear typo -> treat as missing, then fill BOTH NaNs with the median.
df.loc[df["Amount"] > upper, "Amount"] = np.nan
df["Amount"] = df["Amount"].fillna(df["Amount"].median())

# 2f. Validate the result.
assert df.isnull().sum().sum() == 0, "missing values remain!"
assert df.duplicated(subset=["OrderID"]).sum() == 0, "duplicates remain!"
assert (df["Quantity"] > 0).all(), "invalid quantity remains!"
print("\nValidation passed: 0 missing, 0 duplicates, all quantities positive.")
print("\nClean data:")
print(df)

# DELIVERABLE 1: export the clean dataset.
csv_path = os.path.join(HERE, "freshbasket_clean.csv")
df.to_csv(csv_path, index=False)
print("\nSaved clean dataset ->", csv_path)


# ==============================================================================
# STEP 3 — EXPLORE (EDA)  (Day 6)
# ==============================================================================
print("=" * 70, "\nSTEP 3 — EXPLORE\n", "=" * 70, sep="")
print("Descriptive stats:\n", df[["Amount", "Quantity"]].describe().round(1), sep="")
print("\nOrders per category:\n", df["Category"].value_counts(), sep="")
print("\nOrders per city:\n", df["City"].value_counts(), sep="")

rev_by_cat = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
rev_by_city = df.groupby("City")["Amount"].sum().sort_values(ascending=False)
print("\nRevenue by category:\n", rev_by_cat, sep="")
print("\nRevenue by city:\n", rev_by_city, sep="")

corr_val = df["Quantity"].corr(df["Amount"])
print("\nCorrelation (Quantity vs Amount):", round(corr_val, 2))


# ==============================================================================
# STEP 4 — VISUALIZE  (Day 7/8)  -> 5 charts saved at dpi=300
# ==============================================================================
print("=" * 70, "\nSTEP 4 — VISUALIZE\n", "=" * 70, sep="")
sns.set_theme(style="whitegrid")


def save(name):
    plt.tight_layout()
    path = os.path.join(CHARTS, name)
    plt.savefig(path, dpi=300)         # dpi=300 as required
    plt.close()
    print("saved:", path)


# (a) Bar — revenue by category
plt.figure()
sns.barplot(x=rev_by_cat.index, y=rev_by_cat.values)
plt.title("Total Revenue by Category"); plt.xlabel("Category"); plt.ylabel("Revenue (Rs.)")
save("01_revenue_by_category.png")

# (b) Bar — revenue by city
plt.figure()
sns.barplot(x=rev_by_city.index, y=rev_by_city.values)
plt.title("Total Revenue by City"); plt.xlabel("City"); plt.ylabel("Revenue (Rs.)")
save("02_revenue_by_city.png")

# (c) Histogram — distribution of order amounts
plt.figure()
sns.histplot(df["Amount"], bins=6, kde=True)
plt.title("Distribution of Order Amounts"); plt.xlabel("Amount (Rs.)"); plt.ylabel("Count")
save("03_amount_distribution.png")

# (d) Box plot — amount by category
plt.figure()
sns.boxplot(data=df, x="Category", y="Amount")
plt.title("Order Amount by Category"); plt.xlabel("Category"); plt.ylabel("Amount (Rs.)")
save("04_amount_by_category_box.png")

# (e) Scatter — quantity vs amount, colored by category
plt.figure()
sns.scatterplot(data=df, x="Quantity", y="Amount", hue="Category", s=120)
plt.title("Quantity vs Amount by Category"); plt.xlabel("Quantity"); plt.ylabel("Amount (Rs.)")
save("05_quantity_vs_amount.png")

# (f) Heatmap — correlation
plt.figure()
sns.heatmap(df[["Amount", "Quantity"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
save("06_correlation_heatmap.png")


# ==============================================================================
# STEP 5 — SQL ANALYSIS  (Day 9)
# ==============================================================================
print("=" * 70, "\nSTEP 5 — SQL ANALYSIS\n", "=" * 70, sep="")
conn = sqlite3.connect(":memory:")
df.to_sql("sales", conn, index=False, if_exists="replace")

q_top_cat = ("SELECT Category, SUM(Amount) AS TotalRevenue FROM sales "
             "GROUP BY Category ORDER BY TotalRevenue DESC")
q_top_city = ("SELECT City, SUM(Amount) AS Revenue FROM sales "
              "GROUP BY City ORDER BY Revenue DESC")
q_high_value = ("SELECT Customer, Category, Amount FROM sales "
                "WHERE Amount > 10000 ORDER BY Amount DESC")
q_pune = "SELECT Customer, Amount FROM sales WHERE City = 'Pune'"

print("Q1 Top revenue category:\n", pd.read_sql(q_top_cat, conn), sep="")
print("\nQ2 Top city by revenue:\n", pd.read_sql(q_top_city, conn), sep="")
print("\nQ3 High-value orders (> 10000):\n", pd.read_sql(q_high_value, conn), sep="")
print("\nQ4 Pune customers:\n", pd.read_sql(q_pune, conn), sep="")
conn.close()


# ==============================================================================
# STEP 6 — INSIGHTS (insight ladder)
# ==============================================================================
print("=" * 70, "\nSTEP 6 — INSIGHTS\n", "=" * 70, sep="")
print("""
Observation    : Electronics revenue (Rs.135,000) dwarfs Grocery (9,100) & Clothing (5,700).
Finding        : Electronics earns ~90% of revenue from just 3 large orders.
Insight        : Revenue is concentrated in a handful of high-value Electronics sales.
Recommendation : Protect Electronics stock; never let best-sellers go out of stock.

Observation    : Mumbai has the MOST orders (4) but Pune has the MOST revenue (Rs.135,000).
Finding        : Pune's revenue lead comes entirely from its Electronics orders.
Insight        : Order COUNT and REVENUE point to different 'top' cities - Pune is the
                 high-value market, Mumbai is the high-frequency market.
Recommendation : Push Electronics promotions in Pune; use loyalty offers to lift Mumbai's
                 average order value.

Observation    : Grocery sells in high quantities but low amounts (corr Quantity~Amount = -0.62).
Finding        : Buying more units goes WITH spending less - Grocery bulk vs single Electronics.
Insight        : Grocery is a customer-acquisition channel, not a profit centre.
Recommendation : Use Grocery deals to attract buyers, then upsell Electronics.

Observation    : One order was recorded as Rs.999999 (now corrected).
Finding        : A data-entry error slipped into the export.
Insight        : Input controls at order entry are weak.
Recommendation : Add validation (amount/quantity range checks) at data entry.
""")

print("DONE. Deliverables generated: freshbasket_clean.csv + charts/*.png")
