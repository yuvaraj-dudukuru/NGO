# FreshBasket — Day 10 Assessment Project

> **The main deliverable for Day 10.** A complete, end-to-end analysis of a messy sales export
> for *FreshBasket* (online grocery + electronics retailer), applying everything from Days 1–9:
> **Load → Clean → Explore → Visualize → SQL → Insights → Report.**

This is your **first portfolio project** — concrete proof you can take raw data and deliver
business value end to end.

---

## The Brief

You are a junior data analyst. Management hands you a messy 10-row sales export and asks:
*Which cities and categories drive revenue? Who are our top customers? Is anything unusual?*

---

## The Five Submission Deliverables

| # | Deliverable | File / Folder | Status |
|---|-------------|---------------|--------|
| 1 | **Clean dataset** | [`freshbasket_clean.csv`](freshbasket_clean.csv) | ✅ generated |
| 2 | **Jupyter notebook** | [`freshbasket_analysis.ipynb`](freshbasket_analysis.ipynb) | ✅ all 7 steps, Markdown + code |
| 3 | **EDA report** (8 sections) | [`EDA_REPORT.md`](EDA_REPORT.md) | ✅ business language + recommendations |
| 4 | **SQL queries** (labelled) | [`sql_queries.sql`](sql_queries.sql) | ✅ each tagged with its business question |
| 5 | **Saved visualizations** (dpi=300) | [`charts/`](charts/) | ✅ 6 PNG charts |

There is also a **`build_freshbasket.py`** — a single script that reproduces the whole pipeline
(deliverables 1 and 5) so you can regenerate the CSV and charts with one command.

---

## How to run

```bash
pip install pandas numpy matplotlib seaborn      # sqlite3 ships with Python

# Option A — one-shot script (regenerates the CSV + all charts)
python build_freshbasket.py

# Option B — the notebook (the graded deliverable)
jupyter notebook freshbasket_analysis.ipynb
# then: Kernel -> Restart & Run All
```

---

## What the data showed (headline results)

- **Electronics drives revenue:** ₹135,000 vs Grocery ₹9,100 and Clothing ₹5,700 (~90% of total).
- **Top city depends on the metric:** **Pune** leads *revenue* (₹135,000); **Mumbai** leads
  *order count* (4 orders).
- **Negative correlation (−0.62)** between Quantity and Amount — bulk Grocery vs single-unit
  Electronics: two different buying patterns.
- **High-value customers** (all Pune, all Electronics): Sahil ₹52k, Ravi ₹45k, Imran ₹38k.

## The six data-quality issues fixed (Step 2)

1. Duplicate order (OrderID 203) → dropped on the business key.
2. OrderDate text → real datetime.
3. Messy text (`"  ravi"`, `"ASHA"`, `"meena "`, `"mumbai"`) → stripped + Title case.
4. Invalid quantity (−3) → median of valid quantities.
5. Outlier amount (₹999,999) → flagged by IQR → treated as error → median fill.
6. Missing amount (OrderID 205) → median fill.

Final clean dataset: **9 unique orders, 0 missing, 0 duplicates, correct types, all valid.**
