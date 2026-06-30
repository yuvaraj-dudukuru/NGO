"""
Business Analytics Case Study 2 - Customer Behaviour Analysis
=============================================================

Business context:
    A company wishes to determine whether its Premium and Regular customer
    segments genuinely differ in their average spending, which would justify
    distinct strategies.

Objective:
    Test whether the two customer segments have significantly different average
    spending, using an INDEPENDENT t-test.

Why an independent t-test?
    Premium and Regular customers are two different groups of people, so the
    two-sample independent t-test (stats.ttest_ind) is appropriate.

Hypotheses:
    H0 (null)        : mean(premium) == mean(regular)
    H1 (alternative) : mean(premium) != mean(regular)
"""

from scipy import stats

# Spending figures (in Rs) for the two segments (different customers).
premium = [45000, 52000, 48000, 60000, 55000, 50000, 58000]
regular = [12000, 15000, 11000, 14000, 13000, 16000, 12500]

t_stat, p_value = stats.ttest_ind(premium, regular)

print("Case Study 2 - Customer Behaviour Analysis")
print("-" * 45)
print("Premium mean:", round(sum(premium) / len(premium), 0))
print("Regular mean:", round(sum(regular) / len(regular), 0))
print("t-statistic:", round(t_stat, 4))
print("p-value:", round(p_value, 8))
print("Significant" if p_value < 0.05 else "Not significant")

# Expected output:
#   Premium mean: 52571.0
#   Regular mean: 13357.0
#   p-value: 0.0
#   Significant
#
# Business interpretation:
#   The p-value is effectively zero, far below 0.05, so the difference in
#   average spending is overwhelmingly significant. Premium customers spend
#   roughly four times as much as Regular customers on average, and this gap is
#   genuine, not chance.
#   Insight: the two segments are fundamentally distinct in value.
#   Recommendation: treat the segments separately - invest in retaining and
#   growing Premium customers and design distinct strategies to migrate Regular
#   customers upward.
