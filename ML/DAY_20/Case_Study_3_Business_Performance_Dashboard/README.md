# Case Study 3 — Business Performance Dashboard

> A comprehensive, integrated dashboard for the executive team — combining sales, customer,
> and financial metrics to monitor the overall health of the organisation.

## How to view

Open [`index.html`](index.html) in any modern browser. Charts load from a public Chart.js
CDN (internet needed on first load). No build step.

---

## Business context

The executive team requires a comprehensive business-performance dashboard, integrating sales,
customer, and financial metrics, to monitor the overall health of the organisation.

## The design

An integrated strategic dashboard drawing the most important KPIs from across the business:

- **Header** establishes the context.
- **A row of headline KPIs** leads: **Revenue**, **Profit**, **Customer Count**, and **Growth** —
  each measured **against target with conditional colour** (green above target, red below).
- **Revenue & Profit trend** shows top and bottom line over time.
- **Revenue-by-region breakdown** surfaces any localized problem.
- **Customer growth** indicator shows base expansion.
- **Financial summary** charts revenue against expenses — the gap is profit.

The design exemplifies executive reporting: a small set of the most important cross-functional
KPIs, prominently displayed, with focused supporting visualizations, in a clean and disciplined
layout that conveys the state of the **whole business at a glance**.

### Design principles embodied

| Principle | How it shows up here |
|---|---|
| Cross-functional KPIs | Sales + customer + financial in one row |
| Conditional colour | Each KPI turns green/red against its target |
| Clear hierarchy | KPIs → trend → region → customers → finances |
| Fit-for-purpose charts | Line for trends, bar for breakdown & rev-vs-expense |
| Integration | One coherent view of the entire organisation |

## The insights

The dashboard reveals the **integrated health** of the organisation: revenue and profit growing
against target, the customer base expanding, and finances within plan — with any localized problem
(a declining region, a cost overrun, a retention concern) **surfaced for attention**. The
integration lets the executive see the business *whole*, and the relationships between its parts.

> Filter to **Region = South** to see a market lagging the others — the localized problem the
> integrated view is designed to surface.

## The recommendations

1. **Sustain** the elements that are performing.
2. **Address** the specific problems the dashboard surfaces.
3. **Use the integrated view** to balance the priorities of growth, profitability, and customer health.

This is the highest form of executive reporting — integrating the analysis of the entire
organisation into a single, coherent, decision-driving instrument.

---

## Data note

All figures are **synthetic sample data** generated in the browser, with targets chosen so the
KPIs can demonstrate conditional (green/red) colouring. **No real, proprietary, or personal data
is included.**
