# Day 14 — SQL Case Study & Business Analysis

This folder contains the Day 14 work on **analytical SQL for business analysis** — taking a
transactional database, translating business questions into SQL, separating revenue from profit,
excluding invalid records by business judgement, detecting data-quality issues, and presenting the
findings with Pandas + Seaborn.

There are two projects: a **guided hands-on activity** and an **independent capstone** that applies
the same workflow to a new dataset.

All data in both projects is **synthetic sample data** created for these exercises — no real or
personal information is included.

## Projects

| Folder | What it is |
| --- | --- |
| [`Day14_SQL_Case_Study/`](Day14_SQL_Case_Study/) | **Guided hands-on activity** — reproduces the TechCart case study end-to-end in SQLite (schema, sample data, analytical queries, and a Seaborn chart). |
| [`UrbanGrocer_Capstone/`](UrbanGrocer_Capstone/) | **Capstone mini project** — an independent business analysis for UrbanGrocer (online grocery retailer): a self-designed schema, seven labelled business questions, a full written report, and visualizations. |

### `Day14_SQL_Case_Study/` — TechCart hands-on activity
- `Day14_SQL_Case_Study.ipynb` — five-table schema, sample data, and the analysis queries (KPIs,
  profit by category, top customers, segments, inactive customers, geography, monthly trend, payment
  reconciliation), plus a revenue-by-category chart.
- `README.md` — how to run and what each step does.

### `UrbanGrocer_Capstone/` — capstone mini project
- `UrbanGrocer_Capstone_Analysis.ipynb` — self-designed 5-table schema (10 customers, 14 products
  across 5 categories, 16 orders, 40 line items, 14 payments) with all queries labelled by business
  question Q1–Q7, plus charts.
- `Business_Report.md` — the written report: executive summary, business problem, data description,
  key findings, recommendations, conclusion.
- `README.md` — project overview and method notes.

## The workflow both projects demonstrate

1. **Design & populate** a relational schema in SQLite.
2. **Query** business questions in analytical SQL — KPIs, category economics, customer/product/
   geographic analysis, trends, and data-quality checks.
3. **Apply business judgement** — count only completed orders; keep revenue and profit distinct.
4. **Visualize** — aggregate in SQL, hand the summary to Pandas, chart it with Seaborn.
5. **Report** — turn the numbers into findings and actionable recommendations.

## Requirements

- Python 3.9+
- `pandas`, `matplotlib`, `seaborn`
- `sqlite3` (Python standard library)

```bash
pip install pandas matplotlib seaborn jupyter
```

## How to run

Open either notebook and run the cells top to bottom:

```bash
jupyter notebook Day14_SQL_Case_Study/Day14_SQL_Case_Study.ipynb
jupyter notebook UrbanGrocer_Capstone/UrbanGrocer_Capstone_Analysis.ipynb
```

Each notebook uses an in-memory database (`:memory:`), so nothing is written to disk and results are
fully reproducible on every run.
