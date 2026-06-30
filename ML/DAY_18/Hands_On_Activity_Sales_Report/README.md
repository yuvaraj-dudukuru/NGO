# Hands-On Activity — One-Page Sales Report

A complete, guided Excel analysis taking a **messy raw dataset** all the way to a
**one-page business report**. It covers all nine steps of the activity: import,
clean, formulas, functions, PivotTable, PivotChart, KPIs, summary report, and
documented findings.

## Files

| File | Description |
|------|-------------|
| `sales_data_raw.csv` | The **raw, deliberately messy** dataset (stray spaces, inconsistent capitalisation) |
| `Sales_Report.xlsx` | Three-sheet workbook: **Raw Import → Clean Data → Report** |

> No personal data is used — only generic region and product labels.

## How the workbook maps to the 9 steps

| Step | What it does | Where to find it |
|------|--------------|------------------|
| 1 — Import | Raw dataset imported with headers; numbers right-aligned (numeric) | sheet **Raw Import** |
| 2 — Clean | `TRIM` removes stray spaces, `PROPER` standardises capitalisation; **data validation** restricts Region to North/South/East/West | sheet **Clean Data**, cols A–B |
| 3 — Formulas | `Revenue` column with `=Units*Price`, copied down | sheet **Clean Data**, col E |
| 4 — Functions | KPI functions + a classification column `=IF(Revenue>=100000,"High","Standard")` | KPIs on **Report**; classification on **Clean Data** col F |
| 5 — PivotTable | Region (Rows) × Product (Columns), Sum of Revenue — reproduced with a `SUMIFS` matrix | sheet **Report**, "Revenue by Region and Product" |
| 6 — PivotChart | Column chart of revenue by region | sheet **Report** (chart at top-right) |
| 7 — KPIs | KPI summary table assembled at the top of the report | sheet **Report**, "Key Performance Indicators" |
| 8 — Summary report | KPIs + matrix + chart + title + findings on one worksheet | sheet **Report** |
| 9 — Findings | Written findings & recommendations; conditional formatting highlights top performers | sheet **Report** + green highlights |

## Step 2 in detail — the cleaning

The **Clean Data** sheet pulls from **Raw Import** and standardises it live:

```
Region  =PROPER(TRIM('Raw Import'!A2))     "  north " -> "North"
Product =PROPER(TRIM('Raw Import'!B2))     "PHONE "  -> "Phone"
```

The Region column also carries **data validation** (a dropdown list restricted to
`North, South, East, West`) so future manual entries cannot introduce invalid
regions.

## Step 4 — the KPIs

| KPI | Formula | Result |
|-----|---------|-------:|
| Total revenue | `=SUM(Revenue)` | 2,340,000 |
| Average order value | `=AVERAGE(Revenue)` | 292,500 |
| Largest order | `=MAX(Revenue)` | 600,000 |
| Number of orders | `=COUNTA(Region)` | 8 |

The classification column flags orders ≥ 100,000 as **High** (highlighted green),
everything else as **Standard**.

## Step 5 — the Region × Product matrix

Built with `SUMIFS` (one PivotTable cell per region/product combination):

| Region | Laptop | Phone | Tablet | **Total** |
|--------|-------:|------:|-------:|----------:|
| North | 300,000 | 0 | 300,000 | **600,000** |
| South | 180,000 | 600,000 | 0 | **780,000** |
| East | 480,000 | 60,000 | 0 | **540,000** |
| West | 360,000 | 0 | 60,000 | **420,000** |
| **Grand Total** | **1,320,000** | **660,000** | **360,000** | **2,340,000** |

The top region total (**South**, 780,000) is highlighted in green by conditional
formatting.

## Step 9 — findings & recommendations

**Findings.** Total revenue is **2,340,000** across **8 orders**, with an average
order value of **292,500**. **South** is the top-performing region and **Laptop**
is the top-performing product (1,320,000); **West** records the lowest revenue.

**Recommendation.** Prioritise Laptop inventory and replicate South's sales
practices in other regions; investigate and support the lower-performing West
region.

## Expected outcome

A complete, professional Excel workbook containing a cleaned dataset, computed
KPIs, a PivotTable (matrix), a PivotChart, and a written summary — the kind of
deliverable an analyst produces routinely in business.

## Building the *native* PivotTable (optional)

The matrix above mirrors a native PivotTable. To build the real thing:

1. Click any cell in **Clean Data**.
2. **Insert → PivotTable**.
3. **Region → Rows**, **Product → Columns**, **Revenue → Values** (Sum).
4. **PivotTable Analyze → PivotChart** → Column, to visualise revenue by region.
