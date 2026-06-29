# Day 6 — EDA Case Study Codes

Three standalone **Exploratory Data Analysis (EDA)** case studies. Each takes a
small, realistic dataset and walks the complete EDA workflow:

```
Inspect → Descriptive statistics → Find patterns (groups / correlation)
        → Findings, insights & recommendations
```

They complement the main Day 6 project ([`../README.md`](../README.md) — the
FreshCart grocery EDA). Every script builds its data **in code** (no CSV needed)
and prints a narrated analysis to the terminal.

---

## The Files

| File | Dataset | Key techniques | Headline finding |
|------|---------|----------------|------------------|
| [`case_study_1_student_performance.py`](case_study_1_student_performance.py) | Student marks | `describe()`, per-subject & group analysis | Which subject is strongest/weakest and how spread out scores are |
| [`case_study_2_sales.py`](case_study_2_sales.py) | Regional sales | Engineered `Revenue` column, `groupby` totals, outlier check | Which region/product drives revenue, plus unusually large sales |
| [`case_study_3_employee.py`](case_study_3_employee.py) | Employees | Correlation, department group analysis, salary outliers | The experience↔salary relationship and pay differences by department |

Each script's purpose, workflow, and run command are documented in its own
top-of-file docstring.

---

## How to Run

From this folder, run any case study directly:

```bash
python case_study_1_student_performance.py
```

Each prints its full analysis (statistics → patterns → recommendations) and
exits. They are text-only (no chart windows) and run in well under a second.

Run all three:

```bash
for f in case_study_*.py; do echo "=== $f ==="; python "$f"; done
```

---

## How to Stop

The scripts finish on their own. Press **`Ctrl + C`** to interrupt if needed.

---

## Requirements

```bash
pip install pandas        # or: pip install -r ../requirements.txt
```
