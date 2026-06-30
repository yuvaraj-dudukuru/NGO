# Day 11 — Advanced Pandas (GroupBy, Merge, Pivot & Multi-Table Analysis)

> **Summer Internship Program — Data Analytics Track**
> Skill Development Phase · Day 11

This folder is the complete Day 11 package: four runnable practice projects and a
capstone mini challenge. The theme is **advanced pandas** — the techniques used to
**summarize** (GroupBy + aggregations), **combine** (merge / join), and **reshape**
(pivot tables, crosstabs) real business data across multiple tables.

---

## What's in this folder

| Item | Type | What it covers |
|------|------|----------------|
| [`retail_sales_case_study/`](retail_sales_case_study/) | Case Study 1 | GroupBy, named aggregations, and pivot tables on retail sales |
| [`customer_analysis_case_study/`](customer_analysis_case_study/) | Case Study 2 | Merging two tables (joins) + segmentation analysis |
| [`employee_performance_case_study/`](employee_performance_case_study/) | Case Study 3 | Chained joins across three tables + a ranked KPI report |
| [`day11_advanced_pandas_activity/`](day11_advanced_pandas_activity/) | Hands-on activity | A 9-step end-to-end workflow (notebook + script) using the whole toolkit |
| [`shopverse_mini_challenge/`](shopverse_mini_challenge/) | Capstone | The ShopVerse challenge — every Day 11 technique on three tables at once |

Each subfolder has its own `README.md` with the data, the code, the verified output,
and business insights.

---

## Suggested learning path

1. **Work the case studies in order** — they build up one technique at a time:
   - Case Study 1 — *Retail Sales* → GroupBy & pivot on a single table.
   - Case Study 2 — *Customer Analysis* → merging two tables.
   - Case Study 3 — *Employee Performance* → joining three tables into a KPI report.
2. **Do the hands-on activity** — `day11_advanced_pandas_activity/` ties the whole
   toolkit together in 9 steps (available as both a notebook and a script).
3. **Attempt the mini challenge** — `shopverse_mini_challenge/` is the capstone; try it
   before reading the solution.

---

## Requirements

All projects run on:

- **Python 3.8+**
- **pandas**

The hands-on activity additionally offers a Jupyter notebook, and the mini challenge
has an optional Seaborn chart:

```bash
pip install pandas jupyter matplotlib seaborn
```

(`jupyter`, `matplotlib`, and `seaborn` are only needed for the notebook and the
optional chart — the core scripts need only `pandas`.)

---

## How to run

Each project is self-contained — the dataset is defined inside the script, so there are
no external data files to download. From any project folder:

```bash
cd retail_sales_case_study
python retail_sales_analysis.py
```

| Project | Command |
|---------|---------|
| Retail Sales | `python retail_sales_case_study/retail_sales_analysis.py` |
| Customer Analysis | `python customer_analysis_case_study/customer_analysis.py` |
| Employee Performance | `python employee_performance_case_study/employee_performance.py` |
| Hands-On Activity (script) | `python day11_advanced_pandas_activity/day11_advanced_pandas.py` |
| Hands-On Activity (notebook) | `jupyter notebook day11_advanced_pandas_activity/Day11_Advanced_Pandas.ipynb` |
| ShopVerse Mini Challenge | `python shopverse_mini_challenge/shopverse_analysis.py` |

---

## Concepts covered

| Technique | Where it appears |
|-----------|------------------|
| `groupby()` + single aggregation | Retail Sales, Activity, ShopVerse |
| Named multi-aggregations (`.agg(name=("col", "func"))`) | Retail Sales, Employee, Activity |
| `pd.merge()` two-table joins | Customer Analysis, Activity |
| Chained multi-table joins (3 tables) | Employee Performance, ShopVerse |
| Feature engineering (computed columns, e.g. `Revenue`) | ShopVerse |
| `pd.pivot_table()` with `fill_value` & `margins` | Retail Sales, Activity, ShopVerse |
| `pd.crosstab()` | Activity, ShopVerse |
| `idxmax()` to find a top performer | ShopVerse |
| KPI reports + `sort_values()` ranking | Employee, Activity, ShopVerse |
| Turning numbers into insights & recommendations | Every project |
| Visualization (Seaborn bar chart) | ShopVerse (stretch) |

---

## A note on verified outputs

The output blocks shown in each project's README are the **actual, verified results of
running the code** — not copied from the original briefs. Where a source brief
contained figures that didn't match its own dataset (e.g. mis-sorted rows or
mismatched pivot totals), the project README flags the discrepancy and shows the
correct, reproducible output. Re-run any script to confirm.
