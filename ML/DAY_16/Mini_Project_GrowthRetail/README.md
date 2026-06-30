# Mini Project — GrowthRetail Hypothesis-Testing Analysis

A complete, evidence-based hypothesis-testing analysis carried out from the
perspective of a **data analyst at GrowthRetail**. The company recently introduced
a **new loyalty programme** and a **regional product strategy**, and management
needs **statistical validation** that these changes produced genuine effects
before scaling them.

The project translates three distinct business questions into formal hypotheses,
selects and justifies the correct test for each, runs the tests in Python with
SciPy, interprets the p-values, and produces evidence-based recommendations.

---

## The three scenarios

| # | Scenario | Comparison | Test | Why |
|---|----------|-----------|------|-----|
| 1 | **Loyalty programme** | Same customers, before vs after | **Paired t-test** (`ttest_rel`) | The same customers are measured twice, so the values are naturally paired. |
| 2 | **Two-store sales** | Two separate stores | **Independent t-test** (`ttest_ind`) | Two unrelated groups of days with no natural pairing. |
| 3 | **Region vs preference** | Two categorical variables | **Chi-square test** (`chi2_contingency`) | Tests association between two categorical variables. |

Choosing the right test is the core skill the project demonstrates: a paired test
for repeated measures on the same subjects, an independent test for two separate
groups, and a chi-square test for a relationship between categorical variables.

---

## The workflow (applied to every scenario)

1. **Formulate the hypotheses** — null (H0) and alternative (H1).
2. **Select and justify the test** — by data type and comparison.
3. **Perform the test** — in Python using SciPy.
4. **Interpret the p-value** — against a significance level of `alpha = 0.05`.
5. **Decide and recommend** — reject / fail to reject H0, then a business action.

Decision rule: `p < 0.05` → **reject H0** (significant); `p ≥ 0.05` → **fail to
reject H0** (not significant).

---

## Hypotheses at a glance

**Scenario 1 — Loyalty programme**
- H0: mean spending after = mean spending before (no change).
- H1: mean spending after ≠ mean spending before.

**Scenario 2 — Two-store sales**
- H0: mean daily sales of Store A = mean daily sales of Store B.
- H1: the two stores' mean daily sales differ.

**Scenario 3 — Region vs preference**
- H0: region and preferred category are independent.
- H1: region and preferred category are associated.

---

## The data

Realistic sample data lives in the `data/` folder and is loaded with pandas:

| File | Shape | Contents |
|------|-------|----------|
| `data/loyalty_spending.csv` | 12 customers | `customer_id, before, after` monthly spending |
| `data/store_daily_sales.csv` | 14 days | `day, store_a, store_b` daily sales |
| `data/region_preference.csv` | 3×3 | contingency table of region × preferred category |

The data is constructed so that **all three scenarios produce significant
results** (the brief requires at least two of three).

---

## Results (verified by running the notebook)

| Scenario | Key figures | Statistic | p-value | Decision |
|----------|-------------|-----------|---------|----------|
| 1. Loyalty programme | ₹2,742 → ₹3,108 (+₹367/customer) | t ≈ −32.63 | ≈ 2.7e-12 | **Reject H0 — Significant** |
| 2. Two-store sales | A ≈ ₹1,533 vs B ≈ ₹1,366 | t ≈ 13.70 | ≈ 2.1e-13 | **Reject H0 — Significant** |
| 3. Region vs preference | χ² with dof = 4 | χ² ≈ 49.60 | ≈ 4.4e-10 | **Reject H0 — Significant** |

### Recommendations
1. **Loyalty programme genuinely increased spending** → expand it, after
   confirming the extra revenue exceeds the programme's cost.
2. **The two stores differ significantly** → investigate what drives Store A's
   stronger sales and replicate those practices at Store B.
3. **Region and preference are related** → adopt a region-specific stocking and
   marketing strategy instead of one national plan.

> **Honest reporting:** statistical significance confirms an effect is *real*, not
> how *large* or *commercially worthwhile* it is. Pair every p-value with effect
> size and a cost/benefit view, and don't claim causation beyond what the data
> supports.

---

## Requirements

```bash
pip install scipy numpy pandas jupyter
```

## How to run

Open the notebook and run all cells (it reads the CSVs in `data/`):

```bash
jupyter notebook growthretail_hypothesis_testing.ipynb
```

Or execute it headless from this folder:

```bash
python -m nbconvert --to notebook --execute --inplace growthretail_hypothesis_testing.ipynb
```

The notebook ships with its outputs already executed and embedded.

---

## Folder structure

```
Mini_Project_GrowthRetail/
├── README.md
├── growthretail_hypothesis_testing.ipynb   # full analysis: 3 scenarios + summary
└── data/
    ├── loyalty_spending.csv                 # paired before/after (Scenario 1)
    ├── store_daily_sales.csv                # two stores' daily sales (Scenario 2)
    └── region_preference.csv                # region × preference table (Scenario 3)
```
