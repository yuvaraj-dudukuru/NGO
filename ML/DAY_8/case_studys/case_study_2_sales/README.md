# Case Study 2 — Sales Dataset 📈

An EDA of a small sales dataset that explores **whether advertising spend
relates to revenue** and **which regions perform best**. Because we build the
data by hand, this case study is perfect for understanding how a `DataFrame`
is constructed and how relationships are measured.

---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `sales_analysis.py` | Fully commented Python script that creates the data and produces every chart below. |
| `README.md` | This file — the explanation and findings. |

---

## ▶️ How to run

1. Install the required libraries (only needed once):
   ```bash
   pip install pandas seaborn matplotlib
   ```
2. Run the script from a terminal:
   ```bash
   python sales_analysis.py
   ```
3. Each chart opens in its own window. **Close a window to see the next one.**
   The correlation value is printed in the terminal.

---

## 📊 The data

We build the dataset by hand with pandas. Each key becomes a column and each
list a column's values (all lists must have the same length — 8 rows here):

| Region | Product | AdSpend | Revenue |
|--------|---------|---------|---------|
| North  | A       | 10      | 120     |
| South  | B       | 15      | 150     |
| East   | A       | 20      | 240     |
| West   | C       | 12      | 130     |
| North  | C       | 25      | 300     |
| South  | A       | 18      | 170     |
| East   | B       | 14      | 160     |
| West   | A       | 30      | 350     |

---

## 🔍 What the script does, step by step

### 1. Relationship — Ad Spend vs Revenue (`scatterplot` + `.corr()`)
A scatter plot places one dot per row at `(AdSpend, Revenue)`, colored by
region. We also print the correlation coefficient.
- **Interpretation:** The dots rise from lower-left to upper-right — a strong
  **positive** relationship. The printed correlation (**~0.96**) confirms it
  numerically: higher ad spend is associated with higher revenue.

### 2. Category comparison — Average Revenue by Region (`barplot`)
Seaborn automatically computes the **mean** revenue for each region.
- **Interpretation:** **West and East** show the highest averages.

### 3. Distribution — Revenue (`boxplot`)
A single-variable box plot shows the spread of all revenue values.
- **Interpretation:** It shows where most revenue sits and flags any unusually
  high value as an **outlier**.

---

## ✅ Findings and recommendations

- Ad spend and revenue are **strongly correlated (~0.96)** — advertising
  *appears* effective.
- **West and East** are the top-performing regions on average.
- **Recommendation:** Consider increasing ad budgets and study what makes West
  and East succeed.

> ⚠️ **Causation caution:** A 0.96 correlation is *not* proof that ads cause
> revenue. Confirm the **causal effect** (e.g. with a controlled test) before
> committing more budget.

---

## 🧠 Concepts practised
Building a `DataFrame` by hand · `scatterplot` · `hue` for grouping ·
`.corr()` · `barplot` (group means) · `boxplot` · correlation-vs-causation
