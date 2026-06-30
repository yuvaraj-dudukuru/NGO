# Day 18 — Excel for Data Analysts

This folder contains five self-contained Excel deliverables that demonstrate the
complete analyst workflow: **import → clean → formula → function → PivotTable →
PivotChart → insight**. Three are business analytics *case studies*, one is a
guided *hands-on activity* that walks through every step end-to-end, and one is a
capstone *mini project* — a full, portfolio-grade business report.

Each deliverable lives in its own folder and ships with:

- a **CSV dataset** (open it directly in Excel, or use it to rebuild the workbook),
- an **`.xlsx` workbook** with *live* formulas, a summary table, and a chart, and
- a folder-level **`README.md`** explaining the data, the formulas, and the findings.

> **No personal data is included.** All names are generic placeholders
> (`Customer 1`, `Employee 1`, region/product labels only).

## Folder structure

```
DAY_18/
├── README.md                              ← you are here
├── Case_Study_1_Sales_Analysis/
│   ├── sales_data.csv
│   ├── Sales_Analysis.xlsx
│   └── README.md
├── Case_Study_2_Customer_Analysis/
│   ├── customer_data.csv
│   ├── Customer_Analysis.xlsx
│   └── README.md
├── Case_Study_3_Employee_Performance/
│   ├── employee_data.csv
│   ├── Employee_Performance.xlsx
│   └── README.md
├── Hands_On_Activity_Sales_Report/
│   ├── sales_data_raw.csv
│   ├── Sales_Report.xlsx
│   └── README.md
└── Mini_Project_RetailEdge_Sales_Report/
    ├── sales_data.csv
    ├── products_reference.csv
    ├── RetailEdge_Sales_Report.xlsx
    └── README.md
```

## The five deliverables at a glance

| # | Folder | Theme | Key techniques |
|---|--------|-------|----------------|
| 1 | `Case_Study_1_Sales_Analysis` | Sales (total/average, regional ranking) | `SUM`, `AVERAGE`, `MAX`, `MIN`, `SUMIF`, bar chart |
| 2 | `Case_Study_2_Customer_Analysis` | Customer segments (value & activity) | `COUNTA`, `SUM`, `AVERAGE`, `SUMIF`, `COUNTIF`, `AVERAGEIF` |
| 3 | `Case_Study_3_Employee_Performance` | HR performance by department | nested `IF`, `AVERAGEIF`, `COUNTIF`, conditional formatting |
| 4 | `Hands_On_Activity_Sales_Report` | One-page sales report (all 9 steps) | `TRIM`, `PROPER`, data validation, `SUMIFS` matrix, `IF`, conditional formatting, column chart |
| 5 | `Mini_Project_RetailEdge_Sales_Report` | Capstone: full RetailEdge business report (32 orders) | `TRIM`/`PROPER`, data validation, `VLOOKUP`, `TEXT` (date→month), `IF`, `SUMIF` summaries (region/category/month), conditional formatting, 3 charts |

## How to use these workbooks

1. **Open the `.xlsx` file in Microsoft Excel** (or LibreOffice Calc / Google Sheets).
2. The formulas are **live**: cells store the formula (e.g. `=Units*Price`,
   `=SUM(...)`), and Excel recalculates them on open. The workbooks are flagged to
   *full-calc on load*, so the headline numbers appear automatically.
3. Each workbook has a **data sheet** and one or more **summary/report sheets**
   with a chart.

### A note on PivotTables

The case studies are written around **PivotTables**. These workbooks reproduce the
exact same result using **`SUMIF` / `COUNTIF` / `AVERAGEIF` / `SUMIFS`** summary
tables, because those formulas are transparent, portable, and easy to audit.

To build the *native* PivotTable described in each case study:

1. Click any cell in the data sheet.
2. **Insert → PivotTable**.
3. Drag the field named in the case study into **Rows** (and **Columns** where
   stated), and drag the value field into **Values** (set to *Sum*, *Count*, or
   *Average* as required).
4. **PivotTable Analyze → PivotChart** to add the matching chart.

The summary table already in each workbook shows you the numbers the PivotTable
should produce, so you can check your work.

## Rebuilding from the CSVs

The CSV in each folder is the raw input. If you want to recreate a workbook from
scratch, import the CSV via **Data → From Text/CSV**, then follow the steps in that
folder's `README.md`.
