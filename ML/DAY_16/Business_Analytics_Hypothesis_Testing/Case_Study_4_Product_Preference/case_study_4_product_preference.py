"""
Business Analytics Case Study 4 - Product Preference Analysis
============================================================

Business context:
    A company wishes to determine whether customers in different regions prefer
    different product categories, which would justify region-specific stocking
    and marketing.

Objective:
    Test whether region and product preference are related, using a CHI-SQUARE
    test of independence.

Why a chi-square test of independence?
    Both variables are categorical (region, and preferred product category).
    The chi-square test on a contingency table checks whether the two
    categorical variables are independent or associated.

Hypotheses:
    H0 (null)        : region and product preference are independent
    H1 (alternative) : region and product preference are associated (related)
"""

import numpy as np
from scipy.stats import chi2_contingency

# Contingency table: rows are regions, columns are preferred categories.
# Columns: Electronics, Clothing, Groceries
# Rows:    North, South, East
observed = np.array([
    [50, 30, 20],   # North
    [20, 45, 35],   # South
    [40, 25, 35],   # East
])

chi2, p_value, dof, expected = chi2_contingency(observed)

print("Case Study 4 - Product Preference Analysis")
print("-" * 45)
print("Chi-square statistic:", round(chi2, 3))
print("Degrees of freedom:", dof)
print("p-value:", round(p_value, 5))
print("Significant" if p_value < 0.05 else "Not significant")

# Expected output (verified by running this script):
#   Chi-square statistic: 24.227
#   Degrees of freedom: 4
#   p-value: 0.00007
#   Significant
#
# Note: some materials quote 22.107 / 0.00019 for this table, but the actual
# value returned by chi2_contingency for the array above is 24.227 / 0.00007.
# The verdict (Significant) is the same either way.
#
# Business interpretation:
#   The p-value of 0.00019 is well below 0.05, so the relationship between
#   region and product preference is statistically significant. Different
#   regions favour different categories - the North leans toward Electronics,
#   the South toward Clothing, and the East shows a more balanced pattern.
#   Insight: product preference depends on region.
#   Recommendation: adopt region-specific stocking and marketing - prioritize
#   Electronics in the North, Clothing in the South, and a balanced assortment
#   in the East.
