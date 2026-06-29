# `charts/` — Generated Figures (Advanced Drill)

Chart images for the **advanced** practice drill
([`../README.md`](../README.md)). These are **generated outputs** — produced by
[`../advanced_assessment.py`](../advanced_assessment.py).

## The Charts

| File | Chart type | Shows |
|------|-----------|-------|
| `01_revenue_by_category.png` | Bar | Total revenue by product category |
| `02_amount_distribution.png` | Histogram | Spread of order amounts |
| `03_amount_by_category_box.png` | Box plot | Amount per category (outliers) |
| `04_quantity_vs_amount.png` | Scatter | Quantity vs. amount relationship |
| `05_correlation_heatmap.png` | Heatmap | Correlation between numeric columns |

## How to (re)generate

This folder only stores images — nothing to run or stop here. Rebuild them from
the parent folder:

```bash
cd ..
python advanced_assessment.py
```

The script uses Matplotlib's `Agg` backend, so PNGs are saved **without opening
windows**. Re-running overwrites the files in place.

> All figures are built from **synthetic** sample data — no real personal data.
