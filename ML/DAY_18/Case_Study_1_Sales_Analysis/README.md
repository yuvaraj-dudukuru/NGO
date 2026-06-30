# Case Study 1 — Sales Analysis

**Business context.** A retail manager provides a sales dataset and requires an
analysis of total and average sales, regional performance, and the identification
of top and bottom performers.

## Files

| File | Description |
|------|-------------|
| `sales_data.csv` | The raw dataset: `Region, Product, Units, Price` |
| `Sales_Analysis.xlsx` | Workbook with the Revenue formula, KPIs, a regional summary, and a chart |

## The dataset

| Region | Product | Units | Price |
|--------|---------|------:|------:|
| North | Laptop | 5 | 60,000 |
| South | Phone | 20 | 30,000 |
| East | Laptop | 8 | 60,000 |
| North | Tablet | 15 | 20,000 |
| South | Laptop | 3 | 60,000 |
| East | Phone | 12 | 30,000 |

## The analysis

**1. Revenue column.** A `Revenue` column is computed with `=Units*Price`, entered
in the first data row and copied down (`=C2*D2`, `=C3*D3`, …).

**2. Headline KPIs** (sheet *Sales Data*, KPI block):

| KPI | Formula | Result |
|-----|---------|-------:|
| Total revenue | `=SUM(Revenue)` | 2,220,000 |
| Average revenue per order | `=AVERAGE(Revenue)` | 370,000 |
| Largest order | `=MAX(Revenue)` | 600,000 |
| Smallest order | `=MIN(Revenue)` | 180,000 |

**3. Regional summary** (sheet *Regional Summary*). A PivotTable with **Region** in
Rows and **Sum of Revenue** in Values produces the regional totals. The workbook
reproduces this with `SUMIF`:

| Region | Total Revenue |
|--------|--------------:|
| North | 600,000 |
| South | 780,000 |
| East | 840,000 |

A **PivotChart / bar chart** visualises these totals.

## Business interpretation

The analysis reveals total revenue (2,220,000), the average and range of order
values, and the ranking of regions. **East leads** the regions, and revenue is
concentrated in high-value **Laptop** orders. (In the source narrative East is the
strongest region; in this dataset North records the lowest total at 600,000.)

**Findings.** Revenue is concentrated in high-value Laptop orders, and the East
region leads.

**Recommendation.** Prioritise Laptop inventory and investigate the weakest
region's underperformance.

This case study demonstrates the complete Excel analytical sequence — *formula →
function → PivotTable → chart → insight* — that constitutes everyday analyst work.

## Rebuild it yourself

1. **Data → From Text/CSV** → import `sales_data.csv`.
2. Add `Revenue` with `=C2*D2`, copy down.
3. Add the four KPI formulas in a summary area.
4. **Insert → PivotTable**: Region → Rows, Revenue → Values (Sum).
5. **PivotChart** to visualise revenue by region.
