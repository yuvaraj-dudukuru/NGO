# Mini Project — MarketPulse: Two-Year Daily Sales Time Series Analysis

> **Role:** Data analyst at *MarketPulse*, a retail company.
> **Goal:** Conduct a complete time series analysis of two years of daily sales —
> assess performance over time, separate **trend** from **seasonality**, compute
> **growth KPIs** (including a seasonality-adjusted year-over-year figure),
> visualize the series, and deliver **business recommendations**.

This is the capstone for Day 17 — a complete, end-to-end demonstration of time
series competence.

---

## 1. Problem Statement

Given ~730 days of daily sales spanning two full years, perform a complete time
series analysis to assess the company's performance, identify trends and
seasonality, compute growth, and produce business recommendations.

## 2. The Dataset

A synthetic daily-sales series is constructed with a **DatetimeIndex** from three
components, so it behaves like real retail data:

| Component | Code | Role |
|-----------|------|------|
| **Trend** | `np.linspace(1000, 1800, 730)` | Upward growth across the two years. |
| **Annual seasonality** | `300 * np.sin(2π·(day_of_year − 238.75)/365.25)` | A yearly cycle phased to **peak in the final quarter (Q4)** every year. |
| **Noise** | `np.random.normal(0, 40, 730)` | Random day-to-day variation. |

```
sales = trend + seasonal + noise
```

`np.random.seed(42)` makes the series fully **reproducible**. Date span:
**2024-01-01 → 2025-12-30** (730 days). *No real or personal data is used.*

## 3. How to Run

```bash
# from this folder
pip install numpy pandas matplotlib
python marketpulse_sales_analysis.py
```

This prints the full analysis report to the console and writes two charts to
`charts/`.

## 4. Required Analysis — What the Script Does

| # | Section | Method |
|---|---------|--------|
| 1 | **Date handling** | Confirms a `DatetimeIndex`; extracts `Year`, `Quarter`, `Month`, `MonthName`, `DayName`. |
| 2 | **Aggregation** | `resample("ME").sum()` (monthly) and `resample("QE").sum()` (quarterly) totals. |
| 3 | **Trend identification** | 30-day and 90-day centered moving averages; year-over-year change in average daily sales. |
| 4 | **Seasonality analysis** | Average sales by month and quarter; identifies the strongest quarter and confirms it **recurs in both years**. |
| 5 | **Growth KPIs** | Month-over-month growth **and** year-over-year growth for the peak quarter, with an explanation of why YoY is more reliable. |
| 6 | **Visualization** | (a) daily sales + moving average; (b) two-year monthly-pattern comparison. |
| 7 | **Insights & recommendations** | A printed business report with four recommendations. |

## 5. Key Results (verified by running the script)

### Trend (Section 3)
Average daily sales rose **1201 → 1598** from Year 1 to Year 2 — a **+33.1%**
increase. The moving average climbs steadily once noise and seasonality are
smoothed → a **genuine upward trend**.

### Seasonality (Section 4)

Average daily sales by **quarter** (both years combined):

| Quarter | Q1 | Q2 | Q3 | **Q4** |
|---------|----|----|----|--------|
| Avg sales | 1295 | 1082 (low) | 1402 | **1815 (peak)** |

- **Strongest quarter: Q4** — and it is the strongest quarter in **both** 2024
  and 2025 (the seasonal peak **recurs**, confirmed programmatically).
- Strongest months are **October, November, December** (~1744–1855); the
  mid-year (**April–May**, ~1055–1090) is the trough.

Quarterly totals by year (note Q4 is highest in each column):

| Quarter | 2024 | 2025 |
|---------|------|------|
| Q1 | 99,407 | 135,074 |
| Q2 | 80,564 | 116,314 |
| Q3 | 110,635 | 147,331 |
| **Q4** | **149,009** | **183,127** |

### Growth KPIs (Section 5)

| KPI | Value | Notes |
|-----|-------|-------|
| Average month-over-month growth | ~2.7% | **Volatile** — mixes real growth with the annual seasonal swing. |
| **Year-over-year, Q4 (peak quarter)** | **+22.9%** | Same-season comparison → reflects **real** growth. |
| Year-over-year, annual total | **+32.4%** | Confirms growth beyond seasonality. |

> **Why YoY is the more reliable measure:** comparing the **same quarter across
> years** holds the season constant, so the change reflects genuine growth rather
> than the predictable seasonal cycle that distorts month-over-month figures.

## 6. Visualizations (Section 6)

Both are generated into [`charts/`](charts/):

| File | What it shows |
|------|---------------|
| [`charts/daily_sales_trend.png`](charts/daily_sales_trend.png) | Noisy daily sales with the 30-day (red) and 90-day (dashed) moving averages. The smoothed line reveals the recurring annual hump **rising** across the two years. |
| [`charts/yearly_monthly_comparison.png`](charts/yearly_monthly_comparison.png) | Monthly totals for 2024 vs 2025 overlaid. The **2025 line sits above 2024 at every month** (YoY growth) and **both share the same shape** (mid-year dip, Q4 peak → recurring seasonality). |

## 7. Insights & Recommendations (Section 7)

**Findings**
- **Trend:** A genuine upward trend across both years (+33% in average daily sales).
- **Seasonality:** A strong, recurring **Q4 peak** in both years; mid-year (Q2) is the low.
- **Growth:** Positive **year-over-year** growth (Q4 **+22.9%**, total **+32.4%**) —
  real growth beyond the seasonal effect.

**Recommendations**
1. **Inventory planning:** Build stock and staffing ahead of **Q4 every year** to
   capture the recurring peak without stockouts; keep stock **lean mid-year** to
   cut holding costs.
2. **Sustain the growth:** Positive YoY confirms the strategy works beyond
   seasonality — keep investing in what drives the trend.
3. **Report on YoY, not MoM:** Use same-season year-over-year comparisons for
   targets and reporting, since month-over-month is distorted by the annual cycle.
4. **Marketing timing:** Concentrate campaigns in the **Q4 ramp** to amplify the
   period that already converts best.

## 8. Requirements

- Python 3.8+
- `numpy`, `pandas`, `matplotlib`

## 9. Folder Structure

```
Mini_Project_MarketPulse_Sales_Analysis/
├── README.md                       <- you are here
├── marketpulse_sales_analysis.py   <- full analysis pipeline (7 sections)
└── charts/
    ├── daily_sales_trend.png
    └── yearly_monthly_comparison.png
```

## 10. Skills Demonstrated

Correct date handling • time-based aggregation (`resample`) • separating **trend**
from **seasonality** via moving averages • **growth KPIs** including the
seasonality-adjusted **year-over-year** figure • effective time series
visualization • translating analysis into **business recommendations**.

> The charts in `charts/` are regenerated every run; delete them to confirm the
> script recreates them from scratch.
