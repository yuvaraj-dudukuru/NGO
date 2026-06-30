# Case Study 3 — Employee Performance Analysis

**Test type:** Paired t-test — `scipy.stats.ttest_rel`

## Business context
An organization implemented a productivity initiative and wants to determine
whether it genuinely improved the performance of its employees.

## Objective
Test whether the **same** employees' performance improved after the initiative.

## Why this test?
The same ten employees are measured **twice** (before and after). Each "after"
score is naturally paired with that same employee's "before" score, so the
**paired** t-test is correct. By comparing each employee with their own earlier
score, it isolates the initiative's effect from the natural differences between
people.

## Hypotheses
- **H0 (null):** mean difference (after − before) = 0.
- **H1 (alternative):** mean difference (after − before) ≠ 0.
- **Significance level:** alpha = 0.05.

## How to run
```bash
pip install scipy
python case_study_3_employee_performance.py
```

## Result (verified)
| Metric | Value |
|--------|-------|
| Average before | 71.5 |
| Average after | 76.8 |
| p-value | ≈ 0.00000003 |
| Verdict | **Significant** |

## Business interpretation
The p-value is far below 0.05, so the improvement after the initiative is
statistically significant. Average performance rose from 71.5 to 76.8, and this is
very unlikely to be chance.

**Insight:** the productivity initiative genuinely improved performance.
**Recommendation:** continue and expand the initiative, while monitoring whether
the improvement is sustained over time.

> See the parent [README](../README.md) for the full set of case studies.
