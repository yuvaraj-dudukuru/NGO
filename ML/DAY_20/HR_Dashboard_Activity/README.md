# Hands-On Activity — Designing an HR Dashboard from Scratch

> A worked example of the Day 20 hands-on activity: designing a professional dashboard step by step,
> from dataset selection to an executive summary. Domain: **HR / workforce analytics** for the fictional
> company **Northwind**. **All data is synthetic — no real, proprietary, or personal data is included.**

## The story in one line

Northwind's **attrition is rising (~25% YTD)** and is concentrated in **Engineering** and among
**early-tenure** employees — the same places where **engagement is lowest** — pointing to an
onboarding/engagement problem in one team.

---

## How to view

1. Open **[`index.html`](index.html)** — the **9-step activity walkthrough** (KPI framework, layout
   wireframe, chart rationale, usability checklist, insights, executive summary).
2. Open **[`dashboard.html`](dashboard.html)** — the **finished interactive dashboard**.

No install. Charts use the Chart.js CDN (internet on first load). The dashboard reads `assets/data.js`,
so it runs straight from a double-click (`file://`) — no server needed.

### Regenerate the dataset (optional)

```bash
node data/generate_data.js
```

Deterministic (seeded) — reproduces the same `data/employees.csv` and `assets/data.js`.

---

## The nine steps → where each lives

| Step | Activity step | Where it is |
|------|---------------|-------------|
| 1 | Select a business dataset | [index.html](index.html) §1 · [employees.csv](data/employees.csv) |
| 2 | Define the objectives | [index.html](index.html) §2 |
| 3 | Create a KPI framework | [index.html](index.html) §3 |
| 4 | Design the dashboard layout | [index.html](index.html) §4 (wireframe) |
| 5 | Build the visualizations | [dashboard.html](dashboard.html) · rationale in §5 |
| 6 | Add filters | [dashboard.html](dashboard.html) slicers · §6 |
| 7 | Test usability | [index.html](index.html) §7 (checklist) |
| 8 | Generate insights | [index.html](index.html) §8 |
| 9 | Create an executive summary | [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) · §9 |

## Deliverables

- 📊 **Dashboard** — [`dashboard.html`](dashboard.html) (6 KPIs, trend, 4 breakdown charts, 4 slicers)
- 🧹 **Cleaned dataset** — [`data/employees.csv`](data/employees.csv)
- 📚 **Data dictionary** — [`data/data_dictionary.md`](data/data_dictionary.md)
- 📝 **Executive summary** — [`EXECUTIVE_SUMMARY.md`](EXECUTIVE_SUMMARY.md)
- ⚙️ **Reproducible generator** — [`data/generate_data.js`](data/generate_data.js)

## Folder structure

```
HR_Dashboard_Activity/
├── index.html                      ← 9-step activity walkthrough (+ live insight charts)
├── dashboard.html                  ← finished interactive dashboard
├── EXECUTIVE_SUMMARY.md            ← insights & recommendations
├── README.md                       ← you are here
├── data/
│   ├── generate_data.js            ← reproducible synthetic-data generator
│   ├── employees.csv               ← cleaned dataset (deliverable)
│   └── data_dictionary.md          ← field definitions
└── assets/
    └── data.js                     ← dataset as JS (loaded by the dashboard & walkthrough)
```

## Dataset at a glance

- **661 employee records**, FY2025 · ~497 active at year-end
- **7 departments** × **4 locations** × **4 tenure bands** × roles & genders
- **164 exits / 101 hires** in 2025 · avg tenure ~4.4 yrs · avg engagement ~3.5/5

---

## Data & privacy note

Every record is **synthetic**, generated locally by a seeded script purely to demonstrate the dashboard
design workflow. `employee_id` values are pseudonymous keys (e.g. `E1042`). **No real, proprietary, or
personal data is contained in this project.**
