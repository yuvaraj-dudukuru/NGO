# Data Analytics Track — 20-Day Hands-On Program

A complete, beginner-friendly **Data Analytics learning track** that builds from
plain-Python basics all the way to interactive business-intelligence dashboards.
Each day is a self-contained folder with runnable code, sample data, and its own
README.

The track follows the path a real **data analyst** travels — from first
principles to a portfolio of dashboards:

```
Foundations (Days 1–10)
  Python basics → NumPy → Pandas → Data cleaning → EDA → Visualization → SQL → Capstone

Applied analytics & BI (Days 11–20)
  Advanced Pandas → Feature engineering → SQL databases → SQL capstone → Statistics
  → Hypothesis testing → Time series → Excel reporting → BI dashboards → Dashboard capstone
```

> **Note on data & privacy:** every dataset in this repository is **synthetic**
> (made-up names, cities, and numbers used purely for teaching). It contains **no
> real personal data**. Names such as *Asha, Ravi, Imran, Neha* are fictional
> sample values, not real people.

---

## Day-by-Day Map

### Part 1 — Foundations (Days 1–10)

| Day | Folder | Topic | What you build |
|-----|--------|-------|----------------|
| 1 | [`DAY_1/`](DAY_1/) | Data thinking | A written data-quality review of a messy sales sample (no code — analysis & reasoning) |
| 2 | [`DAY_2/`](DAY_2/) | Python fundamentals | A weekly sales-summary program + six tiny example scripts |
| 3 | [`DAY_3/`](DAY_3/) | NumPy fundamentals | A vectorized student-performance report |
| 4 | [`DAY_4/`](DAY_4/) | Pandas basics (EDA intro) | A job-applicant analysis + four mini dataset demos |
| 5 | [`DAY_5/`](DAY_5/) | Data cleaning & preprocessing | A reusable cleaning pipeline **with unit tests** |
| 6 | [`DAY_6/`](DAY_6/) | Exploratory Data Analysis (EDA) | A full EDA on grocery orders + three case studies |
| 7 | [`DAY_7/`](DAY_7/) | Data visualization (Matplotlib) | Chart dashboards across three case studies + a challenge |
| 8 | [`DAY_8/`](DAY_8/) | Statistical visualization (Seaborn) | EDA-through-charts on Titanic, sales, students, tips |
| 9 | [`DAY_9/`](DAY_9/) | SQL for analysis | `SELECT / WHERE / ORDER BY` case studies + a challenge |
| 10 | [`DAY_10/`](DAY_10/) | Capstone (end-to-end) | Two portfolio projects + 7 worked phases + graded drills |

### Part 2 — Applied analytics & BI (Days 11–20)

| Day | Folder | Topic | What you build |
|-----|--------|-------|----------------|
| 11 | [`DAY_11/`](DAY_11/) | Advanced Pandas | Multi-table joins, pivot tables & crosstabs across 3 case studies + a notebook |
| 12 | [`DAY_12/`](DAY_12/) | Feature engineering | Deriving Revenue/Profit/RFM/tenure features for dashboards (3 case studies + challenge) |
| 13 | [`DAY_13/`](DAY_13/) | SQL databases (SQLite) | `schema → data → queries` projects + running SQL from Python |
| 14 | [`DAY_14/`](DAY_14/) | SQL case study & capstone | UrbanGrocer end-to-end SQL analysis (notebooks + business report) |
| 15 | [`DAY_15/`](DAY_15/) | Statistics | Central tendency, dispersion, correlation, outliers (3 case studies + MetroMart project) |
| 16 | [`DAY_16/`](DAY_16/) | Hypothesis testing | t-tests & chi-square with **SciPy** (4 case studies + GrowthRetail project) |
| 17 | [`DAY_17/`](DAY_17/) | Time-series analysis | Trends, seasonality & rolling metrics (4 case studies + MarketPulse project) |
| 18 | [`DAY_18/`](DAY_18/) | Excel reporting | CSV → multi-sheet **`.xlsx`** reports (3 case studies + RetailEdge project) |
| 19 | [`DAY_19/`](DAY_19/) | BI dashboards (Power BI/Tableau fundamentals) | Interactive **HTML + Chart.js** dashboards with KPIs & slicers |
| 20 | [`DAY_20/`](DAY_20/) | Dashboard capstone | An executive-dashboard portfolio (HTML/Chart.js) + capstone & HR builds |

Each day's README explains the scenario, the files, and how to read the results.

---

## Repository Structure

