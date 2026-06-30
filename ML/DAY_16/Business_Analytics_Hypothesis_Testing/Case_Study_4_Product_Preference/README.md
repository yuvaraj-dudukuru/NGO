# Case Study 4 — Product Preference Analysis

**Test type:** Chi-square test of independence — `scipy.stats.chi2_contingency`

## Business context
A company wants to determine whether customers in different regions prefer
different product categories, which would justify region-specific stocking and
marketing.

## Objective
Test whether **region** and **product preference** are related.

## Why this test?
Both variables are **categorical** (region, and preferred product category). The
chi-square test on a contingency table checks whether two categorical variables
are independent or associated.

## Hypotheses
- **H0 (null):** region and product preference are independent.
- **H1 (alternative):** region and product preference are associated (related).
- **Significance level:** alpha = 0.05.

## The data (contingency table)
| Region | Electronics | Clothing | Groceries |
|--------|-------------|----------|-----------|
| North | 50 | 30 | 20 |
| South | 20 | 45 | 35 |
| East | 40 | 25 | 35 |

## How to run
```bash
pip install scipy numpy
python case_study_4_product_preference.py
```

## Result (verified)
| Metric | Value |
|--------|-------|
| Chi-square statistic | ≈ 24.227 |
| Degrees of freedom | 4 |
| p-value | ≈ 0.00007 |
| Verdict | **Significant** |

> **Note:** some printed materials quote `chi-square = 22.107, p = 0.00019` for
> this exact table, but the value `chi2_contingency` actually returns is
> `24.227 / 0.00007`. The verdict (Significant) is the same either way.

## Business interpretation
The p-value is well below 0.05, so the relationship between region and product
preference is statistically significant. Different regions favour different
categories — the North leans toward Electronics, the South toward Clothing, and
the East shows a more balanced pattern.

**Insight:** product preference depends on region.
**Recommendation:** adopt region-specific stocking and marketing — prioritize
Electronics in the North, Clothing in the South, and a balanced assortment in the
East.

> See the parent [README](../README.md) for the full set of case studies.
