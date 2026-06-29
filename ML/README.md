# Data Analytics Track — 10-Day Hands-On Program

A complete, beginner-friendly **Data Analytics learning track** that builds from
plain-Python basics all the way to an end-to-end capstone analysis. Each day is a
self-contained folder with runnable code, sample data, and its own README.

The track follows the path a real **junior data analyst** takes on the job:

```
Python basics → NumPy → Pandas → Data cleaning → EDA → Visualization → SQL → Capstone
```

> **Note on data & privacy:** every dataset in this repository is **synthetic**
> (made-up names, cities, and numbers used purely for teaching). It contains **no
> real personal data**. Names such as *Asha, Ravi, Imran, Neha* are fictional
> sample values, not real people.

---

## Day-by-Day Map

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

Each day's README explains the scenario, the files, and how to read the results.

---

## Repository Structure

```
ML/
├── README.md            ← you are here (whole-track overview)
├── DAY_1/ … DAY_10/     ← one folder per day (each has its own README)
│   ├── README.md        ← what the day covers + how to run it
│   ├── *.py             ← runnable scripts
│   ├── *.ipynb          ← Jupyter notebooks (Days 2, 3, 10)
│   ├── *.sql            ← SQL scripts (Day 9, 10)
│   ├── *.csv            ← sample datasets / generated outputs
│   ├── *.png            ← charts produced by the scripts
│   └── requirements.txt ← per-day dependencies (Days 3–6)
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

pip install pandas numpy matplotlib seaborn pytest jupyter
```

> `sqlite3` is part of the Python standard library, so the SQL days need **no
> extra install**.
>
> Some days ship a `requirements.txt` — you can instead run
> `pip install -r DAY_x/requirements.txt` for just that day.

---

## How to Run Anything

| File type | Command | Notes |
|-----------|---------|-------|
| **Python script** (`.py`) | `python script_name.py` | Run it from inside its own folder so it finds/writes its data and charts in the right place. |
| **Jupyter notebook** (`.ipynb`) | `jupyter notebook file.ipynb` | Use **Kernel → Restart & Run All** to execute every cell top to bottom. |
| **SQL script** (`.sql`) | `sqlite3 < file.sql` or run inside Python via `sqlite3` | Day 9 scripts are self-contained (they `CREATE` their own tables). Day 10 `sql_queries.sql` files run against a table loaded from the cleaned CSV (see that folder's README). |
| **Unit tests** (Day 5) | `pytest` | Run from inside `DAY_5/`. |

Example:

```bash
cd DAY_6
python eda_freshcart.py
```

Charts are saved with Matplotlib's **`Agg` backend**, so the scripts write `.png`
files even on a machine with no display/GUI.

---

## How to Stop a Program

- **A normal script** finishes on its own (it prints output / saves files and
  exits). If one seems stuck, press **`Ctrl + C`** in the terminal to interrupt it.
- **A script that opens a chart window** (`plt.show()`) pauses until you **close
  the chart window**; closing it lets the program continue/finish.
- **A Jupyter notebook** keeps running in the background — stop it with
  **`Ctrl + C`** in the terminal that launched `jupyter`, or use **File → Shut
  Down** in the Jupyter UI.

---

## Status

All programs in this repository have been executed and verified:

- ✅ 39/39 Python scripts run without errors
- ✅ 8/8 unit tests pass (`DAY_5`)
- ✅ 4/4 notebooks execute top to bottom
- ✅ SQL scripts run on SQLite

*A practical data-analytics curriculum — learn by reading the code, running it,
and reading the result.*
