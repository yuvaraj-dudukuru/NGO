# Case Study 1 — Sales Performance Dashboard

> **Open [`dashboard.html`](dashboard.html) in your browser to use the interactive dashboard.**

## Business context

A **sales director** requires an interactive dashboard to monitor sales performance across
**regions, products, and time** — a single place to see the headline numbers, spot the
trend, and drill into any market or product.

## Dashboard components

1. **Revenue KPI cards** at the top — *Total Revenue*, *Total Profit*, *Orders*, and
   *Average Order Value* as prominent figures.
2. **Line chart of revenue over time** (monthly) — reveals the sales trend and seasonality.
3. **Bar chart of revenue by region** — strongest and weakest markets (leader highlighted).
4. **Bar chart of revenue by product** — best-selling products (top 10, horizontal).
5. **Slicers** for **Region**, **Product Category**, and **Time Period (year)** — selecting
   one filters *every* KPI and chart at once. A **Reset filters** button clears them.

## How it was constructed

- Imported the sales data (`data/sales_data.csv`).
- Calculated fields already present per row: **Revenue** = `UnitPrice × Quantity`,
  **Profit** = `(UnitPrice − UnitCost) × Quantity`.
- Built each visual (KPI cards, trend line, regional & product bars).
- Arranged the **KPI cards on top, charts below**, with the **slicer bar** above them.
- Linked all visuals so a slicer selection re-filters the whole page.

## Data dictionary — `data/sales_data.csv` (2,600 synthetic orders, 2023–2024)

| Column | Description |
|--------|-------------|
| `OrderID` | Synthetic order code (`ORD-00001`) |
| `Date` | Order date (`YYYY-MM-DD`) |
| `Region` | East, West, North, South |
| `ProductCategory` | Electronics, Furniture, Office Supplies, Clothing |
| `Product` | Specific product within the category |
| `Quantity` | Units sold |
| `UnitPrice` | Selling price per unit |
| `UnitCost` | Cost per unit |
| `Revenue` | `UnitPrice × Quantity` |
| `Profit` | `(UnitPrice − UnitCost) × Quantity` |

## Business interpretation (from this synthetic data)

The dashboard presents the state of sales at a glance:

- **Headline KPIs:** ~**$5.0M** total revenue, ~**$1.73M** total profit (**34.6% margin**),
  **2,600** orders.
- **Trend:** revenue is **trending upward** across 2023→2024 with clear **seasonality** —
  peaks every November/December (holiday season) and softer summer months.
- **Regions:** **East leads** the market (~$1.68M), followed by West and North;
  **South is the weakest** (~$0.81M).
- **Products:** Electronics products dominate the best-seller list.

**Recommendation:** sustain the upward trend, prioritise the leading product line, lean into
the Q4 seasonal peak with inventory/marketing, and **investigate the weaker South region**
to understand whether it is a demand, coverage, or execution gap.

## Rebuilding this in Power BI / Tableau

1. **Get Data → Text/CSV** and load `data/sales_data.csv`.
2. (Optional) recreate measures: `Total Revenue = SUM(Revenue)`,
   `Total Profit = SUM(Profit)`, `Orders = COUNTROWS(Sales)`,
   `Avg Order Value = DIVIDE([Total Revenue],[Orders])`.
3. Add **Card** visuals for the KPIs.
4. Add a **Line chart**: axis = `Date` (by Month), value = `Total Revenue`.
5. Add a **Bar/Column chart**: axis = `Region`, value = `Total Revenue`.
6. Add a **Bar chart**: axis = `Product`, value = `Total Revenue` (Top N = 10).
7. Add **Slicers** for `Region`, `ProductCategory`, and `Year` (from `Date`).
8. Arrange KPIs on top, charts below; slicers filter the page automatically.

*All data is synthetic — no personal data.*
