# Case Study 2 — Customer Analysis

**Business context.** A marketing team requires a customer analysis showing the
value and activity of each customer segment, with the relevant KPIs.

## Files

| File | Description |
|------|-------------|
| `customer_data.csv` | The raw dataset: `Customer, Segment, Spending` |
| `Customer_Analysis.xlsx` | Workbook with customer KPIs, a segment summary, and a chart |

> Customer names are generic placeholders (`Customer 1` … `Customer 9`).

## The dataset

| Customer | Segment | Spending |
|----------|---------|---------:|
| Customer 1 | Premium | 150,000 |
| Customer 2 | Premium | 135,000 |
| Customer 3 | Premium | 120,000 |
| Customer 4 | Premium | 80,000 |
| Customer 5 | Regular | 30,000 |
| Customer 6 | Regular | 25,000 |
| Customer 7 | Regular | 22,000 |
| Customer 8 | Regular | 18,000 |
| Customer 9 | Regular | 15,000 |

## The analysis

**1. Customer KPIs** (sheet *Customer Data*):

| KPI | Formula | Result |
|-----|---------|-------:|
| Total number of customers | `=COUNTA(Customer)` | 9 |
| Total revenue | `=SUM(Spending)` | 595,000 |
| Average spending per customer | `=AVERAGE(Spending)` | 66,111 |

**2. Segment summary** (sheet *Segment Summary*). A PivotTable with **Segment** in
Rows and both the **Sum** and **Count** of Spending in Values produces the segment
profile. The workbook reproduces this with `SUMIF`, `COUNTIF`, and `AVERAGEIF`:

| Segment | Total Spending | Customers | Avg Spending |
|---------|---------------:|----------:|-------------:|
| Premium | 485,000 | 4 | 121,250 |
| Regular | 110,000 | 5 | 22,000 |

A **bar chart** visualises total spending by segment.

## Business interpretation

The analysis profiles the customer base. **Premium** customers, though fewer in
number (4 vs 5), generate the great majority of revenue (485,000 vs 110,000) and
spend roughly **5.5× more on average** than Regular customers.

**Findings.** The Premium segment is disproportionately valuable.

**Recommendation.** Prioritise retention of Premium customers, and develop
strategies to migrate Regular customers toward Premium spending.

The summary table and the KPIs together form a concise, decision-ready customer
report for a marketing audience.

## Rebuild it yourself

1. **Data → From Text/CSV** → import `customer_data.csv`.
2. Add the three KPI formulas (`COUNTA`, `SUM`, `AVERAGE`) in a summary area.
3. **Insert → PivotTable**: Segment → Rows; Spending → Values **twice**
   (set one to *Sum*, one to *Count*; add *Average* for the third column).
4. Add a **PivotChart** of total spending by segment.
