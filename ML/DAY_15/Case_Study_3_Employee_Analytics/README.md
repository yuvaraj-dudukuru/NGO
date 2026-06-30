# Business Analytics Case Study 3 — Employee Analytics

## Business context
A Human Resources analyst must examine the relationships among employee
experience, salary, and performance.

## Objective
Compute descriptive statistics and the correlations among employee variables.

## Data
| Experience (yrs) | Salary | Performance |
|------------------|--------|-------------|
| 2  | 35000  | 70 |
| 4  | 45000  | 74 |
| 6  | 55000  | 78 |
| 8  | 68000  | 82 |
| 10 | 80000  | 85 |
| 12 | 95000  | 88 |
| 15 | 110000 | 90 |
| 20 | 140000 | 95 |

## How to run
```bash
pip install pandas
python employee_analytics.py
```

## Code walkthrough
- `emp` — a dataset of employee experience, salary, and performance score.
- `emp.describe()` — produces the full descriptive summary for every numeric column.
- `emp.corr()` — produces the correlation matrix among the three variables.

## Output
```
Descriptive statistics:
       Experience    Salary  Performance
count         8.0       8.0          8.0
mean          9.6   78500.0         82.8
std           6.0   35306.8          8.4
min           2.0   35000.0         70.0
25%           5.5   52500.0         77.0
50%           9.0   74000.0         83.5
75%          12.8   98750.0         88.5
max          20.0  140000.0         95.0

Correlation matrix:
             Experience  Salary  Performance
Experience         1.00    1.00         0.98
Salary             1.00    1.00         0.98
Performance        0.98    0.98         1.00
```

## Business interpretation
- The descriptive statistics show that experience ranges widely (2 to 20 years),
  and salary varies considerably (standard deviation of about 35,000),
  reflecting the seniority spread.
- The correlation matrix reveals **very strong positive relationships** among
  all three variables: experience, salary, and performance rise together.

### Findings
- The organization's compensation structure rewards experience.
- More experienced employees also tend to perform better.

### Recommendation
- Ensure compensation remains aligned with **both** experience and performance.
- Investigate the few employees, if any, whose salary is out of step with their
  experience and performance.

### Caveat — correlation vs. causation
The strong correlation between experience and performance does **not** by itself
prove that experience *causes* better performance, since other factors (such as
training or selection) may contribute.
