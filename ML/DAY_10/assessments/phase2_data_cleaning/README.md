# Phase 2 — Data Cleaning

**Goal:** Turn the messy Phase 1 data into a **trustworthy** dataset. This is where you apply
*every* Day 5 technique as one connected workflow — not isolated commands.

## The Day 5 Cleaning Workflow (order matters!)

```
detect → handle missing → remove duplicates → fix types
       → standardize text → validate values → handle outliers
```

> **Why order matters:** we remove duplicates *before* computing medians, so duplicated rows
> don't skew the fill values. We inspect outliers *before* deleting anything.

## Run it

```bash
python phase2_data_cleaning.py
```

## The six fixes

| # | Issue found | Fix applied |
|---|-------------|-------------|
| 1 | Duplicate (OrderID 1003) | `drop_duplicates(subset=["OrderID"])` |
| 2 | Date stored as text | `pd.to_datetime()` |
| 3 | Inconsistent text case | `.str.strip().str.title()` |
| 4 | Invalid quantity (-2) | replace with **median** of valid quantities |
| 5 | Outlier amount (999999) | inspect with **IQR** → treat as error → fill with median |
| 6 | Missing amount (row 1002) | fill with **median** |

## Key ideas to internalize

- **Dedupe on the business key** (`OrderID`), not the whole row.
- **Median, not mean**, for fills — the median is *robust to outliers*.
- **Never delete an outlier blindly.** Inspect it first with the **IQR rule**:
  `upper = Q3 + 1.5 × (Q3 − Q1)`. Only then decide it's a typo.
- **Validate at the end:** the script `assert`s there are 0 missing values and 0 duplicate
  OrderIDs. If an assert fails, the cleaning was incomplete.

## Result

> A clean, validated dataset: **7 unique orders**, no missing values, consistent text, a real
> date column, and no impossible/extreme values. Ready for analysis in Phase 3.
