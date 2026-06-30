# 🟢 Beginner Assessment

**Task:** Given a small **clean** dataset of 5 employees (`Name`, `Department`, `Salary`):

1. Load it into a DataFrame and print `head()` and `describe()`.
2. Find the **average salary**.
3. Find the **highest-paid employee**.
4. Count employees per department with `value_counts()`.
5. Create a **bar chart** of salary by employee.

## Run

```bash
python beginner_assessment.py
```

## Solution outline

```python
df.describe()
df["Salary"].mean()
df.sort_values("Salary", ascending=False).head(1)
df["Department"].value_counts()
sns.barplot(data=df, x="Name", y="Salary"); plt.show()
```

## Expected results

| Task | Answer |
|------|--------|
| Average salary | **69,600** |
| Highest-paid | **Karan** (Engineering, 95,000) |
| Per department | Sales 2, Engineering 2, HR 1 |
| Chart | `salary_by_employee.png` |

> **Why a bar chart?** It compares one numeric value (salary) across distinct labels (people).
