# Phase 1 — Dataset Understanding

**Goal:** Understand the dataset *before* changing anything. You cannot fix problems you
have not found, so this phase is all about **looking carefully**.

## The Day 4 Inspection Trio

| Step | Tool | What it tells you |
|------|------|-------------------|
| First look | `df.head()` | What the rows actually look like |
| Structure | `df.shape`, `df.info()` | Size, column types, missing counts |
| Summary | `df.describe()` | Numeric range, averages, suspicious min/max |

## Run it

```bash
python phase1_dataset_understanding.py
```

## Expected output (key parts)

```
Shape: (8, 7)
...
 4   Amount     7 non-null      float64   <- 1 missing
 6   OrderDate  8 non-null      object    <- date stored as text
...
            Amount   Quantity
count     7.000000   8.000000
mean  152271.43...   1.875000
max   999999.000000  5.000000
min     1200.000000  -2.000000
```

## What to notice (the "red flags")

- **Amount max = 999999** — far above every other order → a likely **outlier**.
- **Quantity min = -2** — impossible, you cannot order negative items → **invalid value**.
- **Mean Amount ≈ 152,271** but typical orders are ₹1k–₹25k → the outlier is **distorting
  the average**.
- **OrderDate is `object`** (text), not a real date → needs conversion.
- **OrderID 1003** appears twice → a **duplicate**.
- **Customer / City** have mixed case (`mumbai` vs `Mumbai`) → needs standardizing.

## Phase 1 Conclusion

> The data is **dirty** and must be cleaned before any analysis. We do **not** fix anything
> here on purpose — spotting the mess is the whole skill. Fixing is **Phase 2**.
