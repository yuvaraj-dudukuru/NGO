# `src/` — The Cleaning Pipeline

Source code for the **ShopVerse order-cleaning** project (see the
[Day 5 README](../README.md) for the full story).

## File

| File | Purpose |
|------|---------|
| [`clean_orders.py`](clean_orders.py) | The complete, runnable cleaning pipeline |

## What the script does

It runs four stages and is built from small, testable functions:

| Function | Stage | Responsibility |
|----------|-------|----------------|
| `make_raw_orders()` | — | Recreates the messy 7-row export **in code** (so no input file is required) |
| `inspect(df)` | 1. Inspect | Prints shape, dtypes, missing counts, duplicates, and inconsistent text |
| `clean(df)` | 2. Clean | Drops duplicates, fixes types, fills missing with the **median**, standardizes text, removes invalid (negative) amounts, adds `Total = Amount × Quantity` |
| `validate(df)` | 3. Validate | Asserts 0 missing, 0 duplicates, correct dtypes |
| (main block) | 4. Export | Writes `raw_orders.csv` and `clean_orders.csv` into [`../data/`](../data/) |

Paths are resolved relative to the file (`Path(__file__)`), so the script works
no matter which directory you launch it from.

## How to run

```bash
# from the DAY_5/ folder
python src/clean_orders.py
```

It prints each stage to the terminal and writes the two CSV files into
[`../data/`](../data/). It runs in well under a second and exits on its own.

## How to stop

It finishes by itself. To interrupt early, press **`Ctrl + C`**.

## Requirements

```bash
pip install pandas numpy        # or: pip install -r ../requirements.txt
```

> Tested by the suite in [`../tests/`](../tests/) — run `pytest` from `DAY_5/`.
