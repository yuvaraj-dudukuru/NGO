# Day 20 — Dashboard Design Principles

A complete, hands-on collection that applies the Day 20 material end to end: three real-world
**case studies**, a **portfolio**, a full **capstone project**, and a guided **hands-on activity** —
each self-contained, interactive, and runnable in any modern browser. **Every figure is synthetic
sample data — no real, proprietary, or personal data is used anywhere.**

---

## What's inside

| Project | What it is | Open this |
|---|---|---|
| 📊 **Case Study 1 — Executive Sales** | Strategic sales dashboard vs targets | [folder](Case_Study_1_Executive_Sales_Dashboard/) → `index.html` |
| 👥 **Case Study 2 — Customer Intelligence** | Customer base, segments & retention | [folder](Case_Study_2_Customer_Intelligence_Dashboard/) → `index.html` |
| 🏢 **Case Study 3 — Business Performance** | Integrated sales + customer + finance | [folder](Case_Study_3_Business_Performance_Dashboard/) → `index.html` |
| 💼 **Dashboard Portfolio** | Employer-facing portfolio of analytics projects | [folder](Dashboard_Portfolio/) → `index.html` |
| 🎓 **Capstone Project** | End-to-end analysis → dashboard → recommendations (GreenCart retail) | [folder](Capstone_Project/) → `index.html` |
| 🧪 **HR Dashboard — Hands-On Activity** | The 9-step design activity, worked (Northwind HR) | [folder](HR_Dashboard_Activity/) → `index.html` |

Each folder has its **own README** with the full business context, design rationale, insights, and
recommendations.

---

## How to run

No installation, no build step.

1. Open any project folder.
2. Double-click **`index.html`** (or right-click → Open with → your browser).
3. Use the **slicers** to filter (region / product / segment / department / period) and watch the
   KPIs and charts update.

> Charts render with [Chart.js](https://www.chartjs.org/) from a public CDN, so an internet connection
> is needed the first time each page loads. The capstone and HR projects load their data from a local
> `assets/data.js` file, so they work fully offline after that.

---

## The three layers of this collection

1. **Apply the principles** — the three **Case Studies** show finished strategic dashboards for three
   audiences (executive sales, marketing, whole-business).
2. **Package the work** — the **Dashboard Portfolio** demonstrates how to present analytics projects to
   employers, and links to the live dashboards as its featured pieces.
3. **Do it from scratch** — the **Capstone** and the **Hands-On Activity** each carry a real business
   problem all the way from a raw, synthetic dataset through cleaning, analysis, KPIs, a built dashboard,
   insights, and an executive summary.

| Project | Domain | The story it tells |
|---|---|---|
| Capstone — GreenCart | E-commerce / retail | Revenue grows but **margin erodes** via discount creep (worst in Electronics & the South) |
| HR Activity — Northwind | HR / workforce | **Attrition is rising**, concentrated in Engineering & early-tenure staff, where engagement is lowest |

---

## Folder structure

```
DAY_20/
├── README.md                                   ← you are here (collection index)
│
├── Case_Study_1_Executive_Sales_Dashboard/
│   ├── index.html                              ← interactive dashboard
│   └── README.md
├── Case_Study_2_Customer_Intelligence_Dashboard/
│   ├── index.html
│   └── README.md
├── Case_Study_3_Business_Performance_Dashboard/
│   ├── index.html
│   └── README.md
│
├── Dashboard_Portfolio/
│   ├── index.html                              ← portfolio landing page (links to the dashboards)
│   └── README.md
│
├── Capstone_Project/
│   ├── index.html                              ← capstone REPORT (9 stages, live KPIs + charts)
│   ├── dashboard.html                          ← interactive dashboard (centrepiece)
│   ├── INSIGHTS_AND_RECOMMENDATIONS.md
│   ├── README.md
│   ├── data/  (generate_data.js · sales_clean.csv · data_dictionary.md)
│   ├── analysis/methodology.md
│   └── assets/data.js
│
└── HR_Dashboard_Activity/
    ├── index.html                              ← 9-step activity walkthrough
    ├── dashboard.html                          ← finished interactive dashboard
    ├── EXECUTIVE_SUMMARY.md
    ├── README.md
    ├── data/  (generate_data.js · employees.csv · data_dictionary.md)
    └── assets/data.js
```

> The **Dashboard Portfolio** links to the three case-study dashboards with relative paths, so keep these
> folders side by side for those links to work.

### Regenerating the datasets (Capstone & HR only)

Both data-driven projects ship a reproducible, seeded generator:

```bash
node Capstone_Project/data/generate_data.js
node HR_Dashboard_Activity/data/generate_data.js
```

---

## Design principles demonstrated throughout

- **Prominent KPIs** — the most important numbers lead, as large cards.
- **Clear visual hierarchy** — headline metrics first, then supporting detail.
- **Fit-for-purpose charts** — lines for trends, bars for comparison, doughnut for composition, combo for two measures.
- **Disciplined layout** — a consistent grid with generous whitespace.
- **Conventional colour** — green = good / on target, red = problem, neutral blues/indigo elsewhere.
- **A story** — each dashboard leads from headline performance to its underlying causes.
- **Focus through interaction** — slicers let the user explore without clutter.

---

## Data & privacy note

Every figure across this collection is **synthetic**, generated purely to demonstrate dashboard design.
Some series (a declining region, a high-value minority segment, a high-attrition team) are deliberately
modelled so each project can tell a complete analytical story. IDs are pseudonymous keys
(e.g. `C0231`, `E1042`). **No real, proprietary, or personal data — and no personal contact details —
are contained in this project.**
