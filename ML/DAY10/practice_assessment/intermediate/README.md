# 🟡 Intermediate Assessment

**Task:** Given a **messy** dataset of 10 orders (1 missing amount, 1 duplicate, inconsistent
city case):

1. **Detect and report** all data-quality issues.
2. **Clean** the dataset (missing, duplicate, text).
3. Compute **total revenue by city** with `groupby()`.
4. Create a **histogram** of amounts and a **box plot** by city.
5. Write **three findings**.

## Run

```bash
python intermediate_assessment.py
```

## Solution outline

```python
df.isnull().sum(); df.duplicated().sum(); df["City"].value_counts()
df = df.drop_duplicates(subset=["OrderID"])
df["City"] = df["City"].str.strip().str.title()
df["Amount"] = df["Amount"].fillna(df["Amount"].median())
df.groupby("City")["Amount"].sum()
sns.histplot(df["Amount"]); sns.boxplot(data=df, x="City", y="Amount")
```

## The three issues to detect

| Issue | How to find it | Fix |
|-------|----------------|-----|
| Missing amount | `df.isnull().sum()` | `fillna(median)` |
| Duplicate (OrderID 305) | `df.duplicated(subset=["OrderID"])` | `drop_duplicates(subset=["OrderID"])` |
| Mixed-case cities | `df["City"].value_counts()` | `.str.strip().str.title()` |

## Charts produced

- `amount_histogram.png` — distribution of order amounts
- `amount_by_city_box.png` — spread of amounts per city

> **Teaching point:** before cleaning, the cities *look* unbalanced — but that's a **text
> problem** (`mumbai` vs `Mumbai`), not a real one. After `.str.title()`, each city has 3
> orders. Always standardize text *before* you trust a `value_counts()`.
