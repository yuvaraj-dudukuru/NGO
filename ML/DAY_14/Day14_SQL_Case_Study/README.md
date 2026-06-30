# Day 14 — SQL Case Study: Business Analysis

A hands-on activity that reproduces a complete, multi-phase retail business analysis entirely in
**SQLite** through Python, then integrates the results with **Pandas** and **Seaborn**. It ties
together the SQL, Pandas, and visualization skills from earlier lessons (Days 7, 8, and 13).

All data used here is **synthetic sample data** created for the exercise — no real or personal
information is included.

## Contents

| File | Description |
| --- | --- |
| `Day14_SQL_Case_Study.ipynb` | The complete Jupyter notebook (schema, data, queries, charts). |
| `README.md` | This file. |

## Requirements

- Python 3.9+
- `pandas`, `matplotlib`, `seaborn`
- `sqlite3` (bundled with the Python standard library)

Install the third-party packages if needed:

```bash
pip install pandas matplotlib seaborn jupyter
```

## How to run

```bash
jupyter notebook Day14_SQL_Case_Study.ipynb
```

Then run the cells top to bottom. The database lives in memory (`:memory:`), so nothing is written
to disk and the notebook is fully reproducible on every run.

## What the notebook does

**Step 1 — Create and populate the database**
Builds a five-table schema and loads the sample data.

| Table | Purpose |
| --- | --- |
| `Customers`  | Customer profile, location, and segment. |
| `Products`   | Catalog with price and cost. |
| `Orders`     | Order header with status and date. |
| `OrderItems` | Line items linking orders to products. |
| `Payments`   | Recorded payments per order. |

**Step 2 — Run the analysis queries**
Executes each analytical query and returns the result as a DataFrame:

- Baseline KPIs — completed orders, active customers, total revenue
- Profit by category
- Top customers by revenue
- Revenue by customer segment
- Inactive customers (no completed orders)
- Revenue by geography (state / city)
- Monthly revenue trend
- Payment reconciliation (order value vs. amount paid)

**Step 3 — Combine SQL with Pandas and visualization**
Pulls an aggregated SQL result into Pandas and visualizes it with Seaborn (revenue by category bar
chart and a monthly revenue trend line chart).

**Step 4 — Close the connection**
Releases the database connection.

## The professional workflow it demonstrates

SQL aggregates the data inside the database → Pandas receives the summarized result → Seaborn
visualizes it for the report. This is the standard division of labor in a real analytics pipeline:
push heavy aggregation down to the database and use Python only for the final shaping and
presentation.
