"""
EduTrack — NumPy Performance Report (SOLUTION)
==============================================

A quick student performance report built entirely with NumPy.

Run me with:  python solution.py
"""

import numpy as np

# 1. Store the scores in a NumPy array
scores = np.array([78, 92, 56, 88, 95, 43, 67, 81, 73, 60])
print("Scores:", scores)

# 2. Total, average, highest, lowest
print("Total:", np.sum(scores))
print("Average:", np.mean(scores))
print("Highest:", np.max(scores))
print("Lowest:", np.min(scores))

# 3. Median and standard deviation
print("Median:", np.median(scores))
print("Standard Deviation:", round(np.std(scores), 1))

# 4. Position (index) of the top scorer
print("Top scorer is at index:", np.argmax(scores))

# 5. Boolean indexing — students who passed (score >= 60)
passed = scores[scores >= 60]
print("Passed students (>=60):", passed)

# 6. Count how many passed
print("Number of students who passed:", passed.size)

# 7. Vectorized operation — add 5 grace marks to every score
grace = scores + 5
print("Scores after 5 grace marks:", grace)

# ----------------------------------------------------------------------
# Stretch goals (optional)
# ----------------------------------------------------------------------
print("\n--- Stretch goals ---")

# Pass percentage
pass_percentage = passed.size / scores.size * 100
print("Pass percentage:", pass_percentage, "%")

# Position of the lowest scorer
print("Lowest scorer is at index:", np.argmin(scores))

# Cap grace-mark scores at 100 so no score exceeds 100
grace_capped = np.clip(scores + 5, None, 100)
print("Grace marks capped at 100:", grace_capped)
