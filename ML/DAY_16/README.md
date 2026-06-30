# Day 16 — Hypothesis Testing Basics

A complete, hands-on collection of business-analytics materials on **hypothesis
testing** — turning "it looks like the number moved" into a statistically
defensible decision. Everything here uses Python with **SciPy** and follows the
same disciplined workflow: state the hypotheses, pick the right test, compute a
p-value, and decide against a significance level of `alpha = 0.05`.

The material is organised into **three top-level deliverables**, each in its own
dedicated folder with its own README.

---

## Contents

| Folder | What it is | Format | Tests used |
|--------|-----------|--------|-----------|
| [Business_Analytics_Hypothesis_Testing/](Business_Analytics_Hypothesis_Testing/) | Four worked **case studies**, each in its own subfolder | Python scripts | Independent t-test, paired t-test, chi-square |
| [Day16_Hands_On_Activity/](Day16_Hands_On_Activity/) | The full **8-step workflow** on two scenarios | Jupyter notebook | Independent t-test, chi-square |
| [Mini_Project_GrowthRetail/](Mini_Project_GrowthRetail/) | A **capstone mini project** (3 scenarios, CSV data) | Jupyter notebook + data | Paired t-test, independent t-test, chi-square |

Open any folder's `README.md` for its business context, hypotheses, run
instructions, verified results, and recommendations.

---

## The three deliverables

### 1. Business Analytics — Case Studies
Four standalone case studies, each isolating one test and one business question:

| Case study | Question | Test |
|-----------|----------|------|
| 1 — Marketing Campaign | Did a campaign raise weekly sales? | Independent t-test |
| 2 — Customer Behaviour | Do Premium vs Regular customers spend differently? | Independent t-test |
| 3 — Employee Performance | Did an initiative improve performance? | Paired t-test |
| 4 — Product Preference | Is region related to product preference? | Chi-square test |

Each is a runnable `.py` script that prints means/statistics, the p-value, and a
Significant / Not-significant verdict.

### 2. Day 16 — Hands-On Activity
A Jupyter notebook (`Day16_Hypothesis_Testing.ipynb`) that walks the **complete
eight-step workflow** — load data → business question → hypotheses → choose test →
execute → interpret → decide → document — across two scenarios:
- **Scenario A (numeric):** two stores' sales → independent t-test.
- **Scenario B (categorical):** region vs product preference → chi-square.

It closes with an **Industry Best Practices** section.

### 3. Mini Project — GrowthRetail
A capstone analysis written from the perspective of a data analyst at
**GrowthRetail**, validating a loyalty programme and a regional product strategy.
It loads realistic **CSV data** and runs all three test types end-to-end:
- **Loyalty programme** (paired t-test) — same customers, before vs after.
- **Two-store sales** (independent t-test) — two separate stores.
- **Region vs preference** (chi-square) — two categorical variables.

All three scenarios come out significant, each with an evidence-based
recommendation.

---

## Choosing the right test

The single most important skill across all three deliverables:

| Test | SciPy function | Use when… |
|------|----------------|-----------|
| **Independent (two-sample) t-test** | `stats.ttest_ind` | comparing the means of **two separate, unrelated groups** |
| **Paired t-test** | `stats.ttest_rel` | comparing **the same subjects measured twice** (before/after) |
| **Chi-square test of independence** | `stats.chi2_contingency` | testing a relationship between **two categorical variables** |

Decision rule everywhere: `p < 0.05` → **reject H0** (significant);
`p ≥ 0.05` → **fail to reject H0** (not significant).

---

## Requirements

- Python 3.8+
- SciPy and NumPy (for the case-study scripts)
- Jupyter and pandas (additionally for the two notebooks)

```bash
pip install scipy numpy pandas jupyter
```

---

## How to run

```bash
# Case studies (scripts)
cd Business_Analytics_Hypothesis_Testing/Case_Study_1_Marketing_Campaign
python case_study_1_marketing_campaign.py        # ...and the other three case studies

# Hands-on activity (notebook)
cd Day16_Hands_On_Activity
jupyter notebook Day16_Hypothesis_Testing.ipynb

# Mini project (notebook + CSV data)
cd Mini_Project_GrowthRetail
jupyter notebook growthretail_hypothesis_testing.ipynb
```

Both notebooks ship with their outputs already executed and embedded.

---

## Verified results (all computed by running the code)

| Deliverable | Scenario | Test | p-value | Verdict |
|-------------|----------|------|---------|---------|
| Case Studies | 1 — Marketing Campaign | Independent t | ≈ 0.000001 | Significant |
| Case Studies | 2 — Customer Behaviour | Independent t | ≈ 0.0 | Significant |
| Case Studies | 3 — Employee Performance | Paired t | ≈ 0.00000003 | Significant |
| Case Studies | 4 — Product Preference | Chi-square | ≈ 0.00007 | Significant |
| Hands-On | A — Two stores | Independent t | ≈ 0.000353 | Significant |
| Hands-On | B — Region × product | Chi-square | ≈ 0.000586 | Significant |
| Mini Project | 1 — Loyalty programme | Paired t | ≈ 2.7e-12 | Significant |
| Mini Project | 2 — Two-store sales | Independent t | ≈ 2.1e-13 | Significant |
| Mini Project | 3 — Region vs preference | Chi-square | ≈ 4.4e-10 | Significant |

> **Note on a few numbers:** some printed source materials quote different
> p-values for Case Study 4 (`0.00019`) and the Hands-On activity
> (`0.000093` / `0.003`). Those figures do not match what `chi2_contingency` /
> `ttest_ind` actually return for the given data — the values above were computed
> by running the code. Every verdict (Significant) is unchanged.

---

## Directory structure

```
DAY_16/
├── README.md                                   # this overview
│
├── Business_Analytics_Hypothesis_Testing/
│   ├── README.md
│   ├── Case_Study_1_Marketing_Campaign/        # independent t-test
│   ├── Case_Study_2_Customer_Behaviour/        # independent t-test
│   ├── Case_Study_3_Employee_Performance/      # paired t-test
│   └── Case_Study_4_Product_Preference/        # chi-square test
│
├── Day16_Hands_On_Activity/
│   ├── README.md
│   └── Day16_Hypothesis_Testing.ipynb          # 8-step workflow, 2 scenarios
│
└── Mini_Project_GrowthRetail/
    ├── README.md
    ├── growthretail_hypothesis_testing.ipynb   # 3 scenarios + summary
    └── data/                                    # loyalty / stores / region CSVs
```

---

## Key takeaways

- **Match the test to the data:** separate groups → independent t-test; same
  subjects twice → paired t-test; two categorical variables → chi-square.
- **A p-value answers "is it real?", not "how big is it?"** Always read it
  alongside the effect size (the actual means or counts).
- **Significance is the start, not the end.** A real effect still has to clear the
  business bar — cost, feasibility, durability — before you act on it.
- **Document everything:** hypotheses, test, p-value, decision, recommendation —
  so the analysis is transparent and reproducible.

> All datasets here are small and illustrative, chosen to make the concepts clear.
> The same code patterns apply directly to real business data.
