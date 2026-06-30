# `data/` — Datasets for the Cleaning Project

This folder holds the input and output of the ShopVerse cleaning pipeline. Both
files are **generated** by [`../src/clean_orders.py`](../src/clean_orders.py) —
you do not need to create them by hand.

## Files

| File | Role | Created by |
|------|------|-----------|
| [`raw_orders.csv`](raw_orders.csv) | The **messy** export (7 rows) — duplicates, text amounts, a negative value, inconsistent casing, missing cells | written on each run from `make_raw_orders()` |
| [`clean_orders.csv`](clean_orders.csv) | The **cleaned** dataset — deduplicated, correct types, no missing values, standardized text, plus a `Total` column | written on each run by the `clean()` step |

## What the data looks like

`raw_orders.csv` (problems are intentional):

```
OrderID,Customer,City,Amount,Quantity,OrderDate
1001,  asha,pune,500,2.0,2026-05-01     ← leading spaces, lowercase city
1003,imran ,mumbai,750,3.0,2026-05-03   ← duplicated below
1003,imran ,mumbai,750,3.0,2026-05-03   ← duplicate row
1005,Divya,delhi,-200,1.0,2026-05-04    ← invalid negative Amount
1006,KARAN,Pune,,2.0,2026-05-05         ← missing Amount
1007,meena,DELHI,,2026-05-06            ← missing Quantity
```

`clean_orders.csv` (after the pipeline):

```
OrderID,Customer,City,Amount,Quantity,OrderDate,Total
1001,Asha,Pune,500.0,2,2026-05-01,1000.0
1002,Ravi,Mumbai,300.0,1,2026-05-02,300.0
...
```

> All names and values are **synthetic** sample data — no real personal data.

## How to (re)generate

```bash
# from the DAY_5/ folder
python src/clean_orders.py
```

This overwrites both CSV files. There is nothing to "run" or "stop" in this
folder itself — it only stores data.
