# Dashboard / Data-Analytics Portfolio — Demo

> A demonstration portfolio that consolidates analytics projects into a single, polished, employer-facing
> page — applying the "Building a Dashboard Portfolio" guidance from Day 20 (Section 29).

## How to view

Open [`index.html`](index.html) in any modern browser. The page is fully self-contained
(HTML + CSS, a few lines of JS) — no install, no build, works offline.

The **Executive Dashboard Suite** section links to the three live, interactive dashboards in the
sibling folders, so the portfolio actually *demonstrates* a published dashboard project rather than
just describing one.

---

## What this demo shows

Section 29 says a portfolio should be a **curated collection of your best, most varied work**, each
project presented to a professional standard. This demo lays out exactly that structure:

| Section | Purpose (per Section 29) |
|---|---|
| **Hero + contact** | Who you are and how to reach you (placeholders to fill in) |
| **Featured Projects** | A varied selection across the analytics workflow |
| **Executive Dashboard Suite** | A *published, interactive* dashboard project (Days 19–20) |
| **Skills** | The toolkit behind the work |
| **Standards** | The professional reporting structure every project follows |

### The varied project mix (Section 29.2)

The demo includes a card for each recommended project type:

1. **End-to-End Analytics Capstone** (Day 10)
2. **SQL Business Investigation** (Day 14)
3. **Statistical Study — Hypothesis Testing & Segmentation** (Days 15–16)
4. **Data Visualization Project** (Days 7–8)
5. **Executive Dashboard Suite** — *featured*, links to the 3 working dashboards (Days 19–20)

### Professional report structure (Sections 29.3 & 29.4)

Each project card follows the same structure of a professional report:

- **Business problem** stated up front
- **Data & approach** described
- **Analysis / visualizations** presented (the dashboards are live)
- **Insight & recommendation** to close

This makes the portfolio understandable *without explanation* — the documentation discipline the
programme emphasises.

---

## Folder structure

```
DAY_20/
├── Dashboard_Portfolio/
│   ├── index.html        ← the portfolio landing page (this demo)
│   └── README.md         ← you are here
├── Case_Study_1_Executive_Sales_Dashboard/        ← linked from the portfolio
├── Case_Study_2_Customer_Intelligence_Dashboard/  ← linked from the portfolio
└── Case_Study_3_Business_Performance_Dashboard/   ← linked from the portfolio
```

> The portfolio links to the case-study dashboards with relative paths (`../Case_Study_…/index.html`),
> so keep this folder beside them for the dashboard links to work.

---

## How to make it your own

1. Replace the placeholder **Name / Email / GitHub / LinkedIn** fields in the hero.
2. Swap the four placeholder project cards (capstone, SQL, statistics, visualization) for links to your
   real notebooks, queries, reports, or hosted projects.
3. Optionally publish the dashboards to **Power BI Service** or **Tableau Public** (Day 19) and point the
   featured links there for interactive, shareable versions.
4. Host the whole folder for free on **GitHub Pages** to get a public portfolio URL.

---

## Data & privacy note

Contact details are **placeholders**, not real values. All numbers in the linked dashboards are
**synthetic sample data**. **No real, proprietary, or personal data is included in this project.**
