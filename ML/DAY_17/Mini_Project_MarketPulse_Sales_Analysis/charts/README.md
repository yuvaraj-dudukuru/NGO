# `charts/` — generated time-series figures

Chart images produced by
[`../marketpulse_sales_analysis.py`](../marketpulse_sales_analysis.py):

| File | Shows |
|------|-------|
| `daily_sales_trend.png` | The daily sales time series with its rolling trend |
| `yearly_monthly_comparison.png` | Month-by-month sales compared across years (seasonality) |

## How to (re)generate

```bash
cd ..
python marketpulse_sales_analysis.py
```

The script uses Matplotlib's `Agg` backend, so the PNGs are written **without
opening any windows**. Re-running overwrites them. Built from synthetic data.
