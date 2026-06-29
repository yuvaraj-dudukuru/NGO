"""
================================================================================
PHASE 1 — DATASET UNDERSTANDING
================================================================================
Goal: Understand what we are holding BEFORE we touch it.

We apply the "Day 4 inspection trio":
    1. First look      -> df.head()
    2. Structure       -> df.shape, df.info()
    3. Summary stats   -> df.describe()

IMPORTANT: In Phase 1 we deliberately keep the data DIRTY. The whole point is to
SPOT the problems first. We do NOT fix anything here — fixing happens in Phase 2.
================================================================================
"""

import numpy as np
import pandas as pd

# ------------------------------------------------------------------------------
# 5.1  LOADING AND FIRST LOOK
# ------------------------------------------------------------------------------
# For a fully reproducible example we BUILD the dataset in code instead of
# reading a CSV. In a real project this line would be:
#     df = pd.read_csv("retailmart_sales.csv")
df = pd.DataFrame({
    "OrderID":   [1001, 1002, 1003, 1003, 1005, 1006, 1007, 1008],
    "Customer":  ["asha", "RAVI", "Imran", "Imran", "Sneha", "Karan", "Meena", "Tara"],
    "City":      ["Pune", "mumbai", "Pune", "Pune", "Delhi", "Mumbai", "delhi", "Pune"],
    "Category":  ["Electronics", "Clothing", "Electronics", "Electronics",
                  "Grocery", "Electronics", "Clothing", "Grocery"],
    # np.nan = a MISSING value (the Clothing order has no amount recorded)
    "Amount":    [25000, np.nan, 18000, 18000, 1200, 999999, 3200, 1500],
    # -2 is IMPOSSIBLE: you cannot order negative items
    "Quantity":  [2, 3, 1, 1, 5, 1, -2, 4],
    # Dates are stored as TEXT here, not real dates — note the quotes
    "OrderDate": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02",
                  "2026-05-03", "2026-05-03", "2026-05-04", "2026-05-05"],
})

print("=" * 60)
print("5.1  FIRST LOOK  (df.head)")
print("=" * 60)
# .head() shows the first 5 rows so we can eyeball the data quickly.
print(df.head())

# ------------------------------------------------------------------------------
# 5.2  INSPECTING STRUCTURE
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("5.2  STRUCTURE  (shape + info)")
print("=" * 60)
# .shape -> (rows, columns). Tells us the dataset size at a glance.
print("Shape:", df.shape)        # Expect (8, 7)
# .info() -> column names, non-null counts, and dtypes.
#   - "7 non-null" on Amount (out of 8) reveals 1 MISSING value.
#   - OrderDate dtype 'object' reveals the date is stored as TEXT, not a date.
df.info()

# ------------------------------------------------------------------------------
# 5.3  SUMMARY STATISTICS
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("5.3  SUMMARY STATISTICS  (describe)")
print("=" * 60)
# .describe() gives count/mean/std/min/quartiles/max for NUMERIC columns.
# Two RED FLAGS jump out:
#   - Amount max = 999999  -> far above everything else = likely OUTLIER.
#   - Quantity min = -2     -> impossible value = data error.
# The huge gap between mean Amount (~152,271) and typical values (~1k-25k)
# tells us the outlier is DISTORTING the average.
print(df.describe())

# ------------------------------------------------------------------------------
# 5.4  PHASE 1 CONCLUSIONS  (what we plan to fix in Phase 2)
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("5.4  PHASE 1 CONCLUSIONS")
print("=" * 60)
print("""
- Small dataset (8 rows) with a clear DUPLICATE (OrderID 1003 appears twice).
- Amount has 1 MISSING value and 1 extreme OUTLIER (999999).
- Quantity has an INVALID negative value (-2).
- Text columns (Customer, City) have INCONSISTENT capitalization.
- OrderDate needs CONVERSION from text to a real date.
=> The data is DIRTY and must be cleaned before any analysis (that is Phase 2).
""")
