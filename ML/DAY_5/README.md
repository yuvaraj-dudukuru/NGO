# ShopVerse — Order Data Cleaning

> A junior-data-analyst mini project: take a raw, messy export of recent orders
> from the online retailer **ShopVerse** and clean it so it can be trusted for
> reporting.

This project demonstrates a complete, repeatable **data-cleaning workflow** with
pandas: inspect → find issues → clean → validate → export.

---

## The Problem

The operations team handed over a raw export of 7 orders. It looks small, but
it contains nearly every common data-quality issue:

| Issue | Where | Fix |
|-------|-------|-----|
| **Duplicate order** | `OrderID` 1003 appears twice | Drop duplicates on `OrderID` |
| **Wrong type** | `Amount` stored as text (`"500"`) | `pd.to_numeric(...)` |
| **Wrong type** | `OrderDate` stored as text | `pd.to_datetime(...)` |
| **Missing value** | one missing `Amount`, one missing `Quantity` | Fill with the **median** |
| **Invalid value** | a negative `Amount` of `-200` | Remove during validation |
| **Inconsistent text** | mixed case + stray spaces in `Customer` / `City` | `str.strip().str.title()` |

After cleaning: **~5 valid rows, zero missing values, zero duplicates, correct
types, and consistent text** — ready for reporting.

---

## Project Structure

```
shopverse-data-cleaning/
├── README.md              # this file
├── CLEANING_NOTES.md      # detailed issue-by-issue change log
├── requirements.txt       # dependencies (pandas, numpy)
├── .gitignore
├── src/
│   └── clean_orders.py    # the cleaning pipeline
├── tests/
│   └── test_clean_orders.py
└── data/                  # generated when you run the script
    ├── raw_orders.csv     # the original messy export
    └── clean_orders.csv   # the final clean dataset
```

---

## How to Run

```bash
# 1. (optional) create a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 2. install dependencies
pip install -r requirements.txt

# 3. run the pipeline
python src/clean_orders.py
```

The script prints each stage (inspect → clean → validate) and writes
`data/clean_orders.csv`.

### Run the tests

```bash
pip install pytest
pytest
```

---

## The Cleaning Workflow

The standard professional order, applied here:

```
Raw data → Inspect → Find issues → Handle missing → Remove duplicates
        → Fix types → Standardize text → Validate → Clean dataset
```

> **Why median, not mean?** The median is robust to outliers, so a single
> extreme order amount cannot distort the value we impute.

> **Why validate the negative amount *before* imputing?** A negative value would
> drag down the median we fill with. We remove it first, then impute.

---

## Stretch Goals (included)

- **`Total = Amount × Quantity`** column added and exported.
- **IQR outlier check** on `Amount` (1.5 × IQR rule).
- **Data-quality summary** — see [CLEANING_NOTES.md](CLEANING_NOTES.md).

---

*Part of the Day 5 — Data Cleaning & Preprocessing lesson (Data Analytics track).*
