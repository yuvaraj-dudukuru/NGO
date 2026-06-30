# Capstone Mini Project — UrbanGrocer Business Analysis

An independent, end-to-end business analysis for **UrbanGrocer**, a fictional online grocery and
household-goods retailer. It designs and populates a relational database in **SQLite**, answers a set
of business questions with analytical **SQL**, and assembles the findings into a professional report
with a **Pandas + Seaborn** visualization.

All data is **synthetic sample data** created for this exercise — no real or personal information is
included.

## Contents

| File | Description |
| --- | --- |
| `UrbanGrocer_Capstone_Analysis.ipynb` | The notebook: schema, sample data, and all labelled queries (Q1–Q7) plus charts. |
| `Business_Report.md` | The written report (executive summary → recommendations → conclusion). |
| `README.md` | This file. |

## Requirements

- Python 3.9+
- `pandas`, `matplotlib`, `seaborn`
- `sqlite3` (Python standard library)

```bash
pip install pandas matplotlib seaborn jupyter
```

## How to run

```bash
jupyter notebook UrbanGrocer_Capstone_Analysis.ipynb
```

Run the cells top to bottom. The database is in-memory (`:memory:`), so nothing is written to disk
and the notebook is fully reproducible on every run.

## Database design

A five-table schema, deliberately seeded with edge cases so the analysis has something to find:

| Table | Notes |
| --- | --- |
| `Customers` (10)  | Premium / Regular segments; **one customer never orders** (inactive). |
| `Products` (14)   | 5 categories: Produce, Dairy & Eggs, Beverages, Household, Snacks. |
| `Orders` (16)     | **One cancelled order** (excluded from revenue). |
| `OrderItems` (40) | Line items (quantity × unit price). |
| `Payments` (14)   | **One missing payment** and **two discrepancies**. |

## Business questions answered (notebook labels Q1–Q7)

1. **Baseline KPIs** — total revenue, completed orders, active customers, average order value.
2. **Category analysis** — revenue, profit, and margin per category.
3. **Customer analysis** — top 5 customers, revenue by segment, inactive customers, repeat vs.
   one-time.
4. **Product analysis** — best sellers by units and by revenue.
5. **Geographic analysis** — revenue by state and city, with a `HAVING` threshold filter.
6. **Trend analysis** — monthly revenue.
7. **Data quality** — orders with missing payments and payment discrepancies.

## Method notes

- **Revenue counts completed orders only** — the cancelled order is excluded by business judgement.
- **Revenue vs. profit are kept distinct** — profit uses `unit_price − cost`, and margin = profit ÷
  revenue, so a high-revenue category is not assumed to be high-profit.
- **SQL → Pandas → Seaborn**: SQL aggregates inside the database; Pandas receives the summary; Seaborn
  renders the chart for the report.

## Headline result

₹11,430 revenue across 15 completed orders from 9 active customers (AOV ₹762), with ~80% of revenue
concentrated in Premium and repeat customers — and ~₹470 of unreconciled payments flagged for finance.
See `Business_Report.md` for the full findings and recommendations.
