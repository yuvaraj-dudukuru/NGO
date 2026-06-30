# Day 17 — Time Series Basics

A complete, hands-on study of **time series fundamentals** with `pandas`,
`numpy`, and `matplotlib`: handling dates, aggregating across time, separating
**trend** from **seasonality**, computing **growth KPIs**, visualizing series,
and turning the analysis into **business recommendations**.

The day is organized into three deliverables that build from short, focused case
studies → a guided notebook → a full capstone project.

---

## Contents

| # | Deliverable | What it is | Folder |
|---|-------------|------------|--------|
| 1 | **Business Analytics Case Studies** | Four short, focused analyses (scripts + READMEs) | [`Business_Analytics_Case_Studies/`](Business_Analytics_Case_Studies/) |
| 2 | **Hands-On Activity** | A guided 9-step Jupyter notebook covering the full workflow | [`Hands_On_Activity_Time_Series/`](Hands_On_Activity_Time_Series/) |
| 3 | **Mini Project — MarketPulse** | Capstone: 2 years of daily sales, end-to-end analysis + charts | [`Mini_Project_MarketPulse_Sales_Analysis/`](Mini_Project_MarketPulse_Sales_Analysis/) |

---

## 1. Business Analytics Case Studies

Four self-contained case studies, each in its own folder with a runnable script
and a detailed README.

| Case | Topic | Technique |
|------|-------|-----------|
| 1 | [Retail Sales Analysis](Business_Analytics_Case_Studies/Case_Study_1_Retail_Sales_Analysis/) | Trend + seasonality; `idxmax`/`idxmin`; half-year comparison |
| 2 | [Website Traffic Analysis](Business_Analytics_Case_Studies/Case_Study_2_Website_Traffic_Analysis/) | Weekly seasonality + trend; `groupby` weekday; 7-day moving average |
| 3 | [Customer Growth Analysis](Business_Analytics_Case_Studies/Case_Study_3_Customer_Growth_Analysis/) | Cumulative base + acquisition rate; `cumsum`; `pct_change` |
| 4 | [Inventory Analysis](Business_Analytics_Case_Studies/Case_Study_4_Inventory_Analysis/) | Seasonal demand for stock planning; above-average flagging |

> See the [case-studies index](Business_Analytics_Case_Studies/README.md) for details.

## 2. Hands-On Activity

[`Day17_Time_Series.ipynb`](Hands_On_Activity_Time_Series/Day17_Time_Series.ipynb)
— a guided notebook that walks through the **complete workflow** on a synthetic
daily-sales series:

`load → convert/verify dates → extract features → aggregate → moving-average
trend → weekly seasonality → growth KPI → visualize → document findings`

> See the [activity README](Hands_On_Activity_Time_Series/README.md) for the
> step-by-step guide and expected outputs.

## 3. Mini Project — MarketPulse

The capstone: as a data analyst at *MarketPulse*, analyze **two years of daily
sales** end to end. Covers date handling, monthly/quarterly aggregation, trend
via moving averages, recurring **Q4 seasonality**, **month-over-month vs
year-over-year** growth (and why YoY is more reliable), two charts, and a written
report with recommendations.

**Headline verified results:** upward trend (avg daily sales **+33%**), a
seasonal **Q4 peak that recurs in both years**, and **+22.9% YoY Q4 growth**
(+32.4% total) — real growth beyond seasonality.

> See the [mini-project README](Mini_Project_MarketPulse_Sales_Analysis/README.md)
> for full results and the generated charts.

---

## Concepts Covered Across Day 17

- **Date handling** — `pd.to_datetime`, `DatetimeIndex`, `.dt` accessors
  (`year`, `quarter`, `month_name`, `day_name`).
- **Aggregation** — `groupby` and `resample` to monthly / quarterly totals.
- **Trend** — moving averages (`rolling`) to smooth noise and seasonality.
- **Seasonality** — weekly and annual patterns; confirming recurrence across periods.
- **Growth KPIs** — `cumsum`, `pct_change`, month-over-month, and
  seasonality-adjusted **year-over-year**.
- **Visualization** — daily series with trend overlays; period-over-period comparisons.
- **Business translation** — turning analysis into findings and recommendations.

## Requirements

- Python 3.8+
- `numpy`, `pandas`, `matplotlib`
- `jupyter` (for the Hands-On notebook)

```bash
pip install numpy pandas matplotlib jupyter
```

## How to Run

```bash
# 1. Case studies (run any script from its folder)
python Business_Analytics_Case_Studies/Case_Study_1_Retail_Sales_Analysis/retail_sales_analysis.py

# 2. Hands-on notebook
jupyter notebook Hands_On_Activity_Time_Series/Day17_Time_Series.ipynb

# 3. Mini project (prints the report and writes charts/)
python Mini_Project_MarketPulse_Sales_Analysis/marketpulse_sales_analysis.py
```

## Folder Structure

```
DAY_17/
├── README.md                                  <- you are here (Day 17 index)
├── Business_Analytics_Case_Studies/
│   ├── README.md
│   ├── Case_Study_1_Retail_Sales_Analysis/      (script + README)
│   ├── Case_Study_2_Website_Traffic_Analysis/   (script + README)
│   ├── Case_Study_3_Customer_Growth_Analysis/   (script + README)
│   └── Case_Study_4_Inventory_Analysis/         (script + README)
├── Hands_On_Activity_Time_Series/
│   ├── README.md
│   └── Day17_Time_Series.ipynb
└── Mini_Project_MarketPulse_Sales_Analysis/
    ├── README.md
    ├── marketpulse_sales_analysis.py
    └── charts/
        ├── daily_sales_trend.png
        └── yearly_monthly_comparison.png
```

## Notes

- All datasets are **synthetic and reproducible** (fixed random seeds) — no real
  or personal data is included.
- Monetary figures are illustrative; the techniques are currency-agnostic.
