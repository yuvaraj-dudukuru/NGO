# Day 16 — Hands-On Activity (Hypothesis Testing Workflow)

**Notebook:** `Day16_Hypothesis_Testing.ipynb`

A Jupyter notebook that walks through the **complete eight-step hypothesis-testing
workflow** on a business scenario, covering both a **numeric comparison** and a
**categorical relationship**.

## The eight-step workflow
1. **Load the dataset** — sales of two stores (numeric) + a region × product
   contingency table (categorical).
2. **Define the business question** — for each scenario.
3. **Formulate the hypotheses** — state H0 and H1 *before* looking at results.
4. **Choose the test** — match the test to the data.
5. **Execute the tests** — run them in code.
6. **Interpret the p-values** — apply the `alpha = 0.05` decision rule.
7. **Make the decision** — reject or fail to reject H0.
8. **Document the findings** — record hypotheses, test, p-value, decision,
   recommendation.

The notebook closes with an **Industry Best Practices** section.

## The two scenarios
| Scenario | Question | Test | p-value | Verdict |
|----------|----------|------|---------|---------|
| **A (numeric)** | Do two stores have different average sales? | Independent t-test (`ttest_ind`) | ≈ 0.000353 | **Significant** |
| **B (categorical)** | Is region related to product preference? | Chi-square (`chi2_contingency`) | ≈ 0.000586 | **Significant** |

Store A's average sales (≈ 136) are significantly higher than Store B's (≈ 119);
region and product preference are significantly related.

## Hypotheses
**Scenario A**
- H0: the two stores have equal average sales.
- H1: the two stores' average sales differ.

**Scenario B**
- H0: region and product preference are independent.
- H1: region and product preference are related.

Significance level: `alpha = 0.05`. Decision rule: `p < 0.05` → reject H0.

> **Note:** some printed materials quote `Scenario A p = 0.000093` and
> `Scenario B p = 0.003` for this exact data. Those figures do not match what
> `ttest_ind` / `chi2_contingency` actually return — the verified values are
> `0.000353` and `0.000586`. Both are well below 0.05, so every conclusion is
> unchanged. The notebook uses the verified values.

## How to run
```bash
pip install jupyter scipy numpy pandas
jupyter notebook Day16_Hypothesis_Testing.ipynb
```
Then run the cells top to bottom (Kernel → Restart & Run All). The notebook ships
with outputs already executed and embedded.

## Folder structure
```
Day16_Hands_On_Activity/
├── README.md
└── Day16_Hypothesis_Testing.ipynb   # 8-step workflow, 2 scenarios + best practices
```
