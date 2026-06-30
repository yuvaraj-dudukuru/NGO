# Findings & Recommendations — Sales Dashboard

*Step 8 deliverable for the Hands-On Activity. Figures below come from the synthetic
`data/sales_data.csv` (2,000 orders, Jan 2023 – Dec 2024) and match the interactive
[`dashboard.html`](dashboard.html) with no filters applied.*

## Headline KPIs

| KPI | Value |
|-----|-------|
| **Total Sales** | **≈ $4.17M** |
| **Total Profit** | **≈ $1.28M** |
| **Profit Margin** | **≈ 30.8%** |
| **Orders** | **2,000** |
| **Avg Sales / Order** | **≈ $2,084** |

## Key insights

1. **Leading region — West.** West is the strongest market (**≈ $1.29M**), ahead of Central
   (≈ $1.09M) and East (≈ $1.01M). **South is the weakest** (≈ $0.78M).
2. **Leading product — Laptops.** Laptops are the best-selling product (**≈ $1.04M**),
   narrowly ahead of Accessories and Phones — all three sit inside the **Technology**
   category.
3. **Category concentration.** **Technology drives the business (~$3.04M, ≈ 73% of sales)**;
   Furniture (~$1.05M) is secondary and Office Supplies (~$0.07M) is marginal.
4. **Upward trend with seasonality.** Sales **grew ~31% year over year** (2023 ≈ $1.80M →
   2024 ≈ $2.37M), with a recurring **Q4 (Nov–Dec) seasonal peak** and a softer summer.

## Recommendations

- **Double down on Technology / Laptops** — the clear revenue engine — with inventory and
  promotion, especially ahead of the **Q4 peak**.
- **Investigate the South region.** Its under-performance relative to West suggests a
  coverage, demand, or execution gap worth a deeper look (use the Region slicer to isolate
  it).
- **Re-evaluate Office Supplies.** At ~2% of sales it contributes little — decide whether to
  grow it deliberately or de-prioritise it.
- **Sustain the growth trajectory** — momentum is positive year over year; protect it by
  reinforcing the leading region and category.

## How to reproduce these numbers

Open [`dashboard.html`](dashboard.html) (no filters) to read the KPIs and chart values
directly, or rebuild the dashboard in Power BI / Tableau by importing `data/sales_data.csv`
and following Steps 1–7 in the [README](README.md).

*All data is synthetic — no personal data.*
