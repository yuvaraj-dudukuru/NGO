# Feature Engineering Case Study 1 — Retail

**Goal:** Transform a raw retail sales table into a dashboard-ready dataset.

## Overview

Starting from just 6 raw columns (`OrderID`, `OrderDate`, `Category`, `Units`,
`UnitPrice`, `UnitCost`), we engineer **7 new features** that make the data
ready for charting and analysis.

| Feature | How it's built | Why it matters |
|---|---|---|
| `Revenue` | `Units * UnitPrice` | Top-line sales per order |
| `Cost` | `Units * UnitCost` | Total cost per order |
| `Profit` | `Revenue - Cost` | Money actually earned |
| `ProfitMargin%` | `Profit / Revenue * 100` | Profitability ratio |
| `Month` | `OrderDate.dt.month_name()` | Enables time-series charts |
| `OrderSize` | `pd.cut` on `Revenue` (Small/Medium/Large) | Order-size segmentation |
| `HighMargin` | flag where `ProfitMargin% >= 25` | Quick filtering |

## How to run

```bash
python retail_feature_engineering.py
```

Requires `pandas` and `numpy`:

```bash
pip install pandas numpy
```

## Expected output

```
   OrderID     Category  Revenue  Profit  ProfitMargin%     Month OrderSize HighMargin
0        1  Electronics    60000   16000           26.7   January     Large        Yes
1        2      Grocery     2000     500           25.0  February     Small        Yes
2        3  Electronics    60000   15000           25.0     March     Large        Yes
3        4     Clothing     7500    3000           40.0     April    Medium        Yes
4        5      Grocery     2000     560           28.0       May     Small        Yes

Category
Electronics    31000
Clothing        3000
Grocery         1060
Name: Profit, dtype: int64
```

## Insight

**Electronics drives the most profit.** This analysis was only possible after
engineering the `Profit` feature — proving the value of transformation. From the
transformed dataset you can chart profit by month, margin by category,
order-size distribution, and more.

> Note: All names and values in this case study are fictional sample data used
> for demonstration only.
