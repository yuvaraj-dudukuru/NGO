# Business Analytics Case Studies — Time Series Basics

A collection of four self-contained business analytics case studies built around
**time-series fundamentals**: identifying **trend**, **seasonality**, **growth
rates**, and **cumulative measures** with `pandas`.

Each case study lives in its own folder with a runnable Python script and a
detailed README that walks through the business context, the data, the method
(line by line), the expected output, and the business interpretation.

---

## Case Studies

| # | Case Study | Focus / Technique | Folder |
|---|------------|-------------------|--------|
| 1 | **Retail Sales Analysis** | Trend + seasonality; `idxmax` / `idxmin`; half-year comparison | [`Case_Study_1_Retail_Sales_Analysis/`](Case_Study_1_Retail_Sales_Analysis/) |
| 2 | **Website Traffic Analysis** | Weekly seasonality + trend; `groupby` weekday; 7-day moving average | [`Case_Study_2_Website_Traffic_Analysis/`](Case_Study_2_Website_Traffic_Analysis/) |
| 3 | **Customer Growth Analysis** | Cumulative base + acquisition rate; `cumsum`; `pct_change` | [`Case_Study_3_Customer_Growth_Analysis/`](Case_Study_3_Customer_Growth_Analysis/) |
| 4 | **Inventory Analysis** | Seasonal demand for stock planning; above-average flagging; `idxmax` | [`Case_Study_4_Inventory_Analysis/`](Case_Study_4_Inventory_Analysis/) |

## Concepts Covered

- **Trend** — the long-run direction of a series (Case Studies 1, 2, 3).
- **Seasonality** — recurring high/low periods, monthly and weekly (Case Studies 1, 2, 4).
- **Moving average** — smoothing to separate trend from short-term cycles (Case Study 2).
- **Cumulative sum (`cumsum`)** — running totals over time (Case Study 3).
- **Percentage change (`pct_change`)** — period-over-period growth rate (Case Study 3).
- **Peak detection (`idxmax` / `idxmin`)** — locating extremes (Case Studies 1, 4).

## Requirements

- Python 3.8+
- `pandas`

```bash
pip install pandas
```

## How to Run

Each script is standalone. From a case study folder:

```bash
python retail_sales_analysis.py        # Case Study 1
python website_traffic_analysis.py     # Case Study 2
python customer_growth_analysis.py     # Case Study 3
python inventory_analysis.py           # Case Study 4
```

## Repository Structure

```
Business_Analytics_Case_Studies/
├── README.md                                  <- you are here (master index)
├── Case_Study_1_Retail_Sales_Analysis/
│   ├── retail_sales_analysis.py
│   └── README.md
├── Case_Study_2_Website_Traffic_Analysis/
│   ├── website_traffic_analysis.py
│   └── README.md
├── Case_Study_3_Customer_Growth_Analysis/
│   ├── customer_growth_analysis.py
│   └── README.md
└── Case_Study_4_Inventory_Analysis/
    ├── inventory_analysis.py
    └── README.md
```

## Notes

- All datasets are **synthetic and illustrative** — no real or personal data is included.
- Monetary figures are shown in **₹** for the retail/inventory examples; the units
  are illustrative and the techniques are currency-agnostic.
