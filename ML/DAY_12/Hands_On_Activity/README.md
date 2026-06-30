# Day 12 — Hands-On Activity: Feature Engineering

A step-by-step Jupyter notebook that transforms a raw, messy order table into a
rich, validated, **dashboard-ready** dataset.

## File

- [`Day12_Feature_Engineering.ipynb`](Day12_Feature_Engineering.ipynb) — the notebook to work through.

## What you'll build

Starting from 7 raw columns (`OrderID`, `Customer`, `OrderDate`, `Category`,
`Units`, `UnitPrice`, `UnitCost`), you engineer **10+ new features** across every
major technique:

| Step | Technique | Features created |
|---|---|---|
| 3 | Arithmetic | `Revenue`, `Cost`, `Profit`, `Margin%` |
| 4 | Date | `Month`, `Quarter` |
| 5 | String + category + conditional | `FirstName`, `OrderSize`, `HighValue` (and cleaned `Customer`) |
| 6 | Aggregated KPI | `CustomerTotal` |
| 7 | Validation | data-quality checks |
| 8 | Analysis | profit by category, order-size mix |

## How to run

```bash
pip install pandas numpy jupyter
jupyter notebook Day12_Feature_Engineering.ipynb
```

Then run the cells top to bottom (Shift + Enter), or **Run All**.

## Step-by-step

1. **Load** the raw dataset into a DataFrame.
2. **Identify** transformation opportunities.
3. **Arithmetic columns** — Revenue, Cost, Profit, Margin%.
4. **Date features** — Month name and Quarter from `OrderDate`.
5. **String/category features** — standardize `Customer`, extract `FirstName`,
   bin into `OrderSize`, flag `HighValue`.
6. **KPI/aggregated feature** — `CustomerTotal` via `groupby().transform("sum")`.
7. **Validate** — no missing values, no negative profit, margins in range.
8. **Analyze** — profit by category and orders by size.
9. **Document** findings in a Markdown cell.

## Expected validation output

```
Missing values: 0
Negative profit rows: 0
Margin out of range: 0
```

## Key findings

- **10+ engineered features** created from 7 raw columns.
- **Electronics drives the most profit.**
- The dataset is now dashboard-ready: chart profit by month/category, the
  order-size mix, and customer totals.

> Note: All names and values in this activity are fictional sample data used
> purely for demonstration.
