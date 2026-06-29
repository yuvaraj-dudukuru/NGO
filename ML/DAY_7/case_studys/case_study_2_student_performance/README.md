# Case Study 2 — Student Performance Analysis

## Objective
Turn a small table of student data into a clear **visual report** using two
charts that serve two different purposes:
- **Compare** students against each other.
- **Reveal** a relationship between two numbers.

## The Charts
| # | Chart Type | Question It Answers |
|---|------------|---------------------|
| 1 | **Bar chart**    | Who scored highest / lowest in Math? |
| 2 | **Scatter plot** | Do more study hours lead to higher marks? |

## The Data
| Column | Meaning |
|--------|---------|
| `Name`       | Student's name |
| `Math`       | Math marks (out of 100) |
| `StudyHours` | Hours the student spent studying |

## How to Run
1. Install the required libraries (one time only):
   ```bash
   pip install pandas matplotlib
   ```
2. Run the script:
   ```bash
   python student_performance.py
   ```
3. A window opens with the report, and an image `student_performance.png` is saved
   in the same folder.

## Interpreting the Report
- **Bar chart:** Imran scored highest (92), Divya lowest (45) — instantly
  identifying the top and struggling students.
- **Scatter plot:** The dots rise from bottom-left to top-right — a clear
  **positive relationship** between study hours and marks.

### Insight
> Marks increase with study hours; the lowest scorers studied the least.

### Recommendation
> Encourage more study time, and provide extra support to low-scoring students
> like Divya.

## Key Concepts Practiced
- **Bar chart** for comparing categories (students).
- **Scatter plot** for spotting a relationship between two numeric columns.
- Reading a "positive trend" (bottom-left → top-right) from a scatter plot.
