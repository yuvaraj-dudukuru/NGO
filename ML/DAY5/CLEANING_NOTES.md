# Cleaning Notes — ShopVerse Orders

A record of every data-quality issue found in the raw export and exactly how it
was fixed. This is the documentation a real analyst hands over with a cleaned
dataset.

## Data-Quality Summary (before → after)

**Before:** 7 rows. The export had a duplicate order, two columns stored with
the wrong type (`Amount` as text, `OrderDate` as text), two missing values
(one `Amount`, one `Quantity`), one invalid negative amount, and inconsistent
text (mixed case and stray spaces) in `Customer` and `City`.

**After:** 5 rows. Zero missing values, zero duplicate orders, correct data
types, validated non-negative amounts, and consistent title-cased text — a
dataset that can be trusted for reporting.

---

## Issue-by-Issue Log

### 1. Duplicate order
- **Found:** `OrderID` 1003 appears twice (rows 2 and 3).
- **Fix:** `drop_duplicates(subset=["OrderID"])` — keeps the first occurrence.
- **Why `subset`:** `OrderID` is the true unique key; this avoids deleting
  genuinely distinct orders that happen to share other field values.

### 2. Wrong data type — Amount
- **Found:** `Amount` is `object` (text) because values are quoted strings
  (`"500"`), so arithmetic and aggregation would fail.
- **Fix:** `pd.to_numeric(df["Amount"], errors="coerce")`.
- **Why `coerce`:** any unparseable value becomes `NaN` instead of crashing,
  and is then handled by the missing-value step.

### 3. Wrong data type — OrderDate
- **Found:** `OrderDate` is text, so it cannot be sorted chronologically or used
  for date math.
- **Fix:** `pd.to_datetime(df["OrderDate"], errors="coerce")`.

### 4. Invalid value — negative Amount
- **Found:** row with `Amount = -200`; an order amount cannot be negative.
- **Fix:** removed via the validation filter `Amount >= 0`.
- **Order matters:** this runs **before** imputation so the bad value does not
  pull down the median used to fill missing amounts.

### 5. Missing values
- **Found:** one missing `Amount` and one missing `Quantity`.
- **Fix:** filled each with its **column median**.
- **Why median:** robust to outliers, so a single large order cannot distort the
  imputed value.

### 6. Inconsistent text — Customer & City
- **Found:** mixed case (`"RAVI"`, `"imran "`, `"mumbai"` vs `"Mumbai"`) and
  leading/trailing spaces.
- **Fix:** `str.strip().str.title()` on both columns.
- **Result:** cities collapse to `Pune`, `Mumbai`, `Delhi`; names become
  `Asha`, `Ravi`, etc. Grouping and counting are now correct.

---

## Validation Checks (all must pass)

- `df.isnull().sum().sum() == 0` — no missing values
- `df.duplicated(subset=["OrderID"]).sum() == 0` — no duplicate orders
- `(df["Amount"] < 0).sum() == 0` — no invalid amounts
- `Amount` is numeric, `OrderDate` is `datetime64`

## Stretch Work

- Added `Total = Amount × Quantity`.
- IQR outlier check on `Amount` (1.5 × IQR rule) — no outliers in the clean set.
