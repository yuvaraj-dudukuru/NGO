# Day 10 — Capstone: End-to-End Data Analysis

Day 10 connects **every skill from Days 4–9** into complete, real-world data analysis projects.
You take small, deliberately *messy* datasets and carry each through the full professional
workflow: **understand → clean → explore → visualize → query → interpret → report.**

> **For students:** start with the worked **`assessments/`** phases (the teaching material),
> study the demo report, then prove the skill on the **`practice_assessment/`** drills and the
> two portfolio projects (**`assessment_project/`** and **`mini_challenge/`**).

---

## What's in this folder

| # | Folder | What it is | Best for |
|---|--------|-----------|----------|
| 1 | [`assessments/`](assessments/) | The 7 worked teaching phases (RetailMart) | Learning each step in isolation |
| 2 | [`EDA_demo_report/`](EDA_demo_report/) | A finished model EDA report | Seeing the quality target |
| 3 | [`assessment_project/`](assessment_project/) | **FreshBasket** — full graded project (5 deliverables) | Your 1st portfolio project |
| 4 | [`practice_assessment/`](practice_assessment/) | 3 graded drills (beginner → advanced) | Practising end to end |
| 5 | [`mini_challenge/`](mini_challenge/) | **CityCab** — full project challenge (5 deliverables) | Your 2nd portfolio project |

---

## 1. `assessments/` — the worked example (RetailMart)

The seven phases of the professional workflow, each in its own folder with **fully commented,
runnable code** and a **README** explaining *why* each step matters and what output to expect.

| Phase | Folder | Skill (Day) |
|-------|--------|-------------|
| 1 | [`phase1_dataset_understanding/`](assessments/phase1_dataset_understanding/) | Inspect shape, types, summary stats (Day 4) |
| 2 | [`phase2_data_cleaning/`](assessments/phase2_data_cleaning/) | Missing, duplicates, types, outliers (Day 5/6) |
| 3 | [`phase3_eda/`](assessments/phase3_eda/) | Group analysis, correlation (Day 6) |
| 4 | [`phase4_visualization/`](assessments/phase4_visualization/) | Charts with Matplotlib + Seaborn (Day 7/8) |
| 5 | [`phase5_sql_analysis/`](assessments/phase5_sql_analysis/) | SQL on the cleaned data (Day 9) |
| 6 | [`phase6_insight_generation/`](assessments/phase6_insight_generation/) | The Observation→Recommendation ladder (Day 6) |
| 7 | [`phase7_report_writing/`](assessments/phase7_report_writing/) | Structure of a professional report |

```bash
cd assessments/phase1_dataset_understanding
python phase1_dataset_understanding.py
```

> Phases 2–6 each rebuild and re-clean the dataset internally, so **every file runs standalone**.
> Phase 1 keeps the data *raw* on purpose, so you can see the mess before it is fixed.

## 2. `EDA_demo_report/` — the quality target

[`EDA_REPORT_DEMO.md`](EDA_demo_report/EDA_REPORT_DEMO.md) is a finished, eight-section model
report. Read it alongside Phase 7 — it shows the standard your own reports should match.

## 3. `assessment_project/` — FreshBasket (graded project)

The main graded deliverable. A complete analysis of a messy 10-row sales export, producing all
**five submission items**: clean CSV, Jupyter notebook, 8-section report, labelled SQL, and
charts (dpi=300). See its [README](assessment_project/README.md).

## 4. `practice_assessment/` — three graded drills

Ramped practice: [`beginner/`](practice_assessment/beginner/) (5 employees),
[`intermediate/`](practice_assessment/intermediate/) (10 messy orders), and
[`advanced/`](practice_assessment/advanced/) (12-row end-to-end mini project). Attempt each
yourself first, then run the provided solution to check.

## 5. `mini_challenge/` — CityCab (project challenge)

A second full portfolio project on a messy ride-hailing export — same five deliverables. The data
confirms a strong **+0.93** distance↔fare correlation. See its [README](mini_challenge/README.md).

---

## Setup (one time)

```bash
pip install pandas numpy matplotlib seaborn
```
> `sqlite3` ships with Python — no install needed for the SQL phases.

Every Python script uses Matplotlib's `Agg` backend, so charts **save as PNG files even with no
display**. The notebooks (`.ipynb`) are the graded deliverables — run **Restart & Run All** before
submitting.

---

## The Golden Rule

> **Numbers and charts are not insights.** A beginner stops at *"Electronics revenue is highest."*
> A professional climbs to *"Prioritize Electronics stock to protect revenue."* The value of an
> analyst is how high they climb the **insight ladder** — always answer the decision-maker's silent
> question: *"So what should we do?"*
