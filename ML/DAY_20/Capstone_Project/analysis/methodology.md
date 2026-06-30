# Methodology — GreenCart Capstone

A documented, reproducible account of how the analysis was carried out, from raw data to
recommendations. This is the "notebook/report" deliverable of the capstone.

> **Reproduce everything:** `node data/generate_data.js` regenerates the dataset and the
> dashboard data file deterministically (fixed random seed).

---

## 1. Business problem (Stage 1)

GreenCart's revenue is growing, but profit appears to be lagging. The analysis sets out to
establish **whether margin is eroding, what is driving it, and where to act.**

## 2. Data selection (Stage 2)

A synthetic order-level dataset for FY2025 was generated to resemble a real e-commerce export:
3,617 orders across 4 regions, 5 categories, 3 segments, and ~880 customers. The grain (one row
per order) supports trend, breakdown, and segmentation analysis.

## 3. Cleaning & validation (Stage 3)

The raw transactions were transformed into `sales_clean.csv` by:

1. **Parsing & typing** — `order_date` to ISO date; numeric fields coerced to numbers; category
   fields normalised to a fixed vocabulary.
2. **Feature derivation**
   - `month` = month of `order_date`
   - `revenue` = `unit_price × units × (1 − discount_pct/100)`
   - `cost` = `unit_price × units × cost_ratio(category)`
   - `profit` = `revenue − cost`
   - `margin_pct` = `profit ÷ revenue × 100`
   - `is_new_customer` = 1 on a customer's first order, else 0
3. **Validation rules**
   - `discount_pct` clamped to `[0, 55]`
   - `units`, `revenue`, `cost` non-negative
   - `order_id` unique; `customer_id` consistent in region & segment
4. **Result** — a tidy, trustworthy table, one row per order, ready for analysis.

## 4. Analysis (Stage 4)

| Question | Method | Finding |
|---|---|---|
| Is margin eroding? | Monthly revenue, profit, margin trend | Margin fell ~27% → ~19% as revenue rose |
| What drives it? | Avg discount vs margin by month | Discount roughly doubled (~8% → ~18%); margin tracks it down |
| Which categories? | Revenue & margin by category | Electronics = biggest revenue, thin margin; Grocery structurally low |
| Which regions? | Revenue & margin by region | South = most revenue, **lowest margin** (discount-led) |
| Which segments? | Revenue & customer share by segment | Premium = ~19% of customers, largest revenue share, highest margin |
| Loyalty? | New vs returning orders | ~76% of orders from returning customers |

## 5. KPIs (Stage 5)

Selected to reflect *profitable growth*: Total Revenue, Total Profit, **Profit Margin**,
Average Order Value, Orders, Active Customers, Premium revenue share, and South-region margin.
(Computed live in [`../index.html`](../index.html) and [`../dashboard.html`](../dashboard.html).)

## 6. Dashboard (Stage 6)

Built per dashboard-design principles: prominent KPIs, clear hierarchy, fit-for-purpose charts
(combo bar+line for trend, doughnut for mix), conventional colour, and slicers for interactivity.
See [`../dashboard.html`](../dashboard.html).

## 7–8. Insights & recommendations (Stages 7–8)

Documented in [`../INSIGHTS_AND_RECOMMENDATIONS.md`](../INSIGHTS_AND_RECOMMENDATIONS.md).

## 9. Presentation (Stage 9)

The full project is presented as a report ([`../index.html`](../index.html)) plus an interactive
dashboard, with all supporting deliverables documented — portfolio-ready.

---

### Reproducibility

- **Generator:** [`../data/generate_data.js`](../data/generate_data.js) — deterministic (seeded PRNG).
- **Outputs:** `data/sales_clean.csv` (deliverable) and `assets/data.js` (dashboard data).
- **Privacy:** entirely synthetic; no real, proprietary, or personal data.
