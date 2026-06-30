# Mini Project — RetailEdge Sales Performance Report

**Problem statement.** You are a data analyst at **RetailEdge**, a retail company.
Given a sales dataset, produce a complete, professional Excel business report that
demonstrates the full range of Excel analytical skills.

This is the capstone deliverable for Day 18: it exercises **import, cleaning,
formulas, logical + text + date + lookup functions, PivotTables, PivotCharts,
conditional formatting, and a one-page report** — all in a single workbook.

## Files

| File | Description |
|------|-------------|
| `sales_data.csv` | The orders dataset — 32 rows, the 8 columns named in the brief |
| `products_reference.csv` | The **separate product master** used for the lookup step |
| `RetailEdge_Sales_Report.xlsx` | Four-sheet workbook: **Raw Orders → Products → Orders → Report** |

> No personal data is used — generic order IDs, regions, products, and segments only.

### A note on the dataset & the lookup requirement

The brief lists `Category` and `Unit Price` among the dataset columns and adds:
*"if product details are in a separate table, use a lookup function to bring them
alongside the orders."* This project takes that design: the transactional file
(`sales_data.csv`) carries the order facts, while **`Category` and `Unit Price`
live in a separate product master** (`products_reference.csv`) and are brought
alongside each order with **`VLOOKUP`**. The enriched **Orders** sheet therefore
contains all eight specified columns — with the two product attributes sourced via
lookup, exactly as the requirement intends.

## Workbook structure (the four sheets)

| Sheet | Purpose |
|-------|---------|
| **Raw Orders** | Imported transactional data (Order ID, Date, Region, Product, Units, Segment) — deliberately *messy* text (stray spaces, mixed case) to drive the cleaning step |
| **Products** | Product master: `Product → Category, Unit Price` (the `VLOOKUP` source) |
| **Orders** | Cleaned + enriched analysis table with all derived columns |
| **Report** | One-page report: KPI panel, three summaries, three charts, written findings |

## How the workbook maps to the 8 required analyses

| # | Requirement | Where / how |
|---|-------------|-------------|
| 1 | Import & clean; data validation on a categorical column | **Raw Orders** (import); **Orders** cleans Region/Product/Segment with `TRIM`+`PROPER`; **data validation** restricts `Customer Segment` to Premium/Regular/Corporate |
| 2 | Revenue, headline KPIs, logical classification | **Orders** col J `=Units*Unit Price`; KPI panel on **Report**; col K `=IF(Revenue>=100000,"High-Value","Standard")` |
| 3 | Lookups | **Orders** cols E & G pull Category and Unit Price from **Products** via `VLOOKUP` |
| 4 | Date analysis — extract month | **Orders** col I `=TEXT(Date,"mmm")` enables monthly analysis |
| 5 | PivotTables — revenue by region, category, month | **Report**: three `SUMIF` summary tables (PivotTable equivalents) |
| 6 | PivotCharts — regional & monthly | **Report**: column charts for region and month (plus a category chart) |
| 7 | Conditional formatting — top performers | top region/category/month highlighted green; High-Value orders highlighted on **Orders** |
| 8 | One-page report | **Report** assembles KPI panel + summaries + charts + findings |

## The cleaning & enrichment formulas (Orders sheet)

```
Region          =PROPER(TRIM('Raw Orders'!C2))      "  south " -> "South"
Product         =PROPER(TRIM('Raw Orders'!D2))
Category        =VLOOKUP(D2, Products!$A$2:$C$7, 2, FALSE)
Unit Price      =VLOOKUP(D2, Products!$A$2:$C$7, 3, FALSE)
Customer Segment=PROPER(TRIM('Raw Orders'!F2))       " premium " -> "Premium"
Month           =TEXT(B2, "mmm")
Revenue         =F2*G2
Classification  =IF(J2>=100000, "High-Value", "Standard")
```

## Headline KPIs

| KPI | Formula | Result |
|-----|---------|-------:|
| Total revenue | `=SUM(Revenue)` | 3,092,500 |
| Average order value | `=AVERAGE(Revenue)` | 96,641 |
| Order count | `=COUNTA(Order ID)` | 32 |
| Largest order | `=MAX(Revenue)` | 300,000 |
| Smallest order | `=MIN(Revenue)` | 12,000 |
| High-Value orders (≥ 100,000) | `=COUNTIF(Classification,"High-Value")` | 12 |

## The three summaries (PivotTable equivalents)

**Revenue by Region** — top region highlighted green:

| Region | Revenue |
|--------|--------:|
| **North** | **1,016,000** |
| East | 933,000 |
| South | 688,000 |
| West | 455,500 |

**Revenue by Category** — top category highlighted green:

| Category | Revenue |
|----------|--------:|
| **Mobile** | **1,510,000** |
| Computers | 1,380,000 |
| Accessories | 202,500 |

**Revenue by Month** — peak month highlighted green:

| Month | Revenue |
|-------|--------:|
| Jan | 390,000 |
| Feb | 330,000 |
| Mar | 572,500 |
| Apr | 643,000 |
| **May** | **1,157,000** |

## Findings & recommendations

**Findings.** Total revenue is **3,092,500** across **32 orders**, with an average
order value of **96,641**. The strongest region is **North** (1,016,000), the
strongest category is **Mobile** (1,510,000), and the peak month is **May**
(1,157,000). **12 of 32** orders qualify as High-Value (≥ 100,000). The weakest
region is **West** (455,500).

**Recommendation.** Concentrate inventory and marketing on the **Mobile** category
and the **North** region; reinforce the sales conditions that drove the **May**
peak (revenue nearly tripled from February); and investigate the lower-performing
**West** region to close the gap.

## Building the *native* PivotTables (optional)

The summaries above mirror native PivotTables. To build the real ones from the
**Orders** sheet:

1. **Insert → PivotTable**.
2. *Revenue by region*: Region → Rows, Revenue → Values (Sum).
3. *Revenue by category*: Category → Rows, Revenue → Values (Sum).
4. *Revenue by month*: Month → Rows, Revenue → Values (Sum).
5. For each, **PivotTable Analyze → PivotChart** (Column) to add the visual.

## Expected outcome

A complete, business-ready workbook: a cleaned and enriched dataset, computed KPIs,
PivotTables (region / category / month), PivotCharts, conditional formatting, and a
written summary — a substantial, portfolio-grade demonstration of Excel analytical
competence.
