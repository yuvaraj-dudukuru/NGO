# Feature Engineering Case Study 2 — Customer Analytics

**Goal:** Create advanced analytical features for customer segmentation.

## Overview

From a plain order log we aggregate to a **per-customer** table built around the
classic **RFM** model (Recency, Frequency, Monetary), plus a loyalty segment.

| Feature | How it's built | RFM role |
|---|---|---|
| `TotalSpend` | sum of `Amount` per customer | **Monetary** |
| `Frequency` | count of orders per customer | **Frequency** |
| `AvgOrder` | mean `Amount` per customer | Order value |
| `LastPurchase` | max `OrderDate` per customer | — |
| `Recency` | days from `LastPurchase` to "today" | **Recency** |
| `Segment` | `pd.cut` on `TotalSpend` (Bronze/Silver/Gold) | Loyalty tier |

Reference date used for recency: **2026-06-18**.

## How to run

```bash
python customer_analytics_feature_engineering.py
```

Requires `pandas`:

```bash
pip install pandas
```

## Expected output

```
  Customer  TotalSpend  Frequency  AvgOrder LastPurchase  Recency Segment
0     Asha       67000          3   22333.0   2026-05-25       24    Gold
1    Divya       45000          1   45000.0   2026-06-10        8    Gold
2    Imran        8000          1    8000.0   2026-04-20       59  Bronze
3     Ravi        3500          2    1750.0   2026-06-01       17  Bronze
```

## Insight

Asha and Divya are **Gold** customers (high value); Imran is a **Bronze**
customer who hasn't purchased in **59 days** (churn risk). These engineered
features enable precise, targeted marketing — impossible from the raw order list.

> Note: All names and values in this case study are fictional sample data used
> for demonstration only.
