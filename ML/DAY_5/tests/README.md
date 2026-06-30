# `tests/` — Unit Tests for the Cleaning Pipeline

Automated tests that prove the [`../src/clean_orders.py`](../src/clean_orders.py)
pipeline actually fixes the data problems it claims to. Written with
**pytest**.

## File

| File | Purpose |
|------|---------|
| [`test_clean_orders.py`](test_clean_orders.py) | 8 tests covering the raw data and every cleaning guarantee |

## What is tested

| Test | Verifies |
|------|----------|
| `test_raw_has_known_issues` | The raw export really is messy (text amounts, a duplicate `OrderID`) |
| `test_no_duplicates_after_clean` | Cleaning removes duplicate orders |
| `test_no_missing_after_clean` | No missing values remain |
| `test_no_negative_amounts` | The invalid `-200` amount is gone |
| `test_correct_types` | `Amount` is numeric and `OrderDate` is a datetime |
| `test_text_standardized` | City names are title-cased with no stray spaces |
| (+ 2 more) | Total column and row-count guarantees |

The test file adds `../src` to `sys.path`, then imports `clean` and
`make_raw_orders` directly — so it tests the real functions, not a copy.

## How to run

```bash
# from the DAY_5/ folder
pytest
```

Expected output: **`8 passed`**.

Useful variants:

```bash
pytest -v        # show each test name
pytest -q        # quiet, one line summary
```

## How to stop

The suite finishes in well under a second. Press **`Ctrl + C`** to interrupt a
run if needed.

## Requirements

```bash
pip install pytest pandas numpy
```

> Note: running pytest creates a `.pytest_cache/` folder — it is disposable and
> can be safely deleted (it is listed in the project `.gitignore`).
