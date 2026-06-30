# Hands-On Activity — Day 17: Time Series Basics

> A single Jupyter notebook (`Day17_Time_Series.ipynb`) that walks through the
> **complete time series analysis workflow** on a synthetic daily-sales dataset.

---

## 1. Objective

Perform an end-to-end time series analysis: build a daily-sales series that
contains a **trend**, **weekly seasonality**, and **noise**, then load, clean,
feature-engineer, aggregate, detect the trend, analyze seasonality, compute a
growth KPI, and visualize the result.

## 2. The Nine Steps

| Step | Title | Technique |
|------|-------|-----------|
| 1 | Load the time series dataset | `np.linspace`, `np.sin`, `np.random.normal`, `pd.date_range` |
| 2 | Convert and verify the date column | `pd.to_datetime`, `.dtype` |
| 3 | Extract date features | `.dt.month_name()`, `.dt.day_name()` |
| 4 | Aggregate to monthly totals | `.dt.month`, `groupby().sum()` |
| 5 | Identify the trend with a moving average | `.rolling(window=7).mean()` |
| 6 | Analyze weekly seasonality | `groupby("DayName").mean()` |
| 7 | Calculate a growth KPI | `.iloc[-1]` vs `.iloc[0]`, percentage change |
| 8 | Visualize the trend | `matplotlib` line plot + moving average overlay |
| 9 | Document the findings | Markdown summary |

## 3. How the Dataset Is Built (Step 1)

The 120-day series is the sum of three signals, so it behaves like real sales:

```
sales = trend + weekly + noise
```

| Component | Code | Role |
|-----------|------|------|
| **Trend** | `np.linspace(1000, 1600, 120)` | A straight line rising 1000 → 1600 (the growth). |
| **Weekly seasonality** | `150 * np.sin(np.arange(120) * (2*np.pi/7))` | A sine wave repeating every 7 days. |
| **Noise** | `np.random.normal(0, 50, 120)` | Small random day-to-day variation. |

`np.random.seed(42)` fixes the noise so the results are **reproducible** every run.

## 4. How to Run

```bash
# from this folder
pip install numpy pandas matplotlib jupyter

# open interactively...
jupyter notebook Day17_Time_Series.ipynb

# ...or run it headless, writing executed outputs back into the notebook
jupyter nbconvert --to notebook --execute --inplace Day17_Time_Series.ipynb
```

Then run the cells top to bottom (in Jupyter: **Kernel → Restart & Run All**).

## 5. Expected Output (per step)

These values are reproducible thanks to the fixed seed (small differences are
possible across numpy/pandas versions).

**Step 2 — date type**
```
Date column type: datetime64[ns]
```
> On newer pandas versions this may print `datetime64[us]` (microsecond
> resolution) instead of `[ns]`. Either way it confirms the column is a proper
> **datetime** type — that is what the step verifies.

**Step 4 — monthly totals** (rising Jan → Apr, confirming the upward trend)
```
MonthNum
1    33296.0
2    34081.0
3    42485.0
4    45658.0
Name: Sales, dtype: float64
```

**Step 6 — average sales by weekday** (values differ by weekday = weekly seasonality)
```
DayName
Friday       1418.0
Monday       1157.0
Saturday     1369.0
Sunday       1222.0
Thursday     1416.0
Tuesday      1204.0
Wednesday    1286.0
Name: Sales, dtype: float64
```

**Step 7 — growth KPI**
```
Growth from first to last month: 37.1%
```

**Step 8 — chart**

A line plot of noisy daily sales (faint) with the **7-day moving average** (red)
traced on top, showing a clear upward trend through the smoothed line.

## 6. Findings (Step 9)

- Sales show a **clear upward trend** over the four months, confirmed by the
  rising moving average and a strong month-over-month increase (**~37%**).
- A **weekly seasonal pattern** is present — certain weekdays are consistently
  higher than others.
- The underlying growth, separated from noise by the moving average, is **steady
  and positive**.
- **Recommendation:** continue the current strategy driving the growth, and align
  operations with the weekly demand pattern.

## 7. Requirements

- Python 3.8+
- `numpy`, `pandas`, `matplotlib`
- `jupyter` (to open/run the notebook)

## 8. Folder Structure

```
Hands_On_Activity_Time_Series/
├── README.md                  <- you are here
└── Day17_Time_Series.ipynb    <- the notebook (9 steps)
```

## 9. Notes

- The dataset is **synthetic and reproducible** — no real or personal data is included.
- The notebook ships **without saved outputs**; run all cells to generate them.
