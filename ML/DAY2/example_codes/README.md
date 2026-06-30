# Day 2 — Example Codes (Python Fundamentals)

Six tiny, self-contained Python scripts that each teach **one** beginner concept.
They are the building blocks behind the Day 2 mini challenge
([`../README.md`](../README.md) — the ShopSmart weekly sales summary).

Every script ends with a triple-quoted `'''Explanation'''` block that walks
through the logic line by line.

---

## The Files

| File | Concept it teaches | What it does |
|------|--------------------|--------------|
| [`Average_Score.py`](Average_Score.py) | `input()`, `float()`, f-strings | Asks for **three scores** and prints their average |
| [`Sales_Calculations.py`](Sales_Calculations.py) | Variables & arithmetic | Computes revenue, total cost, and profit |
| [`Simple_Discount_Calculator.py`](Simple_Discount_Calculator.py) | Percentages | Applies a 15% discount and prints the final price |
| [`expense_tracking.py`](expense_tracking.py) | Lists + `sum()` | Totals a list of expenses and finds the remaining budget |
| [`student_marks_analysis.py`](student_marks_analysis.py) | `sum()`, `len()`, `max()`, `min()` | Total / average / highest / lowest of a marks list |
| [`temperature_conversion.py`](temperature_conversion.py) | Formula + operator order | Converts Celsius to Fahrenheit |

---

## How to Run

From this folder, run any script with Python:

```bash
python Sales_Calculations.py
```

Most scripts print their result immediately and exit — no input needed.

### The one interactive script

`Average_Score.py` uses `input()`, so it **waits for you to type** three numbers
(press **Enter** after each):

```bash
python Average_Score.py
# Enter score 1: 85
# Enter score 2: 90
# Enter score 3: 78
# Average score: 84.33333333333333
```

You can also feed the answers in without typing interactively:

```bash
printf "85\n90\n78\n" | python Average_Score.py
```

---

## How to Stop

These scripts finish in a fraction of a second on their own. If
`Average_Score.py` is waiting for input and you want to quit instead of typing,
press **`Ctrl + C`** to cancel.

---

## Requirements

**None beyond a standard Python 3 install** — these use only built-in features
(no pandas/numpy).
