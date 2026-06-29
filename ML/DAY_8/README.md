# Day 8 — Statistical Visualization & EDA (Seaborn)

Day 8 builds on Day 7 by using **Seaborn** for statistical charts (box plots,
count plots, heatmaps, regression scatters) to *explore* data — answering
questions by **looking** at well-chosen visuals before drawing conclusions.

---

## What's in this folder

| Item | Type | What it is |
|------|------|-----------|
| [`case_studys/`](case_studys/) | folder | **Three case studies** — each with a commented script + README |
| [`mini_challenge/`](mini_challenge/) | folder | **DineWell** — "what drives bills and tips?" using the Seaborn `tips` dataset |

### Case studies

| # | Folder | Dataset | Focus |
|---|--------|---------|-------|
| 1 | [`case_study_1_titanic/`](case_studys/case_study_1_titanic/) | Titanic | Who survived? Survival by class, sex, age |
| 2 | [`case_study_2_sales/`](case_studys/case_study_2_sales/) | Sales | Revenue patterns and outliers |
| 3 | [`case_study_3_student_performance/`](case_studys/case_study_3_student_performance/) | Students | Marks vs. study hours and subjects |

> Case studies 1 and the mini-challenge load Seaborn's built-in `titanic` / `tips`
> datasets. Seaborn ships these locally, so they work **offline**.

---

## How to Run

Run each script from inside its own folder:

```bash
cd case_studys/case_study_1_titanic
python titanic_analysis.py

cd ../../mini_challenge
python tips_analysis.py
```

These scripts **display charts** with `plt.show()` (the analysis is read off the
charts) and print findings to the terminal.

---

## How to Stop

- Each `plt.show()` **pauses** the script until you **close the chart window**;
  close it to advance to the next chart.
- Press **`Ctrl + C`** to quit immediately.
- For a headless run with **no pop-up windows**, set `MPLBACKEND=Agg` before the
  command (see the [Day 7 README](../DAY_7/README.md#how-to-stop) for the exact
  syntax). Note: these Day 8 scripts mostly *display* rather than save, so a
  headless run simply produces no windows.

---

## Requirements

```bash
pip install pandas matplotlib seaborn
```

> All datasets are **synthetic** or Seaborn's bundled teaching sets — no real
> personal data.
