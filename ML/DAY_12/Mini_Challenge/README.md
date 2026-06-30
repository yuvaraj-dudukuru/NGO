# Mini Challenge — MartPro Retail Feature Engineering

## Problem statement

You are a data analyst at **"MartPro"**, a retail chain. You are given a raw,
messy sales export and asked to transform it into a **dashboard-ready analytical
dataset** with engineered features and KPIs, then summarize the insights.

## File

- [`martpro_mini_challenge.py`](martpro_mini_challenge.py) — full sample solution.

## Requirements (what the solution does)

| # | Requirement | Features / output |
|---|---|---|
| 1 | Transform columns | `Customer` → Title Case (trimmed); `OrderDate` → datetime |
| 2 | Derived metrics | `Revenue`, `Cost`, `Profit`, `Margin%` |
| 3 | Date features | `Month`, `Quarter` |
| 4 | Text features | `FirstName`, `EmailDomain`, `CustomerType` (Corporate/Personal) |
| 5 | Categories | `OrderSize` (Small/Medium/Large via `pd.cut`), `HighMargin` (via `np.where`) |
| 6 | Aggregated KPIs | `TotalSpend`, `OrderCount` (via `groupby().transform`) |
| 7 | Validate | no missing values, no negative profit, margins within 0–100% |
| 8 | Summarize | profit by category, top customer, corporate vs personal revenue, recommendations |

The solution also includes two **stretch goals**: average margin per customer,
and a structured set of recommendations.

## How to run

```bash
pip install pandas numpy
python martpro_mini_challenge.py
```

## Expected validation output

```
Missing values: 0
Negative profit rows: 0
Margin out of range: 0
All validation checks passed.
```

## Key insights revealed

- **Electronics** is by far the most profitable category, driven by high-value
  laptop orders.
- **Asha Sharma** is the top customer (multiple Electronics orders, highest
  `TotalSpend`).
- **Corporate** (company.com) vs **Personal** customers can be compared by
  revenue — useful for B2B vs B2C strategy.
- Most high-value orders are **Large** and **HighMargin Electronics**.

## Recommendations

1. Prioritize Electronics inventory.
2. Nurture top customers like Asha with loyalty offers.
3. Develop targeted strategies for the corporate vs personal segments.
4. Promote high-margin products.

## Stretch goals (optional, not required)

- Add a Seaborn bar chart of profit by category.
- Compute each customer's average margin (included in the solution).
- Write a full EDA-style report of the transformed dataset.

> Note: All names, emails, and values in this challenge are fictional sample data
> used purely for demonstration.
