# CityCab — Mini Project Challenge

> **Your second portfolio project.** A complete, end-to-end analysis of a messy ride export for
> *CityCab*, a ride-hailing company. Applies the full Day 1–9 workflow:
> **Inspect → Clean → Explore → Visualize → SQL → Insights → Report.**

## The Brief

You are the **lead junior analyst**. Management hands you a messy 10-row ride export and asks for
a complete analysis to **improve operations**: which city earns most, how fare relates to
distance, and whether the data is trustworthy.

---

## The Five Deliverables

| # | Deliverable | File / Folder |
|---|-------------|---------------|
| 1 | **Clean dataset** | [`citycab_clean.csv`](citycab_clean.csv) |
| 2 | **Jupyter notebook** | [`citycab_analysis.ipynb`](citycab_analysis.ipynb) |
| 3 | **Saved charts** (dpi=300) | [`charts/`](charts/) — 5 PNGs |
| 4 | **SQL queries** (labelled) | [`sql_queries.sql`](sql_queries.sql) |
| 5 | **EDA report** (8 sections) | [`EDA_REPORT.md`](EDA_REPORT.md) |

Plus **`build_citycab.py`** — one script that reproduces deliverables 1 and 3.

---

## How to run

```bash
pip install pandas numpy matplotlib seaborn      # sqlite3 ships with Python

# Option A — one-shot script (regenerates the CSV + charts)
python build_citycab.py

# Option B — the notebook (the graded deliverable)
jupyter notebook citycab_analysis.ipynb          # then Restart & Run All
```

---

## Headline results (verified output)

- **9 valid rides** across 3 cities after cleaning (1 duplicate removed).
- **Mumbai is the top-fare market (₹680)**, just ahead of **Pune (₹660)**; Delhi ₹310.
- **Distance ↔ Fare correlation = +0.93** — a strong positive relationship: **longer rides cost
  more** (intuitively causal, but still a correlation, not proof).
- Average ride: **₹183 fare, 7.4 km**.
- Two impossible values (**200 km**, **₹5,000**) were data-entry errors, now corrected.

## The data-quality issues fixed (Step 2)

1. Duplicate ride (RideID 3) — deduped on the business key.
2. Missing fare (RideID 3) — median fill.
3. Messy text (`"  ravi"`, `"ASHA"`, `"meena "`, `"mumbai"`) — strip + Title case.
4. Invalid distance (−4.0 km) — median of valid distances.
5. Outlier distance (200 km) — IQR-flagged → median fill.
6. Outlier fare (₹5,000) — IQR-flagged → median fill.
7. RideDate text → datetime.

> **Why the duplicate is tricky:** the two copies of RideID 3 differ (one fare is missing), so a
> full-row `duplicated()` check misses it. Always dedupe on the **business key** (`RideID`), then
> handle the leftover missing value.

## Recommendations (from the report)

1. **Allocate more drivers to Mumbai & Pune** — they generate almost all the fare.
2. **Add input validation** — range checks would block the 200 km / −4 km / ₹5,000 errors.
3. **Use the distance–fare line (+0.93) as a pricing sanity check** to flag off-trend rides.
