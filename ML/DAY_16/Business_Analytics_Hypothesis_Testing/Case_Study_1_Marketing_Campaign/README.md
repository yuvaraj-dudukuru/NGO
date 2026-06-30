# Case Study 1 — Marketing Campaign Analysis

**Test type:** Independent (two-sample) t-test — `scipy.stats.ttest_ind`

## Business context
A retailer ran a marketing campaign and wants to know whether it genuinely
increased weekly sales, or whether the observed increase is ordinary fluctuation.

## Objective
Test whether average weekly sales differ between the periods **before** and
**after** the campaign.

## Why this test?
The "before" weeks and "after" weeks are two **distinct, unrelated** sets of weeks
(different observations, not the same week measured twice), so the independent
two-sample t-test is the correct tool.

## Hypotheses
- **H0 (null):** mean(before) = mean(after) — no real difference.
- **H1 (alternative):** mean(before) ≠ mean(after) — a real difference exists.
- **Significance level:** alpha = 0.05.

## How to run
```bash
pip install scipy
python case_study_1_marketing_campaign.py
```

## Result (verified)
| Metric | Value |
|--------|-------|
| Average weekly sales before | ≈ 206.4 |
| Average weekly sales after | ≈ 238.5 |
| p-value | ≈ 0.000001 |
| Verdict | **Significant** |

## Business interpretation
The p-value is far below 0.05, so the increase in weekly sales after the campaign
is statistically significant. Average weekly sales rose from about ₹206 to about
₹239, and this increase is very unlikely to be chance.

**Insight:** the campaign genuinely drove higher sales.
**Recommendation:** consider repeating and scaling the campaign, while confirming
that the additional revenue exceeds the campaign's cost.

> See the parent [README](../README.md) for the full set of case studies.
