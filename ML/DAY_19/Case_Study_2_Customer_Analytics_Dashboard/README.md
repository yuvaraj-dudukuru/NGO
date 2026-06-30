# Case Study 2 — Customer Analytics Dashboard

> **Open [`dashboard.html`](dashboard.html) in your browser to use the interactive dashboard.**

## Business context

A **marketing team** requires a dashboard to understand the **customer base** — its size,
its value by segment, and whether it is growing and being retained.

## Dashboard components

1. **Customer KPI cards** — *Total Customers*, *Average Customer Value*, *Retention Rate*,
   and *Total Revenue*.
2. **Bar chart of revenue by customer segment** — which segments are most valuable.
3. **Doughnut (pie) chart of customer distribution across segments** — composition of the base.
4. **Line chart of customer growth over time** — cumulative signups, revealing the
   acquisition trend.
5. **Slicers** for **Segment**, **Region**, and **Signup Year** — every KPI and chart
   re-filters together. A **Reset filters** button clears them.

## How it was constructed

- Imported the customer data (`data/customer_data.csv`).
- Segmented customers into **Premium / Standard / Basic** (the value segmentation from
  Days 14 & 16).
- Built the KPI cards, the segment revenue bar, the segment-distribution doughnut, and the
  cumulative growth line.
- Arranged KPIs on top, charts below, with the slicer bar above; all visuals are linked.

## Data dictionary — `data/customer_data.csv` (900 synthetic customers, 2023–2024)

| Column | Description |
|--------|-------------|
| `CustomerID` | Synthetic customer code (`CUST-00001`) |
| `SignupDate` | Acquisition date (`YYYY-MM-DD`) |
| `Region` | East, West, North, South |
| `Segment` | Premium, Standard, Basic |
| `TotalRevenue` | Lifetime revenue from the customer |
| `Orders` | Number of orders placed |
| `Retained` | `1` if still active, `0` if churned |

> *Retention Rate* = retained customers ÷ total customers (for the current filter).
> *Average Customer Value* = total revenue ÷ number of customers.

## Business interpretation (from this synthetic data)

- **Size & value:** **900** customers, **~$2,878** average customer value,
  **66.0%** retention rate.
- **Segment value:** **Premium customers are only ~17.8% of the base but generate ~50.1%
  of all revenue** — fewer in number, yet the most valuable, exactly the finding reached
  analytically on Days 14 & 16, now shown interactively.
- **Growth:** the cumulative signup curve **steepens over time → acquisition is
  accelerating.**

**Recommendation:** prioritise **retention and growth of the Premium segment** (highest
value per customer), and **sustain the acquisition strategy** that is driving the
accelerating growth. Use the Region slicer to find where Premium customers concentrate.

## Rebuilding this in Power BI / Tableau

1. **Get Data → Text/CSV** and load `data/customer_data.csv`.
2. Measures: `Total Customers = COUNTROWS(Customers)`,
   `Avg Customer Value = DIVIDE(SUM(TotalRevenue),[Total Customers])`,
   `Retention Rate = DIVIDE(SUM(Retained),[Total Customers])`.
3. **Card** visuals for the KPIs.
4. **Bar chart**: axis = `Segment`, value = `SUM(TotalRevenue)`.
5. **Pie/Doughnut**: legend = `Segment`, value = `Total Customers`.
6. **Line chart**: axis = `SignupDate` (by Month), value = a **running total** of
   `Total Customers`.
7. **Slicers** for `Segment`, `Region`, and `Year` (from `SignupDate`).

*All data is synthetic — no personal data.*
