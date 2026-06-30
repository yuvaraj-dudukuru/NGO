# Case Study 2 — Customer Behaviour Analysis

**Test type:** Independent (two-sample) t-test — `scipy.stats.ttest_ind`

## Business context
A company wants to determine whether its **Premium** and **Regular** customer
segments genuinely differ in their average spending, which would justify distinct
strategies.

## Objective
Test whether the two customer segments have significantly different average
spending.

## Why this test?
Premium and Regular customers are two **different groups** of people, so the
independent two-sample t-test is appropriate.

## Hypotheses
- **H0 (null):** mean(premium) = mean(regular).
- **H1 (alternative):** mean(premium) ≠ mean(regular).
- **Significance level:** alpha = 0.05.

## How to run
```bash
pip install scipy
python case_study_2_customer_behaviour.py
```

## Result (verified)
| Metric | Value |
|--------|-------|
| Premium mean | ≈ ₹52,571 |
| Regular mean | ≈ ₹13,357 |
| p-value | ≈ 0.0 |
| Verdict | **Significant** |

## Business interpretation
The p-value is effectively zero, far below 0.05, so the difference in average
spending is overwhelmingly significant. Premium customers spend roughly **four
times** as much as Regular customers on average, and this gap is genuine, not
chance.

**Insight:** the two segments are fundamentally distinct in value.
**Recommendation:** treat the segments separately — invest in retaining and
growing Premium customers, and design distinct strategies to migrate Regular
customers upward.

> See the parent [README](../README.md) for the full set of case studies.
