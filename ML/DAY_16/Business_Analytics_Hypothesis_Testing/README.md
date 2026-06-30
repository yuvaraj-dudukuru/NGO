# Business Analytics — Hypothesis Testing

A self-contained set of business analytics materials that show how **hypothesis
testing** turns an "it looks like sales went up" hunch into a statistically
defensible decision. Each item lives in its **own dedicated folder** with its own
README, so it can be opened and run on its own.

These materials accompany **Day 16 — Hypothesis Testing Basics**.

---

## Contents

| Folder | What it is | Test | Verdict |
|--------|-----------|------|---------|
| [Case_Study_1_Marketing_Campaign](Case_Study_1_Marketing_Campaign/) | Did a campaign increase weekly sales? | Independent t-test | Significant |
| [Case_Study_2_Customer_Behaviour](Case_Study_2_Customer_Behaviour/) | Do Premium vs Regular customers spend differently? | Independent t-test | Significant |
| [Case_Study_3_Employee_Performance](Case_Study_3_Employee_Performance/) | Did an initiative improve performance? | Paired t-test | Significant |
| [Case_Study_4_Product_Preference](Case_Study_4_Product_Preference/) | Is region related to product preference? | Chi-square test | Significant |

Each folder has its own `README.md` with the business context, hypotheses, how to
run it, the verified result, and the recommendation.

> The **hands-on workflow notebook** and the **GrowthRetail mini project** now
> live in their own top-level folders alongside this one:
> `../Day16_Hands_On_Activity/` and `../Mini_Project_GrowthRetail/`.

---

## Why hypothesis testing?

When a number moves — sales rise, one segment spends more, scores improve — the
hard question is always the same: **is this a real effect, or just normal random
fluctuation?** Hypothesis testing gives a disciplined answer.

Every test here follows the same logic:

1. **State a null hypothesis (H0)** — the "nothing interesting is happening"
   assumption (e.g. *no difference between the two groups*).
2. **State an alternative hypothesis (H1)** — the effect we suspect is real.
3. **Compute a p-value** — the probability of seeing data this extreme *if H0
   were true*.
4. **Apply a decision rule** — compare the p-value to a significance level
   `alpha` (here, `0.05`):
   - `p < 0.05` → **reject H0** → the result is **statistically significant**.
   - `p >= 0.05` → **fail to reject H0** → **not significant** (could be chance).

> A small p-value means the observed result would be very unlikely by chance
> alone, so we conclude the effect is real. It does **not** measure how *large*
> the effect is — always read the p-value alongside the actual means.

---

## The three tests used here

| Test | Function | When to use it |
|------|----------|----------------|
| **Independent (two-sample) t-test** | `scipy.stats.ttest_ind` | Compare the means of **two separate, unrelated groups** (different weeks, different customers). |
| **Paired t-test** | `scipy.stats.ttest_rel` | Compare **the same subjects measured twice** (before vs. after on the *same* people). |
| **Chi-square test of independence** | `scipy.stats.chi2_contingency` | Test whether **two categorical variables** are related (e.g. region vs. product preference). |

Choosing the right test is the whole game. Using an independent t-test where a
paired test belongs (or vice versa) can hide a real effect or invent a fake one.

---

## Requirements

- Python 3.8+
- [SciPy](https://scipy.org/) and [NumPy](https://numpy.org/)

```bash
pip install scipy numpy
```

---

## How to run

Each item runs from inside its own folder:

```bash
cd Case_Study_1_Marketing_Campaign && python case_study_1_marketing_campaign.py
cd Case_Study_2_Customer_Behaviour && python case_study_2_customer_behaviour.py
cd Case_Study_3_Employee_Performance && python case_study_3_employee_performance.py
cd Case_Study_4_Product_Preference && python case_study_4_product_preference.py
```

### Verified results (summary)

| Item | Statistic | p-value | Verdict |
|------|-----------|---------|---------|
| Case Study 1 — Marketing Campaign | t ≈ −8.005 | ≈ 0.000001 | Significant |
| Case Study 2 — Customer Behaviour | t ≈ 18.24 | ≈ 0.0 | Significant |
| Case Study 3 — Employee Performance | t ≈ −17.67 | ≈ 0.00000003 | Significant |
| Case Study 4 — Product Preference | χ² ≈ 24.227 | ≈ 0.00007 | Significant |

> **Note on Case Study 4:** some printed materials quote `p = 0.00019` for this
> table, but the value `chi2_contingency` actually returns is `≈ 0.00007`. The
> values above were computed by running the code; the verdict (Significant) is
> the same either way.

---

## Folder structure

```
Business_Analytics_Hypothesis_Testing/
├── README.md                                  # this index
├── Case_Study_1_Marketing_Campaign/
│   ├── README.md
│   └── case_study_1_marketing_campaign.py     # Independent t-test
├── Case_Study_2_Customer_Behaviour/
│   ├── README.md
│   └── case_study_2_customer_behaviour.py     # Independent t-test
├── Case_Study_3_Employee_Performance/
│   ├── README.md
│   └── case_study_3_employee_performance.py   # Paired t-test
└── Case_Study_4_Product_Preference/
    ├── README.md
    └── case_study_4_product_preference.py     # Chi-square test of independence
```

The hands-on notebook and the mini project sit beside this folder at the
`DAY_16/` level:

```
DAY_16/
├── Business_Analytics_Hypothesis_Testing/   # this folder (4 case studies)
├── Day16_Hands_On_Activity/                 # 8-step workflow notebook
└── Mini_Project_GrowthRetail/               # capstone mini project
```

---

## Key takeaways

- **Pick the test that matches the data:** separate groups → independent t-test;
  same subjects twice → paired t-test; two categorical variables → chi-square.
- **The p-value answers "is it real?", not "how big is it?"** Always pair the
  p-value with the means/effect size before deciding.
- **Statistical significance is the start, not the end.** A significant result
  still has to clear the business bar — cost, feasibility, and durability of the
  effect — before you act on it.

> These materials use small, illustrative datasets chosen to make the concepts
> clear. The same code patterns apply directly to real business data.
