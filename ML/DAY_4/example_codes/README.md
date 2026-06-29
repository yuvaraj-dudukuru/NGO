# Day 4 — Example Codes (Pandas Basics)

Four small **Pandas** demos that introduce the everyday analyst toolkit:
building a `DataFrame`, filtering rows, adding computed columns, sorting, and
grouping. They support the Day 4 mini-project
([`../README.md`](../README.md) — the TechHire applicant analysis).

Each script builds its data **in code** (no external CSV needed) and ends with a
triple-quoted `'''Explanation'''` block.

---

## The Files

| File | Pandas skills | What it answers |
|------|---------------|-----------------|
| [`Customer_Dataset.py`](Customer_Dataset.py) | Boolean filtering, `value_counts()` | Who are the high-value customers? How many customers per city? |
| [`Employee_Dataset.py`](Employee_Dataset.py) | `groupby().mean()`, `sort_values()` | Average salary per department; the single highest-paid employee |
| [`Sales_Dataset.py`](Sales_Dataset.py) | Computed columns, `groupby().sum()` | Revenue per row, total revenue, units sold per product |
| [`Student_Performance_Dataset.py`](Student_Performance_Dataset.py) | Vectorized columns, `sort_values().head()` | Per-student total/average, class average, top scorer |

---

## How to Run

From this folder:

```bash
python Sales_Dataset.py
```

Each script prints its tables and summaries to the terminal and exits. They run
in well under a second and need no input.

To run all four in sequence:

```bash
for f in *.py; do echo "=== $f ==="; python "$f"; done   # macOS/Linux/Git Bash
```

---

## How to Stop

The scripts finish on their own. If you ever need to interrupt one, press
**`Ctrl + C`** in the terminal.

---

## Requirements

```bash
pip install pandas
```

(Installed once for the whole track — see the [top-level README](../../README.md).)
