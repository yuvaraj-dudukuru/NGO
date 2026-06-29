# `charts/` — Generated Figures (CityCab)

Chart images for the **CityCab** mini-challenge project
([`../README.md`](../README.md)). These are **generated outputs** — produced by
[`../build_citycab.py`](../build_citycab.py) (and the project notebook) at
**dpi=300**.

## The Charts

| File | Chart type | Shows |
|------|-----------|-------|
| `01_fare_by_city.png` | Bar | Total/average fare by city |
| `02_fare_distribution.png` | Histogram | Spread of ride fares |
| `03_fare_box.png` | Box plot | Fare distribution and outliers |
| `04_distance_vs_fare.png` | Scatter | Distance vs. fare (a strong **+0.93** correlation) |
| `05_correlation_heatmap.png` | Heatmap | Correlation between numeric columns |

## How to (re)generate

This folder only stores images — nothing to run or stop here. Rebuild them from
the parent folder:

```bash
cd ..
python build_citycab.py
```

The script uses Matplotlib's `Agg` backend, so PNGs are saved **without opening
windows**. Re-running overwrites the files in place.

> All figures are built from **synthetic** sample data — no real personal data.
