# Case Study 3 — HR Workforce Dashboard

> **Open [`dashboard.html`](dashboard.html) in your browser to use the interactive dashboard.**

## Business context

A **human resources team** requires a dashboard to monitor the **workforce** — headcount,
performance, tenure, and how these break down by department.

## Dashboard components

1. **Employee KPI cards** — *Total Headcount*, *Average Performance Score*, *Average Tenure*,
   and *High Performers*.
2. **Bar chart of average performance by department** — highest- and lowest-performing
   departments (best highlighted green, lowest red).
3. **Bar chart of headcount by department** — how the workforce is distributed.
4. **Doughnut chart of performance categories** (High / Medium / Low) — the spread of
   performance across the workforce (the classification from Day 12).
5. **Stacked bar of performance category by department** — how each department splits across
   the High/Medium/Low bands.
6. **Slicers** for **Department** and **Performance Category** — every KPI and chart
   re-filters together. A **Reset filters** button clears them.

## How it was constructed

- Imported the workforce data (`data/hr_data.csv`).
- Classified each employee into **High / Medium / Low** by performance score
  (≥80 High, 60–79 Medium, <60 Low).
- Built the KPI cards, the departmental performance & headcount bars, the category doughnut,
  and the category-by-department stacked bar.
- Arranged KPIs on top, charts below, with the slicer bar above; all visuals are linked.

## Data dictionary — `data/hr_data.csv` (320 synthetic employees)

| Column | Description |
|--------|-------------|
| `EmployeeID` | Synthetic employee code (`EMP-001`) |
| `Department` | Engineering, Sales, Marketing, Operations, Finance, HR |
| `PerformanceScore` | Performance score, 0–100 |
| `PerformanceCategory` | High (≥80), Medium (60–79), Low (<60) |
| `TenureYears` | Years with the company |

## Business interpretation (from this synthetic data)

- **Workforce size & quality:** **320** employees, **74.0** average performance score,
  **4.0 years** average tenure.
- **By department:** **Engineering performs best** (avg ~81.4) and has the largest headcount;
  **Operations lags** (avg ~62.2).
- **Performance spread:** most of the workforce sits in the **Medium** band (~52%), with a
  smaller High tier (~35%) and a Low tail (~12%) — the expected centre-weighted distribution.

**Recommendation:** **document and replicate the practices of the top department
(Engineering)** across the organisation, and **support the lagging department (Operations)**
with coaching, clearer goals, or resourcing. Use the slicers to inspect any single
department or to isolate the Low-performance band for targeted intervention.

## Rebuilding this in Power BI / Tableau

1. **Get Data → Text/CSV** and load `data/hr_data.csv`.
2. Measures: `Headcount = COUNTROWS(HR)`,
   `Avg Performance = AVERAGE(PerformanceScore)`,
   `Avg Tenure = AVERAGE(TenureYears)`.
3. **Card** visuals for the KPIs.
4. **Bar chart**: axis = `Department`, value = `Avg Performance`.
5. **Bar chart**: axis = `Department`, value = `Headcount`.
6. **Pie/Doughnut**: legend = `PerformanceCategory`, value = `Headcount`.
7. **Stacked bar**: axis = `Department`, legend = `PerformanceCategory`, value = `Headcount`.
8. **Slicers** for `Department` and `PerformanceCategory`.

*All data is synthetic — no personal data.*
