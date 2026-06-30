# Case Study 2 — Website Traffic Analysis

> Separate the **weekly seasonal pattern** from the **underlying trend** in two
> weeks of daily website traffic using a moving average.

---

## 1. Business Context

A digital business wishes to analyze its daily website traffic to identify:

- overall **growth** in visitors,
- **weekday patterns** (which days are busy vs. quiet), and
- **peak periods** for capacity and content planning.

## 2. Objective

> **Analyze daily website visitors to identify the trend and the weekday pattern.**

## 3. Dataset

Fourteen rows — two consecutive weeks of daily visitor counts starting
2025-06-02.

| Field         | Type            | Description                                   |
|---------------|-----------------|-----------------------------------------------|
| `Date`        | datetime        | Calendar date (14 consecutive days)           |
| `Visitors`    | integer         | Visitor count for that day                    |
| `DayName`     | string (derived)| Weekday name, e.g. `Friday`                   |
| `MovingAvg_7` | float (derived) | 7-day rolling mean of `Visitors`              |

```
Visitors: 1200, 1350, 1300, 1400, 1800, 1900, 1100,
          1300, 1450, 1400, 1500, 1950, 2050, 1200
```

## 4. How to Run

```bash
# from this folder
pip install pandas
python website_traffic_analysis.py
```

## 5. Method — Line by Line

| Code | What it does |
|------|--------------|
| `pd.date_range("2025-06-02", periods=14, freq="D")` | Generates 14 consecutive daily dates. |
| `df["Date"].dt.day_name()` | Extracts the weekday name for each date. |
| `df.groupby("DayName")["Visitors"].mean()` | Averages visitors **per weekday**, revealing the weekly pattern. |
| `df["Visitors"].rolling(window=7).mean()` | Computes a **7-day moving average** that smooths weekly fluctuation and exposes the trend. |
| `df["MovingAvg_7"].dropna().iloc[[0, -1]]` | Compares the first valid moving average with the last to see the trend's direction. |

> **Why a 7-day window?** Averaging over a full week cancels the weekday
> highs and lows, so what remains is the slower-moving **trend**.

## 6. Expected Output

```
Average visitors by day of week:
DayName
Friday       1875.0
Monday       1250.0
Saturday     1975.0
Sunday       1150.0
Thursday     1450.0
Tuesday      1400.0
Wednesday    1350.0
Name: Visitors, dtype: float64

First and last 7-day moving averages:
6     1435.714286
13    1550.000000
Name: MovingAvg_7, dtype: float64
```

> The 7-day moving average **rises from ~1436 to 1550** across the two weeks —
> the underlying trend is gently upward once the weekly cycle is smoothed out.

## 7. Business Interpretation

- **Weekly seasonality:** Traffic **peaks on Friday and Saturday** and is
  **lowest on Sunday and Monday** — a strong, repeating weekly cycle.
- **Trend:** The 7-day moving average removes the weekly cycle and reveals an
  **underlying trend that is gently rising** across the two weeks.
- **Findings:** Traffic follows a **strong weekly cycle** and is **growing
  modestly** overall.

### Recommendations

1. Schedule **major content releases and marketing** for the high-traffic
   **Friday and Saturday** periods.
2. Ensure **server capacity** is sufficient for the **weekend peaks**.

## 8. Key Takeaway

This case study illustrates the **simultaneous presence of weekly seasonality
and an underlying trend**, separated cleanly by the moving average — a core
technique for reading noisy daily data.
