# `assessments/` — The Seven Worked Phases (RetailMart)

This folder is the **teaching backbone** of the Day 10 capstone
([`../README.md`](../README.md)). It breaks the full professional data-analysis
workflow into **seven phases**, each in its own folder with **fully commented,
runnable code** and a **README** explaining *why* the step matters and what
output to expect.

All phases use the same small, deliberately messy **RetailMart** sales dataset.

---

## The Phases

| Phase | Folder | Skill (from earlier days) |
|-------|--------|---------------------------|
| 1 | [`phase1_dataset_understanding/`](phase1_dataset_understanding/) | Inspect shape, types, summary stats (Day 4) |
| 2 | [`phase2_data_cleaning/`](phase2_data_cleaning/) | Missing values, duplicates, types, outliers (Day 5/6) |
| 3 | [`phase3_eda/`](phase3_eda/) | Group analysis, correlation (Day 6) |
| 4 | [`phase4_visualization/`](phase4_visualization/) | Charts with Matplotlib + Seaborn (Day 7/8) |
| 5 | [`phase5_sql_analysis/`](phase5_sql_analysis/) | SQL on the cleaned data (Day 9) |
| 6 | [`phase6_insight_generation/`](phase6_insight_generation/) | The Observation → Recommendation ladder (Day 6) |
| 7 | [`phase7_report_writing/`](phase7_report_writing/) | Structure of a professional report (README only) |

> **Phases 2–6 each rebuild and re-clean the dataset internally**, so every
> script **runs standalone** — you don't have to run them in order. **Phase 1**
> keeps the data *raw* on purpose, so you can see the mess before it's fixed.
> **Phase 7** is documentation (no script).

---

## How to Run

Run any phase from inside its folder:

```bash
cd phase1_dataset_understanding
python phase1_dataset_understanding.py
```

Phase 4 saves chart PNGs into its own folder; the others print their analysis to
the terminal. Each phase finishes and exits on its own.

To run every phase in sequence:

```bash
# from this assessments/ folder (macOS/Linux/Git Bash)
for d in phase[1-6]_*; do echo "=== $d ==="; (cd "$d" && python *.py); done
```

---

## How to Stop

The scripts complete on their own. Press **`Ctrl + C`** to interrupt any run.
Phase 4 uses Matplotlib's `Agg` backend, so it **saves PNGs without opening
windows** (nothing to close).

---

## Requirements

```bash
pip install pandas numpy matplotlib seaborn
```

> `sqlite3` (used in Phase 5) ships with Python — no install needed. All data is
> **synthetic** sample data — no real personal data.
