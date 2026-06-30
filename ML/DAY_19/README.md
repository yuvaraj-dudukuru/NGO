# Day 19 — Business Analytics Dashboards (Power BI & Tableau Fundamentals)

Three end-to-end **Business Intelligence dashboard case studies**, each delivered as a
self-contained, **interactive HTML dashboard** with synthetic sample data and a README.

These are working implementations of the case studies in *Day 19 — Power BI and Tableau
Fundamentals*. Each dashboard demonstrates the same BI building blocks you would assemble
in Power BI or Tableau: **KPI cards, trend/line charts, bar charts, distribution charts,
and slicers that filter every visual at once.**

> **No personal data.** Every record is 100% synthetic, generated from fixed distributions
> with a fixed random seed by [`generate_sample_data.py`](generate_sample_data.py).
> Identifiers are generic codes (`ORD-…`, `CUST-…`, `EMP-…`) — no names, emails, or real
> people are involved.

## The case studies + hands-on activity

| # | Folder | Dashboard | Audience |
|---|--------|-----------|----------|
| 1 | [`Case_Study_1_Sales_Dashboard/`](Case_Study_1_Sales_Dashboard/) | Sales Performance | Sales Director |
| 2 | [`Case_Study_2_Customer_Analytics_Dashboard/`](Case_Study_2_Customer_Analytics_Dashboard/) | Customer Analytics | Marketing Team |
| 3 | [`Case_Study_3_HR_Dashboard/`](Case_Study_3_HR_Dashboard/) | HR Workforce | Human Resources |
| ★ | [`Hands_On_Activity_Sales_Dashboard/`](Hands_On_Activity_Sales_Dashboard/) | Sales Dashboard (8-step guided build) | Learner / portfolio |
| ★★ | [`Mini_Project_InsightRetail_Dashboard/`](Mini_Project_InsightRetail_Dashboard/) | InsightRetail (full project + **state map** & **drill-down**) | Portfolio submission |

The **Hands-On Activity** is a step-by-step walkthrough (import → explore → charts → KPIs →
filters → assemble → insights → document) that produces the finished dashboard in
[`dashboard.html`](Hands_On_Activity_Sales_Dashboard/dashboard.html) plus a written
[`FINDINGS.md`](Hands_On_Activity_Sales_Dashboard/FINDINGS.md).

The **Mini Project** is the most complete deliverable: a full *InsightRetail* sales dashboard
with 4 KPI cards, a revenue trend, region/category bars, an **interactive US-state choropleth
map**, slicers for region/category/segment/quarter, and **Region → State drill-down** — with
the analysis written up in
[`INSIGHTS.md`](Mini_Project_InsightRetail_Dashboard/INSIGHTS.md).

## How to view a dashboard

1. Open any case-study folder.
2. **Double-click `dashboard.html`** — it opens in your web browser.
3. Use the **slicers** (Region, Category, Segment, Department, …) at the top to filter
   the KPIs and every chart simultaneously. Click **Reset filters** to clear.

No installation, server, or internet connection is required — the charting library
(Chart.js) is vendored locally inside each folder's `lib/` directory.

## Folder layout

```
DAY_19/
├── README.md                       <- you are here
├── generate_sample_data.py         <- reproducible synthetic-data generator
├── Case_Study_1_Sales_Dashboard/
│   ├── README.md
│   ├── dashboard.html              <- open this
│   ├── data/  sales_data.csv  + sales_data.js
│   └── lib/   chart.umd.min.js
├── Case_Study_2_Customer_Analytics_Dashboard/
│   └── … same structure …
├── Case_Study_3_HR_Dashboard/
│   └── … same structure …
├── Hands_On_Activity_Sales_Dashboard/
│   ├── README.md                   <- the 8-step guided build
│   ├── FINDINGS.md                 <- Step 8 documented insights
│   ├── dashboard.html              <- the finished reference dashboard
│   ├── data/  sales_data.csv + sales_data.js
│   └── lib/   chart.umd.min.js
└── Mini_Project_InsightRetail_Dashboard/
    ├── README.md                   <- 7 deliverables + Power BI/Tableau map & drill-down
    ├── INSIGHTS.md                 <- storytelling / recommendations
    ├── dashboard.html              <- full dashboard incl. US-state choropleth map
    ├── data/  insightretail_sales.csv + .js, us-states.geojson + us-states-geo.js
    └── lib/   chart.umd.min.js + chartjs-chart-geo.umd.min.js
```

The `data/*.csv` files are ready to **import directly into Power BI or Tableau** if you want
to rebuild each dashboard in those tools — each case-study README lists the exact steps.

## Regenerating the data

```bash
python generate_sample_data.py
```

This rewrites the `.csv` (for BI tools) and `.js` (for the HTML dashboards) files in every
case-study `data/` folder. The seed is fixed, so the output is identical each run.

---
*Built for training / educational purposes. Data is synthetic; charts render with
[Chart.js](https://www.chartjs.org/).*
