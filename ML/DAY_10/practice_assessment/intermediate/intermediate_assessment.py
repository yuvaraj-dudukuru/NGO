"""
================================================================================
INTERMEDIATE PRACTICE ASSESSMENT
================================================================================
Dataset: 10 orders (MESSY) — 1 missing amount, 1 duplicate, inconsistent city case.

Tasks:
    1. Detect and report all data-quality issues.
    2. Clean the dataset (missing, duplicate, text).
    3. Compute total revenue by city with groupby().
    4. Create a histogram of amounts and a box plot by city.
    5. Write three findings.
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# Messy 10-order dataset:
#   - OrderID 305 is duplicated
#   - one Amount is missing (NaN)
#   - City case is inconsistent ("mumbai"/"Mumbai", "delhi"/"Delhi")
df = pd.DataFrame({
    "OrderID": [301, 302, 303, 304, 305, 305, 307, 308, 309, 310],
    "City":    ["Pune", "mumbai", "Delhi", "Pune", "Mumbai",
                "Mumbai", "delhi", "Pune", "mumbai", "Delhi"],
    "Amount":  [1200, 2500, np.nan, 4300, 1800, 1800, 900, 5200, 2100, 3000],
})

# --- Task 1: DETECT issues ---------------------------------------------------
print("=== Task 1: Data-quality report ===")
print("Missing values per column:\n", df.isnull().sum(), sep="")
print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate OrderIDs:", df.duplicated(subset=["OrderID"]).sum())
print("\nCity values BEFORE cleaning (note mixed case):")
print(df["City"].value_counts())

# --- Task 2: CLEAN -----------------------------------------------------------
print("\n=== Task 2: Cleaning ===")
# Remove duplicate on the business key.
df = df.drop_duplicates(subset=["OrderID"]).reset_index(drop=True)
# Standardize city text (strip spaces + Title case) so groups merge correctly.
df["City"] = df["City"].str.strip().str.title()
# Fill the missing amount with the median (robust to outliers).
df["Amount"] = df["Amount"].fillna(df["Amount"].median())

print("City values AFTER cleaning:")
print(df["City"].value_counts())        # Mumbai 3, Pune 3, Delhi 3
assert df.isnull().sum().sum() == 0 and df.duplicated().sum() == 0
print("Clean: 0 missing, 0 duplicates.")

# --- Task 3: Revenue by city -------------------------------------------------
print("\n=== Task 3: Total revenue by city ===")
rev = df.groupby("City")["Amount"].sum().sort_values(ascending=False)
print(rev)

# --- Task 4: Histogram + box plot --------------------------------------------
sns.set_theme(style="whitegrid")

plt.figure()
sns.histplot(df["Amount"], bins=6, kde=True)
plt.title("Distribution of Order Amounts"); plt.xlabel("Amount"); plt.ylabel("Count")
plt.tight_layout(); plt.savefig("amount_histogram.png", dpi=150)

plt.figure()
sns.boxplot(data=df, x="City", y="Amount")
plt.title("Order Amount by City"); plt.xlabel("City"); plt.ylabel("Amount")
plt.tight_layout(); plt.savefig("amount_by_city_box.png", dpi=150)
print("\nSaved charts -> amount_histogram.png, amount_by_city_box.png")

# --- Task 5: Three findings --------------------------------------------------
print("\n=== Task 5: Three findings ===")
print(f"""
1. {rev.index[0]} is the top-revenue city (Rs.{rev.iloc[0]:.0f}); the three cities
   are fairly close, so no single market dominates.
2. After standardizing case, each city has 3 orders - the earlier 'imbalance'
   was a TEXT problem, not a real one.
3. Order amounts cluster at the low end with a few larger orders - the box plot
   shows Pune carries the highest-value orders.
""")
