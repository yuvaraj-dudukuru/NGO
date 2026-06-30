# =============================================================================
# CASE STUDY 2 — STUDENT PERFORMANCE ANALYSIS
# =============================================================================
# GOAL:
#   Turn a small table of student data into a simple "visual report" with TWO
#   charts:
#       1. A BAR     chart -> compares Math marks across students
#                             (who is the topper, who is struggling?)
#       2. A SCATTER plot  -> checks whether more STUDY HOURS lead to higher MARKS
#                             (is there a relationship between the two?)
#
#   This shows two very different uses of charts:
#       - Bar chart  = COMPARE individual categories (students).
#       - Scatter    = REVEAL a relationship between two numeric columns.
# =============================================================================


# -----------------------------------------------------------------------------
# STEP 1: Import the libraries
# -----------------------------------------------------------------------------
import pandas as pd               # for the data table (DataFrame)
import matplotlib.pyplot as plt   # for drawing the charts


# -----------------------------------------------------------------------------
# STEP 2: Create the data
# -----------------------------------------------------------------------------
# Each student has:
#   - a Name
#   - a Math mark (out of 100)
#   - the number of hours they studied
# All three lists are the same length (6 students), so the rows line up.
students = pd.DataFrame({
    "Name":       ["Asha", "Ravi", "Imran", "Divya", "Karan", "Meena"],
    "Math":       [85, 60, 92, 45, 78, 55],   # Math marks
    "StudyHours": [6, 3, 8, 2, 5, 3]          # hours spent studying
})

# Print the table so we can see exactly what we are working with.
print("Student data:")
print(students)
print()


# -----------------------------------------------------------------------------
# STEP 3: Create the report layout
# -----------------------------------------------------------------------------
# plt.subplots(1, 2) -> one row with TWO charts: axes[0] and axes[1].
# figsize=(12, 4) makes the figure wide enough to comfortably hold both.
fig, axes = plt.subplots(1, 2, figsize=(12, 4))


# -----------------------------------------------------------------------------
# CHART 1: Bar chart of Math marks per student  (axes[0])
# -----------------------------------------------------------------------------
# A bar chart is perfect for COMPARING a value across named categories.
# Here each student (a category) gets one bar whose height is their Math mark.
axes[0].bar(students["Name"], students["Math"], color="skyblue")
axes[0].set_title("Math Marks by Student")
axes[0].set_xlabel("Student")
axes[0].set_ylabel("Marks")


# -----------------------------------------------------------------------------
# CHART 2: Scatter plot of Study Hours vs Math marks  (axes[1])
# -----------------------------------------------------------------------------
# A scatter plot draws one DOT per student at the position (StudyHours, Math).
# If the dots trend from bottom-left to top-right, more study hours generally
# go together with higher marks -> a POSITIVE relationship.
axes[1].scatter(students["StudyHours"], students["Math"], color="darkred")
axes[1].set_title("Study Hours vs Marks")
axes[1].set_xlabel("Study Hours")
axes[1].set_ylabel("Math Marks")


# -----------------------------------------------------------------------------
# STEP 4: Finish and show the report
# -----------------------------------------------------------------------------
plt.tight_layout()                          # keep labels from overlapping
plt.savefig("student_performance.png", dpi=150)  # save a copy as an image
plt.show()                                  # display the figure


# -----------------------------------------------------------------------------
# STEP 5: Interpret the results
# -----------------------------------------------------------------------------
print("INTERPRETATION")
print("- Bar chart : Imran scored highest (92); Divya lowest (45).")
print("- Scatter   : Dots rise from bottom-left to top-right ->")
print("              a clear positive link between study hours and marks.")
print()
print("INSIGHT:")
print("  Marks increase with study hours; the lowest scorers studied the least.")
print()
print("RECOMMENDATION:")
print("  Encourage more study time, and give extra support to low-scoring")
print("  students like Divya.")
