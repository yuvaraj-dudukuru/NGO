# 🔴 Advanced Assessment

**Task:** Complete a **mini end-to-end project** on a messy 12-row sales dataset.

1. **Clean** fully (missing, duplicates, types, text, invalid values, outliers).
2. **EDA** (statistics, `groupby()` by city and category, correlation).
3. **Four+ visualizations** (bar, histogram, box, scatter/heatmap).
4. **SQLite** + three business queries.
5. **Insight ladder** for three findings.
6. **Complete EDA report.**

> **Solution outline (from the brief):** *Follow the seven phases exactly as in the worked
> RetailMart example.* This folder does precisely that.

## Run

```bash
python advanced_assessment.py
```

## Deliverables produced

| Deliverable | File |
|-------------|------|
| Clean dataset | [`sales_clean.csv`](sales_clean.csv) |
| 5 charts (dpi=300) | [`charts/`](charts/) |
| Full written report | [`EDA_REPORT.md`](EDA_REPORT.md) |
| SQL + insights | printed by the script (see Phase 4 & 5 output) |

## Headline results (verified output)

- **Electronics ₹165,500** vs Clothing ₹10,400 vs Grocery ₹8,600 (~90% of revenue).
- **Pune ₹163,700** — dominant revenue city (all big Electronics orders).
- **Correlation −0.64** (Quantity vs Amount): two buying patterns.
- **High-value buyers:** Neha ₹60k, Tina ₹55k, Amit ₹47k (all Electronics).

## The six planted data-quality issues

1. Duplicate (OrderID 404) · 2. OrderDate text · 3. Messy text/case ·
4. Invalid quantity (−4) · 5. Outlier amount (₹888,888) · 6. Missing amount (OrderID 409).

Final clean dataset: **11 unique orders, 0 missing, 0 duplicates, all valid.**

> This mirrors the FreshBasket project structure — use it as a second rep before building your
> own portfolio piece.
