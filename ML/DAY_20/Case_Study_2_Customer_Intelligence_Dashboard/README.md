# Case Study 2 — Customer Intelligence Dashboard

> A dashboard for the marketing leadership of a subscription business to understand the
> customer base and guide retention and acquisition strategy.

## How to view

Open [`index.html`](index.html) in any modern browser. Charts load from a public Chart.js
CDN (internet needed on first load). No build step.

---

## Business context

The marketing leadership of a subscription business requires a dashboard to understand the
customer base and to guide retention and acquisition strategy.

## The design

Following the customer-analytics blueprint:

- **Prominent KPIs** lead: **Total Customers**, **Retention Rate**, **Average Customer Value**,
  and **New Customers**.
- **Customer growth line** reveals the acquisition trajectory.
- **Revenue-by-segment bar chart** reveals the valuable segments.
- **Customer-mix doughnut** reveals the composition of the base.
- **Retention trend line** reveals loyalty over time.
- **Slicers** for segment, region, and period enable focus.

The design tells the story of the customer base — leading from its **size and value** to its
**growth, loyalty, and composition**.

### Design principles embodied

| Principle | How it shows up here |
|---|---|
| Prominent KPIs | Four cards: customers, retention, value, new |
| Clear hierarchy | KPIs → growth → value → composition → loyalty |
| Fit-for-purpose charts | Line for trends, bar for value, doughnut for mix |
| Conventional colour | Green for healthy retention; Premium highlighted in gold |
| Story | From "how many / how valuable" to "growing, loyal, composed how" |

## The insights

The dashboard reveals that the **customer base is growing strongly**, that **retention is
healthy**, and that the **Premium segment — though a minority of customers — generates the
majority of revenue.** Compare the **Customer Mix** doughnut (Premium is a thin slice) with the
**Revenue by Segment** bar (Premium towers). The design makes the disproportionate value of the
Premium segment immediately apparent.

> Tip: the doughnut shows Premium as a small share of *customers*, while the segment-revenue
> bar shows it as the largest share of *revenue* — the core finding of customer intelligence.

## The recommendations

1. **Prioritise** the retention and growth of the high-value Premium segment.
2. **Sustain** the acquisition strategy driving overall growth.
3. **Design migration initiatives** to move Regular customers toward Premium spending.

The dashboard delivers customer intelligence to the marketing team in an explorable,
actionable form — supporting the central decisions of customer strategy.

---

## Data note

All figures are **synthetic sample data** generated in the browser. Segments, regions, and
revenue-per-customer are modelled so that Premium is a small share of customers but a large share
of revenue. **No real, proprietary, or personal data is included.**
