# UrbanGrocer — Business Analysis Report

*Prepared by the Data Analytics function · Analysis window: Jan–Jun 2026 · Currency: INR (₹)*

> All figures are derived from the synthetic transactional database in
> `UrbanGrocer_Capstone_Analysis.ipynb`. Revenue is measured on **completed orders only**;
> cancelled orders are excluded throughout.

---

## 1. Executive Summary

Over the first half of 2026, UrbanGrocer recorded **₹11,430 in revenue across 15 completed orders**
from **9 active customers**, at an **average order value of ₹762**. The business is healthy but
**highly concentrated**: the Premium segment and repeat buyers each account for roughly **80% of
revenue**, and just two metros — Bengaluru and Mumbai — drive most sales. Beverages is the single
most valuable category by both revenue and profit, while Produce, though small, carries the best
margin. Three data-quality issues were detected — one completely missing payment and two
payment-versus-order discrepancies — representing **~₹470 of unreconciled value** that needs
finance follow-up.

**Top three actions:** (1) protect and grow the repeat/Premium base with a loyalty programme,
(2) reduce dependence on two cities by expanding marketing into under-penetrated states, and
(3) close the payment-reconciliation gaps and add automated checks.

---

## 2. Business Problem

UrbanGrocer's leadership needs an evidence-based read on the first half of 2026 to guide marketing
spend, assortment, and finance controls. The analysis answers seven questions: baseline KPIs,
category economics, customer behaviour, product performance, geographic concentration, the monthly
trend, and the integrity of the payment records. The objective is not just to report numbers but to
**separate revenue from profit, exclude invalid records, and surface risks** that a headline revenue
figure would hide.

---

## 3. Data Description

A five-table relational schema in SQLite (in-memory):

| Table | Rows | Description |
| --- | ---: | --- |
| `Customers`  | 10 | Identity, city/state, segment (Premium/Regular), signup date. |
| `Products`   | 14 | 14 SKUs across **5 categories** (Produce, Dairy & Eggs, Beverages, Household, Snacks), each with price and cost. |
| `Orders`     | 16 | Order header with status; **1 cancelled** (O-2006). |
| `OrderItems` | 40 | Line items (quantity × unit price). |
| `Payments`   | 14 | Mode, amount, date; **1 missing** (O-2016) and **2 discrepancies**. |

**Business rules applied:** revenue = `Σ(quantity × unit_price)` over `Status = 'Completed'`;
profit = `Σ(quantity × (unit_price − cost))`; margin = profit ÷ revenue. The cancelled order is
never counted as revenue.

---

## 4. Key Findings

### 4.1 Baseline KPIs (completed orders)
| Metric | Value |
| --- | ---: |
| Total revenue | ₹11,430 |
| Completed orders | 15 |
| Active customers | 9 |
| Average order value | ₹762 |

### 4.2 Category economics
| Category | Revenue | Profit | Margin |
| --- | ---: | ---: | ---: |
| Beverages | ₹3,220 | ₹1,240 | 38.5% |
| Snacks | ₹2,940 | ₹960 | 32.7% |
| Household | ₹2,670 | ₹950 | 35.6% |
| Dairy & Eggs | ₹1,660 | ₹475 | 28.6% |
| Produce | ₹940 | ₹369 | 39.3% |

**Beverages leads on both revenue and profit.** Produce has the **highest margin (39.3%)** but the
smallest revenue — a candidate for growth. **Dairy & Eggs has the thinnest margin (28.6%)**: it
drives volume (staples) but contributes little profit per rupee.

### 4.3 Customers
- **Top 5 by revenue:** Aarav Sharma (₹2,830), Karthik Nair (₹2,350), Rohan Gupta (₹1,510),
  Aditya Rao (₹1,410), Priya Menon (₹1,050). Four of the five are **Premium**.
- **Segment split:** Premium = 5 customers / ₹9,040 (**79%** of revenue); Regular = 4 customers /
  ₹2,390 (21%).
