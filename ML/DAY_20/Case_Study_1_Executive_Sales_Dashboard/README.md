# Case Study 1 — Executive Sales Dashboard

> A strategic dashboard for executive leadership of a retail company to monitor sales
> performance against annual targets and guide investment decisions.

## How to view

Open [`index.html`](index.html) in any modern browser (Chrome, Edge, Firefox).
The charts load from a public Chart.js CDN, so an internet connection is needed the
first time. No build step, no install.

---

## Business context

The executive leadership of a retail company requires a **strategic dashboard** to monitor
sales performance against annual targets and to guide investment decisions.

## The design

Following the sales-dashboard blueprint, the dashboard is built as a strategic, glance-able view:

- **Header** establishes the reporting period.
- **Four prominent KPI cards** lead: **Total Revenue**, **Total Profit**, **Growth vs Target**
  (green when above target, red when below), and **Orders**.
- **Revenue trend line** reveals the trajectory against target.
- **Regional bar chart** reveals the markets.
- **Product bar chart** reveals the drivers.
- **Growth momentum chart** quantifies momentum by region (green = growing, red = declining).
- **Slicers** for region, product category, and period enable focus.

### Design principles embodied

| Principle | How it shows up here |
|---|---|
| Prominent KPIs | Four large cards at the top |
| Clear hierarchy | KPIs → trend → breakdowns → momentum |
| Fit-for-purpose charts | Line for trend, bar for comparison |
| Disciplined layout | Consistent grid, generous whitespace |
| Conventional colour | Green = good, red = problem, blue = neutral |
| Story | Leads from headline performance to its sources |

## The insights

The dashboard reveals that **overall revenue is growing and exceeds target**, but that
**one region (South) is declining**, and that this decline is **concentrated in a single
product category (Apparel)**. The headline KPIs show health; the regional and product
breakdowns reveal the localized problem; the colour directs attention to it.

> Filter to **Region = South** and **Product = Apparel** to see the trend line fall
> below target and the "Growth vs Target" KPI flip to red.

## The recommendations

1. **Sustain** the successful overall strategy.
2. **Investigate** the declining South region and the responsible Apparel category as a priority.
3. **Consider reallocating** investment toward the strongest markets and products.

The dashboard carries the executive from headline performance to a specific, actionable
problem — the essence of effective executive reporting.

---

## Data note

All figures are **synthetic sample data** generated in the browser for demonstration of
dashboard design principles. The "South" region and "Apparel" category were deliberately
modelled to decline so the dashboard can tell a complete story. **No real, proprietary, or
personal data is included.**
