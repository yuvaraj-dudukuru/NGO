# Capstone Project — GreenCart Profitability Analysis & Dashboard

> The culminating, end-to-end project for Day 20: a complete data-analysis-and-dashboard piece
> carried from raw data to a polished, decision-driving dashboard with documented recommendations.
> **All data is synthetic — no real, proprietary, or personal data is included.**

## The story in one line

GreenCart's **revenue is growing but profit margin is eroding** (~27% → ~19% across FY2025),
driven by **discount creep** — worst in thin-margin **Electronics** and the **South** region — while
the **Premium** segment remains a high-value bright spot.

---

## How to view

1. Open **[`index.html`](index.html)** — the full capstone **report** (all 9 stages, live KPIs, charts).
2. Open **[`dashboard.html`](dashboard.html)** — the interactive **dashboard** (the centrepiece).

No install needed. Charts use the Chart.js CDN (internet on first load). The dashboard reads its
data from `assets/data.js`, so it works directly from `file://` with no server.

### Regenerate the dataset (optional)

```bash
node data/generate_data.js
```

Deterministic (seeded), so it reproduces the same `data/sales_clean.csv` and `assets/data.js`.

---

## The nine required stages → where each lives

| # | Stage | Where it is |
|---|-------|-------------|
| 1 | Define the business problem | [index.html](index.html) §1 · [methodology](analysis/methodology.md) |
| 2 | Select the dataset | [data/sales_clean.csv](data/sales_clean.csv) · [data dictionary](data/data_dictionary.md) |
| 3 | Clean the data | [methodology](analysis/methodology.md) §3 · [generate_data.js](data/generate_data.js) |
| 4 | Analyze the data | [index.html](index.html) §4 (charts) |
| 5 | Create KPIs | [index.html](index.html) §5 (computed live) |
| 6 | Design the dashboard | [dashboard.html](dashboard.html) |
| 7 | Generate insights | [INSIGHTS_AND_RECOMMENDATIONS.md](INSIGHTS_AND_RECOMMENDATIONS.md) |
| 8 | Create recommendations | [INSIGHTS_AND_RECOMMENDATIONS.md](INSIGHTS_AND_RECOMMENDATIONS.md) |
| 9 | Present the findings | [index.html](index.html) (report) + dashboard |

## The deliverables (Section 30.3)

- 📄 **Documented analysis / report** — [`index.html`](index.html)
- 🧹 **Cleaned dataset** — [`data/sales_clean.csv`](data/sales_clean.csv)
- 📈 **Computed KPIs** — shown live in the report and dashboard
- 📊 **Professional dashboard** — [`dashboard.html`](dashboard.html)
- 📝 **Written insights & recommendations** — [`INSIGHTS_AND_RECOMMENDATIONS.md`](INSIGHTS_AND_RECOMMENDATIONS.md)
- 🔬 **Methodology** — [`analysis/methodology.md`](analysis/methodology.md)
- 📚 **Data dictionary** — [`data/data_dictionary.md`](data/data_dictionary.md)

## Folder structure

```
Capstone_Project/
├── index.html                          ← capstone REPORT (9 stages, live KPIs + charts)
├── dashboard.html                      ← interactive DASHBOARD (centrepiece)
├── INSIGHTS_AND_RECOMMENDATIONS.md     ← standalone executive summary
├── README.md                           ← you are here
├── data/
│   ├── generate_data.js                ← reproducible synthetic-data generator
│   ├── sales_clean.csv                 ← cleaned dataset (deliverable)
│   └── data_dictionary.md              ← field definitions
├── analysis/
│   └── methodology.md                  ← cleaning & analysis write-up
└── assets/
    └── data.js                         ← dataset as JS (loaded by the dashboard/report)
```

## Dataset at a glance

- **3,617 orders**, FY2025, ~880 customers
- **4 regions** × **5 categories** × **3 segments**
- **Total revenue ≈ $1.36M**, profit ≈ $315K, overall margin ≈ 23%

---

## Data & privacy note

Every figure is **synthetic**, generated locally by a seeded script purely to demonstrate the
end-to-end analyst workflow. `customer_id` values are pseudonymous keys (e.g. `C0231`).
**No real, proprietary, or personal data is contained in this project.**