```
ML/
├── README.md            ← you are here (whole-track overview)
├── DAY_1/ … DAY_20/     ← one folder per day (every folder has its own README)
│   ├── README.md        ← what the day covers + how to run it
│   ├── *.py             ← runnable scripts (Days 2–17)
│   ├── *.ipynb          ← Jupyter notebooks (Days 2, 3, 10–17)
│   ├── *.sql            ← SQL scripts (Days 9, 10, 13)
│   ├── *.csv            ← sample datasets / generated outputs
│   ├── *.xlsx           ← Excel reports (Day 18)
│   ├── *.html + *.js    ← interactive dashboards + vendored Chart.js (Days 19–20)
│   ├── *.png            ← charts produced by the scripts
│   └── requirements.txt ← per-day dependencies (some days)
```

---

## Setup (one time)

You need **Python 3.10+** (developed and tested on Python 3.13). Install the
libraries used across the track:

```bash
# from the ML/ folder
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell/cmd
# source .venv/bin/activate     # macOS/Linux

pip install pandas numpy matplotlib seaborn scipy openpyxl pytest jupyter
```

| Library | Used for | Days |
|---------|----------|------|
| pandas, numpy | the core analysis toolkit | most days |
| matplotlib, seaborn | charts | 7, 8, 11, 17 |
| scipy | hypothesis tests (t-test, chi-square) | 16 |
| openpyxl | reading/writing `.xlsx` | 18 |
| pytest | unit tests | 5 |
| jupyter | running the `.ipynb` notebooks | many |

> `sqlite3` is part of the Python standard library, so the SQL days need **no
> extra install**.
>
> **Node.js** is only needed if you want to *regenerate* the Day 20 dashboard data
> (`generate_data.js`). The dashboards themselves open straight in a browser — no
> Node required to view them.

---

## How to Run Anything

| File type | Command | Notes |
|-----------|---------|-------|
| **Python script** (`.py`) | `python script_name.py` | Run it from inside its own folder so it finds/writes its data and charts in the right place. |
| **Jupyter notebook** (`.ipynb`) | `jupyter notebook file.ipynb` | Use **Kernel → Restart & Run All** to execute every cell top to bottom. |
| **SQL script** (`.sql`) | `sqlite3 :memory: ".read run_all.sql"` (Day 13) · `sqlite3 < file.sql` (Day 9) | Day 9 & 13 scripts are self-contained (they `CREATE` their own tables). Day 13 uses a `run_all.sql` runner that reads `schema.sql → data.sql → queries.sql`. Day 10 `sql_queries.sql` files run against a table loaded from the cleaned CSV. |
| **Excel report** (`.xlsx`) | open in Excel / LibreOffice | Day 18 — generated from the matching `.csv`; each day README explains the steps. |
| **Dashboard** (`.html`) | **double-click to open in a browser** | Days 19–20 — fully offline (Chart.js is vendored in each `lib/`). Use the slicers to filter every chart at once. |
| **Data generators** (`generate_*.py` / `generate_data.js`) | `python …` / `node …` | Rebuild the synthetic datasets. All are **seeded**, so output is identical each run. |
| **Unit tests** (Day 5) | `pytest` | Run from inside `DAY_5/`. |

Example:

```bash
cd DAY_16/Business_Analytics_Hypothesis_Testing/Case_Study_1_Marketing_Campaign
python case_study_1_marketing_campaign.py
```

Python charts are saved with Matplotlib's **`Agg` backend**, so scripts write
`.png` files even on a machine with no display/GUI.

---

## How to Stop a Program

- **A normal script** finishes on its own (it prints output / saves files and
  exits). If one seems stuck, press **`Ctrl + C`** in the terminal to interrupt it.
- **A script that opens a chart window** (`plt.show()`, used in Days 7–8) pauses
  until you **close the chart window**; closing it lets the program finish.
- **A Jupyter notebook** keeps running in the background — stop it with
  **`Ctrl + C`** in the terminal that launched `jupyter`, or use **File → Shut
  Down** in the Jupyter UI.
- **A dashboard** (`.html`) is just a web page — **close the browser tab** to stop it.

---

## Status

Everything in this repository has been executed and verified (Python 3.13):

- ✅ **64/64 Python scripts** run without errors
- ✅ **13/13 notebooks** execute top to bottom
- ✅ **8/8 unit tests** pass (`DAY_5`)
- ✅ SQL scripts run on SQLite (Days 9, 10, 13)
- ✅ Day 18 Excel workbooks load cleanly (openpyxl)
- ✅ Day 19–20 dashboards: every local reference resolves and all JavaScript passes `node --check`
- ✅ All data generators are **seeded** — re-running reproduces identical data
- ✅ Every folder (129 in total) has its own README

*A practical data-analytics curriculum — learn by reading the code, running it,
and reading the result.*
