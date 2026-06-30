"""
Business Analytics Case Study 1 - Marketing Campaign Analysis
=============================================================

Business context:
    A retailer ran a marketing campaign and wishes to know whether it genuinely
    increased weekly sales, or whether the observed increase is ordinary
    fluctuation.

Objective:
    Test whether average weekly sales differ between the periods before and
    after the campaign, using an INDEPENDENT t-test on two separate sets of
    weeks.

Why an independent t-test?
    The "before" weeks and "after" weeks are two distinct, unrelated sets of
    weeks (different observations, not the same week measured twice), so the
    two-sample independent t-test (stats.ttest_ind) is the correct tool.

Hypotheses:
    H0 (null)        : mean(before) == mean(after)  -> no real difference
    H1 (alternative) : mean(before) != mean(after)  -> a real difference exists
"""

from scipy import stats

# Weekly sales (in Rs) before and after the campaign (separate weeks)
before_campaign = [200, 215, 198, 220, 205, 210, 195, 208]
after_campaign = [235, 240, 228, 250, 245, 238, 230, 242]

# Independent t-test, since the two sets of weeks are distinct.
t_stat, p_value = stats.ttest_ind(before_campaign, after_campaign)

before_mean = sum(before_campaign) / len(before_campaign)
after_mean = sum(after_campaign) / len(after_campaign)

print("Case Study 1 - Marketing Campaign Analysis")
print("-" * 45)
print("Average weekly sales before:", round(before_mean, 1))
print("Average weekly sales after :", round(after_mean, 1))
print("t-statistic:", round(t_stat, 4))
print("p-value:", round(p_value, 6))

alpha = 0.05
print("Significant" if p_value < alpha else "Not significant")

# Expected output:
#   p-value: 0.000001
#   Significant
#
# Business interpretation:
#   The p-value is far below 0.05, so the increase in weekly sales after the
#   campaign is statistically significant. Average weekly sales rose from about
#   Rs 206 to about Rs 239, and this increase is very unlikely to be chance.
#   Insight: the campaign genuinely drove higher sales.
#   Recommendation: consider repeating and scaling the campaign, while
#   confirming that the additional revenue exceeds the campaign's cost.
