# Practice Assessments

Three graded practice assessments, ramping from beginner to advanced. **Attempt each fully on
your own first**, then run the provided solution and check your work against it.

| Level | Folder | Skills tested |
|-------|--------|---------------|
| 🟢 Beginner | [`beginner/`](beginner/) | Load, describe, mean, max, `value_counts()`, a bar chart |
| 🟡 Intermediate | [`intermediate/`](intermediate/) | Detect issues, clean, `groupby()`, histogram + box plot, findings |
| 🔴 Advanced | [`advanced/`](advanced/) | Full end-to-end mini project (clean → EDA → viz → SQL → insights → report) |

## Setup

```bash
pip install pandas numpy matplotlib seaborn      # sqlite3 ships with Python
```

## How to use each folder

1. Read the **README.md** — it states the task and the expected output.
2. Try to write the code yourself.
3. Run the provided `*.py` solution and compare:
   ```bash
   cd beginner
   python beginner_assessment.py
   ```
4. Charts are saved as PNG files in each folder (the scripts use Matplotlib's `Agg` backend so
   they work without a display).

> **The goal isn't just running code — it's climbing the insight ladder.** A beginner stops at
> *"Sales are highest in X."* A professional reaches *"...so we should do Y."*
