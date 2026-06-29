# Day 7 — Data Visualization with Matplotlib

Day 7 turns numbers into **charts that tell a story**. Using Pandas + Matplotlib,
you load small business datasets, summarize them, and choose the right chart
(line, bar, histogram, scatter, pie) to answer real questions.

---

## What's in this folder

| Item | Type | What it is |
|------|------|-----------|
| [`case_studys/`](case_studys/) | folder | **Three guided case studies** (sales dashboard, student performance, customer analysis), each with its own script + README |
| [`mini_challenge/`](mini_challenge/) | folder | **TrendMart** — a self-directed visual performance report |
| `*.png` (this folder) | images | Rendered sample charts produced by the case-study / challenge scripts, kept here as ready-to-view outputs |

The PNG files at the root (`sales_dashboard.png`, `student_performance.png`,
`customer_analysis.png`, `trendmart_dashboard.png`, `trendmart_region_share.png`,
`trendmart_revenue_vs_adspend.png`) are example outputs so you can see the
results without running anything.

---

## How to Run

Each script lives in its own subfolder and is meant to be run **from that
folder** (it reads/writes using relative paths):

```bash
# a case study
cd case_studys/case_study_1_sales_dashboard
python sales_dashboard.py

# the mini challenge
cd ../../mini_challenge
python trendmart_analysis.py
```

A script will **open a chart window** (`plt.show()`) and also **save a `.png`**
of the figure in the folder it is run from. See each subfolder's README for the
exact charts and how to read them.

---

## How to Stop

- A script **pauses on each `plt.show()`** until you **close the chart window** —
  closing it lets the program continue to the next chart and then finish.
- To quit immediately, press **`Ctrl + C`** in the terminal.
- To run without any pop-up windows (just save the PNGs), set the headless
  backend first:

  ```bash
  # macOS/Linux/Git Bash
  MPLBACKEND=Agg python sales_dashboard.py
  ```
  ```powershell
  # Windows PowerShell
  $env:MPLBACKEND="Agg"; python sales_dashboard.py
  ```

---

## Requirements

```bash
pip install pandas matplotlib
```

> Datasets are **synthetic** sample data — no real personal data.
