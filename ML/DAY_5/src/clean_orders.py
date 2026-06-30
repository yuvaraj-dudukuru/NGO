"""
ShopVerse — Order Data Cleaning
================================

A junior-data-analyst task: take a raw, messy export of recent orders and
clean it so it can be trusted for reporting.

Pipeline (see README and CLEANING_NOTES.md for the full write-up):
    1. Inspect      -> find every data-quality issue
    2. Clean        -> duplicates, types, missing values, text, invalid values
    3. Validate     -> verify 0 missing, 0 duplicates, correct types
    4. Export       -> clean_orders.csv

Run:
    python src/clean_orders.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

# Project root = one level above this file's folder (src/)
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)


def make_raw_orders() -> pd.DataFrame:
    """Recreate the messy export exactly as handed over by the ops team."""
    return pd.DataFrame(
        {
            "OrderID": [1001, 1002, 1003, 1003, 1005, 1006, 1007],
            "Customer": ["  asha", "RAVI", "imran ", "imran ", "Divya", "KARAN", "meena"],
            "City": ["pune", "Mumbai", "mumbai", "mumbai", "delhi", "Pune", "DELHI"],
            "Amount": ["500", "300", "750", "750", "-200", np.nan, "650"],
            "Quantity": [2, 1, 3, 3, 1, 2, np.nan],
            "OrderDate": [
                "2026-05-01", "2026-05-02", "2026-05-03", "2026-05-03",
                "2026-05-04", "2026-05-05", "2026-05-06",
            ],
        }
    )


def inspect(df: pd.DataFrame) -> None:
    """Step 1 — surface every data-quality issue."""
    print("=" * 60)
    print("STEP 1: INSPECT THE RAW DATA")
    print("=" * 60)
    print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns\n")
    print("Data types:")
    print(df.dtypes)
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print(f"\nFully-duplicated rows: {df.duplicated().sum()}")
    print(f"Duplicate OrderIDs:    {df.duplicated(subset=['OrderID']).sum()}")
    print("\nCity values (note the inconsistent casing):")
    print(df["City"].value_counts())
    print("\nRaw data:")
    print(df)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Step 2 — fix every issue found during inspection."""
    print("\n" + "=" * 60)
    print("STEP 2: CLEAN THE DATA")
    print("=" * 60)

    df = df.copy()

    # 2a. Remove duplicate orders (OrderID is the unique key)
    df = df.drop_duplicates(subset=["OrderID"]).reset_index(drop=True)
    print(f"- Dropped duplicate OrderIDs -> {len(df)} rows remain")

    # 2b. Fix data types (errors='coerce' turns junk into NaN safely)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    print("- Converted Amount -> numeric, OrderDate -> datetime")

    # 2c. Validate invalid values BEFORE imputing
    #     A negative Amount is impossible; drop those rows so the bad value
    #     does not pollute the median used for imputation.
    before = len(df)
    df = df[(df["Amount"].isna()) | (df["Amount"] >= 0)].reset_index(drop=True)
    print(f"- Removed {before - len(df)} row(s) with a negative Amount")

    # 2d. Handle missing values with the median (robust to outliers)
    df["Amount"] = df["Amount"].fillna(df["Amount"].median())
    df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
    print("- Filled missing Amount and Quantity with the column median")

    # 2e. Standardize text: strip spaces, unify capitalization
    df["Customer"] = df["Customer"].str.strip().str.title()
    df["City"] = df["City"].str.strip().str.title()
    print("- Standardized Customer and City text (strip + title case)")

    # 2f. Tidy types: Quantity is a whole number
    df["Quantity"] = df["Quantity"].astype(int)

    # Stretch goal: a validated Total column
    df["Total"] = df["Amount"] * df["Quantity"]

    return df


def validate(df: pd.DataFrame) -> None:
    """Step 3 — confirm the dataset is now trustworthy."""
    print("\n" + "=" * 60)
    print("STEP 3: VALIDATE THE CLEAN DATA")
    print("=" * 60)

    missing = int(df.isnull().sum().sum())
    dupes = int(df.duplicated(subset=["OrderID"]).sum())
    negatives = int((df["Amount"] < 0).sum())

    print(f"Missing values remaining:    {missing}")
    print(f"Duplicate OrderIDs remaining: {dupes}")
    print(f"Negative amounts remaining:  {negatives}")
    print("\nFinal data types:")
    print(df.dtypes)

    assert missing == 0, "Validation failed: missing values remain"
    assert dupes == 0, "Validation failed: duplicate OrderIDs remain"
    assert negatives == 0, "Validation failed: negative amounts remain"
    print("\nAll validation checks passed.")


def iqr_outlier_check(df: pd.DataFrame, column: str = "Amount") -> None:
    """Stretch goal — flag outliers in `column` using the 1.5 x IQR rule."""
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = df[(df[column] < lower) | (df[column] > upper)]
    print("\n" + "=" * 60)
    print(f"STRETCH GOAL: IQR OUTLIER CHECK ON '{column}'")
    print("=" * 60)
    print(f"Bounds: [{lower:.1f}, {upper:.1f}]")
    if outliers.empty:
        print("No outliers detected.")
    else:
        print("Outliers detected:")
        print(outliers)


def main() -> None:
    raw = make_raw_orders()

    # Save the raw export for reference/reproducibility
    raw.to_csv(DATA_DIR / "raw_orders.csv", index=False)

    inspect(raw)
    clean_df = clean(raw)
    validate(clean_df)
    iqr_outlier_check(clean_df, "Amount")

    out_path = DATA_DIR / "clean_orders.csv"
    clean_df.to_csv(out_path, index=False)

    print("\n" + "=" * 60)
    print("STEP 4: EXPORT")
    print("=" * 60)
    print(f"Clean dataset ({len(clean_df)} rows) written to: {out_path}")
    print("\nFinal clean dataset:")
    print(clean_df)


if __name__ == "__main__":
    main()
