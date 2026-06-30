# InsightRetail — Insights & Recommendations

*Deliverable 6 (Storytelling & insights). Figures come from the synthetic
`data/insightretail_sales.csv` (700 orders, full-year 2024) and match the unfiltered
[`dashboard.html`](dashboard.html).*

## Headline KPIs

| KPI | Value |
|-----|-------|
| **Total Revenue** | **≈ $1.47M** |
| **Total Profit** | **≈ $175.6K** |
| **Profit Margin** | **≈ 12.0%** |
| **Number of Orders** | **700** |
| **Average Order Value** | **≈ $2,096** |

## The story the dashboard tells

1. **The West dominates.** West generates **≈ $550K — about 37% of all revenue**, far ahead
   of East (~$312K), Central (~$307K) and South (~$299K), which are tightly bunched. The
   state map makes this obvious: the darkest states (**Oregon, Arizona, Nevada, California**)
   are all in the West.

2. **Technology is the engine — and almost all the profit.** Technology drives
   **≈ $1.0M of revenue (≈ 68%)** and, crucially, **≈ $163K of the ~$176K total profit (≈
   93%)**. Its best sellers are **Accessories, Phones, and Computers**.

3. **Furniture sells but barely earns.** Furniture is the #2 category by revenue (≈ $428K)
   yet contributes only **≈ $5.5K of profit** — a **margin problem**, not a demand problem.
   Discount-heavy furniture orders are eroding the bottom line.

4. **Steady growth with a strong Q4.** Monthly revenue trends **upward through 2024** and
   **peaks in November–December** (holiday season), with a softer first quarter.

5. **Consumers lead.** The **Consumer** segment is the largest revenue source (≈ $735K),
   ahead of Corporate (≈ $460K) and Home Office (≈ $273K).

## Recommendations

- **Invest behind Technology in the West** — the clear revenue *and* profit engine. Prioritise
  stock, staffing, and marketing for the top West states ahead of the **Q4 peak**.
- **Fix Furniture margins.** Review discounting and pricing on Furniture; its high sales but
  near-zero profit is the single biggest margin opportunity. Use the Category drill to inspect
  which products and regions are responsible.
- **Grow the lagging regions.** East, Central, and South each trail the West by ~$240K.
  Identify whether this is coverage, assortment, or demand and target the weakest states.
- **Protect the Q4 momentum** and the Consumer segment, while testing tactics to expand
  Corporate and Home Office.

## How to explore further (in the dashboard)

- Use the **Region** slicer (or **click a region bar**) to drill into a single region — the
  map and every chart re-scale to that region's states.
- Use the **Category** slicer to isolate Furniture and confirm the margin issue
  (compare its revenue bar to its profit contribution).
- Use the **Time Period** slicer (Q1–Q4) to see the seasonal build toward Q4.

*All data is synthetic — no personal data.*
