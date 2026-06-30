"""
Business Analytics Case Study 3 - Employee Performance Analysis
==============================================================

Business context:
    An organization implemented a productivity initiative and wishes to
    determine whether it genuinely improved the performance of its employees.

Objective:
    Test whether the SAME employees' performance improved after the initiative,
    using a PAIRED t-test.

Why a paired t-test?
    The same ten employees are measured twice (before and after). Each "after"
    score is naturally paired with that same employee's "before" score, so the
    paired t-test (stats.ttest_rel) is the correct choice. By comparing each
    employee with their own earlier score, it isolates the effect of the
    initiative from the natural differences between employees.

Hypotheses:
    H0 (null)        : mean difference (after - before) == 0
    H1 (alternative) : mean difference (after - before) != 0
"""

from scipy import stats

# Performance scores for the SAME employees, before and after the initiative.
before = [72, 68, 75, 70, 65, 78, 74, 69, 71, 73]
after = [78, 74, 80, 77, 70, 82, 79, 73, 76, 79]

t_stat, p_value = stats.ttest_rel(before, after)

print("Case Study 3 - Employee Performance Analysis")
print("-" * 45)
print("Average before:", round(sum(before) / len(before), 1))
print("Average after: ", round(sum(after) / len(after), 1))
print("t-statistic:", round(t_stat, 4))
print("p-value:", round(p_value, 8))
print("Significant" if p_value < 0.05 else "Not significant")

# Expected output:
#   Average before: 71.5
#   Average after:  76.8
#   p-value: 0.00000003
#   Significant
#
# Business interpretation:
#   The p-value is far below 0.05, so the improvement after the initiative is
#   statistically significant. Average performance rose from 71.5 to 76.8, and
#   this is very unlikely to be chance.
#   Insight: the productivity initiative genuinely improved performance.
#   Recommendation: continue and expand the initiative, while monitoring
#   whether the improvement is sustained over time.
