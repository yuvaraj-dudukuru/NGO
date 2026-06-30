# Mini Project — InsightRetail Sales Performance Dashboard

**Role:** Data analyst at *InsightRetail*, a retail company.
**Goal:** Build a complete, interactive BI dashboard (Power BI or Tableau) that monitors
sales performance and supports decision-making.

> **See the finished result:** open **[`dashboard.html`](dashboard.html)** in your browser —
> a working reference implementation with KPI cards, a revenue trend, region/category bars,
> an **interactive US-state choropleth map**, slicers, and **Region → State drill-down**.
> The written analysis is in **[`INSIGHTS.md`](INSIGHTS.md)**.

> **No personal data.** The dataset is 100% synthetic (see
> [`../generate_sample_data.py`](../generate_sample_data.py)). Identifiers are codes only.

---

## The dataset — `data/insightretail_sales.csv` (700 rows, Jan–Dec 2024)

Far exceeds the 50-row minimum, spanning **12 months, 4 regions, 21 states, 3 categories,
11 products, and 3 customer segments.**

| Column | Role | Notes |
|--------|------|-------|
| `Order ID` | dimension | Synthetic code (`ORD-00001`) |
| `Date` | dimension | `YYYY-MM-DD`, all of 2024 |
| `Region` | dimension | West, East, Central, South |
| `State` | dimension | Full US state name (joins the map) |
| `Product` | dimension | e.g. Phones, Chairs, Binders |
| `Category` | dimension | Technology, Furniture, Office Supplies |
| `Units` | measure | Units sold |
| `Unit Price` | measure | Price per unit |
| `Customer Segment` | dimension | Consumer, Corporate, Home Office |
| `Revenue` | **calculated** | `Units × Unit Price` |
| `Profit` | **calculated** | margin applied per category |

---

## Required deliverables — and how this project meets them

### 1. Import and prepare
- **Power BI:** *Get Data → Text/CSV* → `insightretail_sales.csv` → *Transform Data* to verify
  types and clean, then *Close & Apply*.
- **Tableau:** *Connect → Text File*; confirm dimension/measure roles on the Data Source page.
- **Calculated fields:** `Revenue = Units * [Unit Price]`, `Profit` from category margin.
  (Both are pre-computed in the CSV so the dashboard works immediately, and the formula is
  documented above for you to recreate.)

### 2. KPI cards
Headline cards for **Total Revenue**, **Total Profit**, **Number of Orders**, and
**Average Order Value** (`Total Revenue ÷ Number of Orders`).

### 3. Visualizations
- **Revenue trend** — line chart of monthly revenue.
- **Revenue by region** — bar chart.
- **Revenue by category** — bar chart.
- **Map of revenue by state** — a **choropleth** (darker = more revenue), plus a companion
  *Top States* bar for exact figures. A *Revenue by Customer Segment* chart is included as a
  bonus.

### 4. Interactivity
- **Slicers** for **Region**, **Category**, **Segment**, and **Time Period** (quarter); every
  visual is **linked** and re-filters together.
- **Drill-down:** click a **Region** bar to drill into that region (the map and all charts
  update to that region's states); click a **Category** bar to filter by category. A
  breadcrumb shows the active drill path.

### 5. Dashboard
KPI cards are **prominent at the top**, charts are arranged logically below, and the slicers
sit in an **accessible strip** across the top.

### 6. Storytelling and insights
Every visual has a clear title and helper caption. The key insights and recommendations are
documented in **[`INSIGHTS.md`](INSIGHTS.md)**.

### 7. Publish (optional)
- **Power BI:** *Publish* → **Power BI Service**, then *Share* / publish to web.
- **Tableau:** *Server → Tableau Public → Save to Tableau Public* for a portfolio link.

---

## Rebuilding the map & drill-down in the BI tools

**Power BI**
- Map: use the **Filled Map (choropleth)** visual → *Location* = `State`, *Color saturation* =
  `Sum(Revenue)`. (Set the data category of `State` to *State/Province* for correct geocoding.)
- Drill-down: build a hierarchy `Region → State` on the map's Location, then use the drill
  buttons (the down-arrow) to expand a region into its states.

**Tableau**
- Map: double-click `State` (a geographic field) to plot it, then drag `Revenue` to *Color*
  to make it a choropleth.
- Drill-down: create a hierarchy by dragging `State` onto `Region` in the Data pane; the `+`
  control on the map then drills Region → State.

---

## Expected outcome

A complete, interactive, well-designed dashboard with KPI cards, multiple **linked**
visualizations (including a **state map** and **drill-down**), slicers, and documented
business recommendations — a full demonstration of BI competence and a strong, publishable
portfolio piece.

*All data is synthetic — no personal data.*
