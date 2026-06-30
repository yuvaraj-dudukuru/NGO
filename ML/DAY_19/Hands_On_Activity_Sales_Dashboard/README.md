# Hands-On Activity — Build a Complete Sales Dashboard

A guided, step-by-step activity that takes you from a raw dataset to a finished, interactive
BI dashboard with **KPI cards, linked charts, and filters**, plus **documented findings**.
It can be performed in **Power BI** or **Tableau** — the steps below are generic, with
tool-specific actions called out.

> **Want to see the finished result first?** Open **[`dashboard.html`](dashboard.html)** in
> your browser — it is a working reference implementation of the expected outcome.
> Findings are written up in **[`FINDINGS.md`](FINDINGS.md)**.

> **No personal data.** The dataset is 100% synthetic (see
> [`../generate_sample_data.py`](../generate_sample_data.py)).

---

## The dataset — `data/sales_data.csv` (2,000 synthetic orders, 2023–2024)

| Column | Type | Role | Description |
|--------|------|------|-------------|
| `OrderID` | text | dimension | Synthetic order code (`ORD-00001`) |
| `Date` | date | dimension | Order date (`YYYY-MM-DD`) |
| `Region` | text | dimension | West, East, Central, South |
| `Category` | text | dimension | Technology, Furniture, Office Supplies |
| `Product` | text | dimension | Specific product within the category |
| `Quantity` | number | measure | Units sold |
| `Sales` | number | **measure** | Order sales amount |
| `Profit` | number | **measure** | Order profit |

A `data/sales_data.js` copy of the same data powers the HTML reference dashboard.

---

## Step 1 — Import the dataset

- **Power BI:** *Home → Get Data → Text/CSV* → select `data/sales_data.csv` → **Load**
  (or *Transform Data* to inspect first).
- **Tableau:** *Connect → Text File* → select `data/sales_data.csv`.

✅ **Verify** all 8 columns are present and correctly typed (`Date` as a date, `Sales`/
`Profit`/`Quantity` as numbers).

## Step 2 — Explore the data

- **Power BI:** open the **Data View** to scan rows and confirm data types in the column
  tools.
- **Tableau:** stay on the **Data Source** page; confirm that `Sales`, `Profit`, `Quantity`
  are **measures** and `Region`, `Category`, `Product`, `Date` are **dimensions**.

Note the **categorical fields** (Region, Category, Product — for grouping) and the
**numeric fields** (Sales, Profit — for measuring).

## Step 3 — Create charts

Build the three core visuals:

| Chart | Power BI | Tableau |
|-------|----------|---------|
| **Sales by Region** (bar) | Clustered bar: Axis `Region`, Value `Sum(Sales)` | Columns `Region`, Rows `SUM(Sales)` |
| **Sales over Time** (line) | Line: Axis `Date` (Month), Value `Sum(Sales)` | Columns `MONTH(Date)`, Rows `SUM(Sales)` |
| **Sales by Product** (bar) | Bar: Axis `Product`, Value `Sum(Sales)`, sort desc | Rows `Product`, Columns `SUM(Sales)`, sort desc |

✅ Confirm each chart conveys its message clearly (sort bars descending; format the line
axis by month).

## Step 4 — Create KPI cards

Create three **KPI / Card** visuals for the headline figures:

- **Total Sales** = `SUM(Sales)`
- **Total Profit** = `SUM(Profit)`
- **Orders** = `COUNT(OrderID)` (Power BI: `COUNTROWS(Sales)`)

Make the numbers large and prominent.

## Step 5 — Add filters

Add filter controls so the viewer can focus the dashboard:

- **Power BI:** add three **Slicers** for `Region`, `Category`, and `Date` (year).
- **Tableau:** add **Filters** for `Region`, `Category`, `YEAR(Date)`; *Show Filter* and
  set them to *Apply to all using this data source*.

## Step 6 — Build the dashboard

Assemble everything onto one canvas:

- **Power BI:** arrange on the report page — **KPI cards across the top**, **charts below**,
  **slicers in an accessible strip** (top or left). Slicers filter the page automatically.
- **Tableau:** create a **Dashboard**, drag each sheet in, position KPIs on top and charts
  below, and add the filters. Ensure filters are set to apply to all sheets so the visuals
  are **linked**.

✅ Test the linkage: selecting a region (or clicking a bar) should update every other visual.

## Step 7 — Generate insights

Interact with the dashboard to discover insights:

- Which **region** and **product** lead? Which lag?
- Is the **sales trend** rising or falling? Any **seasonality**?
- Use the slicers (and drill-down, if configured) to investigate a single category or year.

## Step 8 — Document the findings

Record the key insights and a recommendation grounded in the analysis, and add clear titles /
annotations. A completed write-up for this dataset is provided in **[`FINDINGS.md`](FINDINGS.md)**.

---

## Expected outcome

A complete, interactive dashboard with **KPI cards, multiple linked visualizations, and
filters**, accompanied by **documented insights** — a professional BI deliverable and a
strong portfolio piece (especially once published to the Power BI Service or Tableau Public).

*All data is synthetic — no personal data.*
