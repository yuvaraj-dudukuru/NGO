# FreshCart — EDA Report

**Analyst:** Junior Data Analyst, FreshCart
**Dataset:** 12 recent orders × 6 columns

---

## Executive Summary

We analyzed 12 recent FreshCart orders across **3 cities** (Pune, Mumbai, Delhi)
and **3 categories** (Fruits, Dairy, Snacks). Order demand is **evenly balanced**
across cities (4 orders each). Revenue per order is **right-skewed** — the mean
(₹1,117) sits well above the median (₹760) — driven by a single unusually large
order. Order size (number of items) is the dominant driver of both **revenue**
and **delivery time**.

---

## Data Overview

- **Shape:** 12 rows × 6 columns, no missing values.
- **Numeric summary (`describe`)**: `OrderValue` ranges ₹320–₹5,000;
  `DeliveryMins` ranges 22–75 minutes; `Items` ranges 6–30.

| Metric        | Mean   | Median | Skew         |
|---------------|--------|--------|--------------|
| OrderValue    | ₹1,117 | ₹760   | Right-skewed |
| DeliveryMins  | 40.4   | 36.5   | Right-skewed |

---

## Key Findings

1. **Balanced demand.** Pune, Mumbai, and Delhi each have 4 orders — no single
   city dominates volume.
2. **Right-skewed revenue.** The mean order value far exceeds the median,
   signalling one or more very large orders.
3. **Outlier confirmed (IQR).** With Q1 = ₹460, Q3 = ₹1,125, IQR = ₹665, the
   upper fence is ₹2,122.5. **Order 10 (₹5,000, Mumbai, Snacks, 30 items)** is a
   clear outlier.
4. **Items drive revenue.** `Items` vs `OrderValue` correlation = **+0.84**
   (very strong positive).
5. **Items drive delivery time.** `Items` vs `DeliveryMins` correlation =
   **+0.99** (very strong positive) — larger orders take longer to deliver.
6. **Snacks lead value.** Snacks has the highest average order value (₹2,200),
   ahead of Dairy (₹755) and Fruits (₹395).
7. **Delivery speed by city.** Pune is fastest (29.5 min avg), then Delhi
   (39.2 min), then Mumbai (52.5 min — inflated by the large order).

---

## Insight Ladder (Observation → Insight → Recommendation)

**Finding A — The large outlier**
- *Observation:* Order 10 is ₹5,000 with 30 items — a statistical outlier.
- *Insight:* This is most likely a genuine bulk / high-value customer, not a
  data-entry error.
- *Recommendation:* Verify the order, then retain and grow this customer with a
  **loyalty or B2B/bulk program** rather than discarding it as noise.

**Finding B — Big orders are slow**
- *Observation:* Delivery time climbs almost perfectly with item count; the
  biggest order took 75 minutes.
- *Insight:* Large, often Snacks-heavy orders are the slowest to fulfill and
  risk hurting customer experience.
- *Recommendation:* Optimize **picking, packing, and routing** for large orders
  (dedicated pickers, order batching) to reduce long delivery times.

---

## Recommendations (Summary)

1. **Investigate & nurture** the large outlier customer with a bulk/loyalty offer.
2. **Streamline fulfillment** for large orders to cut delivery delays.
3. **Run basket-building promotions** — more items per order directly increases
   revenue (strong positive correlation).
4. **Monitor Snacks demand & delivery SLAs** as average order sizes grow.

---

## Stretch Goals

- **Full correlation matrix** computed via `orders.corr(numeric_only=True)` —
  confirms `Items`, `OrderValue`, and `DeliveryMins` all move together.
- **Ideal market:** ranking cities by *high value + fast delivery* points to
  **Delhi** as the best overall blend (solid value with reasonable speed), while
  Mumbai's high value comes at the cost of slow deliveries.
