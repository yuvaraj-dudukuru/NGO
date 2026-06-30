"""
================================================================================
PHASE 2 — DATA CLEANING
================================================================================
Goal: Turn the messy data into a TRUSTWORTHY dataset.

We follow the Day 5 cleaning workflow, IN ORDER:
    detect -> handle missing -> remove duplicates -> fix types
           -> standardize text -> validate values -> handle outliers

The ORDER matters. (e.g. we dedupe before computing medians so duplicates do
not skew the fill values.)
================================================================================
"""

import numpy as np
import pandas as pd


def build_raw_data():
    """Rebuild the same raw dataset from Phase 1 so this file runs standalone."""
    return pd.DataFrame({
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


df = build_raw_data()

# ------------------------------------------------------------------------------
# 6.1  MISSING VALUE DETECTION
# ------------------------------------------------------------------------------
# .isnull() -> True/False grid of missing cells; .sum() counts per column.
print("6.1  Missing values per column:")
print(df.isnull().sum())
# Expect: only Amount = 1 (the Clothing order, row index 1).

# ------------------------------------------------------------------------------
# 6.2  DUPLICATE DETECTION AND REMOVAL
# ------------------------------------------------------------------------------
print("\n6.2  Duplicates before:", df.duplicated().sum())
# We dedupe on the UNIQUE KEY (OrderID), not the whole row. This is the
# Day 5/9 best practice: the business key defines a unique record.
# reset_index(drop=True) renumbers rows cleanly after dropping.
df = df.drop_duplicates(subset=["OrderID"]).reset_index(drop=True)
print("Shape after dedup:", df.shape)   # Expect (7, 7)

# ------------------------------------------------------------------------------
# 6.3  DATA TYPE CORRECTIONS
# ------------------------------------------------------------------------------
# Convert OrderDate from TEXT to a real datetime. This unlocks time-based
# analysis (sorting by date, extracting month, etc.).
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print("\n6.3  Dtypes after conversion:")
print(df.dtypes)   # OrderDate should now be datetime64[ns]

# ------------------------------------------------------------------------------
# 6.4  TEXT STANDARDIZATION
# ------------------------------------------------------------------------------
# .str.strip() removes stray spaces; .str.title() gives consistent Capitalized
# casing. This unifies "mumbai"/"Mumbai" and "delhi"/"Delhi" into one value
# each, so counts and groupings are correct.
df["Customer"] = df["Customer"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
print("\n6.4  City counts after standardizing:")
print(df["City"].value_counts())   # Expect Pune 3, Mumbai 2, Delhi 2

# ------------------------------------------------------------------------------
# 6.5  DATA VALIDATION — FIX THE INVALID QUANTITY
# ------------------------------------------------------------------------------
# Quantity cannot be negative. We treat -2 as an error and replace it with the
# MEDIAN of the VALID (positive) quantities. We use the median because it is
# robust and not distorted by extremes.
median_qty = df.loc[df["Quantity"] > 0, "Quantity"].median()
# Cast to float first: the median can be a decimal (here 2.5), and newer pandas
# refuses to place a float into an int column.
df["Quantity"] = df["Quantity"].astype(float)
df.loc[df["Quantity"] < 0, "Quantity"] = median_qty
print("\n6.5  Quantity after fixing the invalid -2:")
print(df[["OrderID", "Quantity"]])

# ------------------------------------------------------------------------------
# 6.6  HANDLE THE OUTLIER AND MISSING VALUE
# ------------------------------------------------------------------------------
# NEVER delete an outlier blindly. First INSPECT it using the IQR rule:
#   IQR = Q3 - Q1 ; anything above Q3 + 1.5*IQR is flagged as an outlier.
print("\n6.6  Outlier check (IQR rule):")
Q1, Q3 = df["Amount"].quantile([0.25, 0.75])
IQR = Q3 - Q1
upper = Q3 + 1.5 * IQR
print(df[df["Amount"] > upper][["OrderID", "Amount"]])

# 999999 is clearly a data-entry typo (no order here is a million rupees).
# We treat it as MISSING, then fill BOTH missing amounts (this one + the
# original Clothing NaN) with the MEDIAN (robust to outliers — Day 6).
df.loc[df["Amount"] > upper, "Amount"] = np.nan
df["Amount"] = df["Amount"].fillna(df["Amount"].median())
print("\nAmount after handling outlier + missing:")
print(df[["OrderID", "Amount"]])

# ------------------------------------------------------------------------------
# 6.7  CLEANING SUMMARY
# ------------------------------------------------------------------------------
print("\n6.7  CLEANING SUMMARY")
print("""
Issue found                  -> Fix applied
-----------------------------------------------------------
1 duplicate (OrderID 1003)   -> drop_duplicates(subset=['OrderID'])
Date stored as text          -> pd.to_datetime()
Inconsistent text case       -> .str.strip().str.title()
Invalid quantity (-2)        -> replaced with median
Outlier amount (999999)      -> treated as error -> filled with median
Missing amount (row 1002)    -> filled with median
""")
print("Final clean data:")
print(df)

# Final sanity check: no missing values, no duplicates left.
assert df.isnull().sum().sum() == 0, "There should be no missing values left!"
assert df.duplicated(subset=["OrderID"]).sum() == 0, "No duplicate OrderIDs!"
print("\nValidation passed: 0 missing, 0 duplicates. Dataset is clean.")