- **Repeat vs. one-time:** Repeat (2+ orders) = 5 customers / ₹9,150 (**80%**); one-time = 4
  customers / ₹2,280. Repeat buyers are the engine of the business.
- **Inactive:** 1 registered customer (Manish Verma, Delhi, Regular) has **never placed a completed
  order** — a re-engagement target.

### 4.4 Products
- **By units (staples):** Full Cream Milk (9), Organic Bananas (8), Cold Pressed Juice (6), Potato
  Chips (6), Greek Yogurt (5) — frequency drivers that bring customers back.
- **By revenue (basket value):** Mixed Nuts (₹2,400), Laundry Detergent (₹1,350), Cold Pressed Juice
  (₹1,320), Masala Chai (₹1,000), Paper Towels (₹960) — higher-ticket items that lift order value.

### 4.5 Geography (threshold ≥ ₹1,000)
- **By state:** Maharashtra ₹3,780 and Karnataka ₹3,760 are effectively tied at the top, followed by
  Delhi ₹1,510 and Kerala ₹1,050.
- **By city:** Bengaluru ₹3,760 leads, then Mumbai ₹3,290, Delhi ₹1,510, Kochi ₹1,050. **Two cities
  (Bengaluru + Mumbai) generate ~62% of revenue** — a concentration risk.

### 4.6 Monthly trend
| Month | Orders | Revenue |
| --- | ---: | ---: |
| 2026-01 | 3 | ₹1,930 |
| 2026-02 | 2 | ₹1,210 |
| 2026-03 | 3 | ₹2,920 |
| 2026-04 | 3 | ₹2,070 |
| 2026-05 | 2 | ₹1,990 |
| 2026-06 | 2 | ₹1,310 |

Revenue **peaked in March (₹2,920)** and was softest in February and June. The trend is choppy at
this scale rather than clearly seasonal — worth re-checking as volume grows.

### 4.7 Data quality
- **Missing payment:** order **O-2016 (₹460)** is completed but has **no payment record**.
- **Discrepancies:** **O-2007** was overpaid by **+₹10** (₹500 vs ₹490) and **O-2010** underpaid by
  **−₹20** (₹500 vs ₹520).
- **Net effect:** of ₹11,430 billed, roughly **₹470 is unreconciled** (₹460 uncollected + a net ₹10
  payment mismatch). Small here, but the same defect rate at scale is material.

---

## 5. Recommendations

1. **Launch a loyalty / retention programme.** With ~80% of revenue from repeat and Premium buyers,
   protecting this base is the highest-leverage move — tiered rewards, reorder reminders, and early
   access for Premium.
2. **Grow Produce and Beverages deliberately.** Produce has the best margin but lowest revenue;
   Beverages already leads. Bundle high-margin Produce with high-frequency staples to lift both order
   value and profit.
3. **Diversify geographically.** Two cities drive most revenue. Pilot targeted acquisition in Delhi,
   Kochi, Pune, and Ahmedabad to reduce single-market dependence.
4. **Re-engage and clean the customer base.** Win back the inactive customer and convert one-time
   buyers (₹2,280 today) with a second-order incentive.
5. **Fix payment reconciliation.** Recover the missing ₹460 on O-2016, correct O-2007/O-2010, and add
   an automated nightly check that flags any completed order where `paid_amount ≠ order_value` or a
   payment is absent.

---

## 6. Conclusion

UrbanGrocer is profitable and growing but **concentrated** — in a few Premium, repeat customers and
two metros — and carries **minor but real data-quality debt** in payments. The levers are clear:
deepen loyalty where the money already is, expand the geographic and category base to de-risk growth,
and tighten financial controls before scale turns small leaks into large ones. Acting on the five
recommendations converts a healthy snapshot into a durable, defensible growth plan.

---

*Reproducibility: every figure above is produced by the labelled SQL queries (Q1–Q7) in
`UrbanGrocer_Capstone_Analysis.ipynb`. Re-run the notebook top to bottom to regenerate all results
and charts.*
