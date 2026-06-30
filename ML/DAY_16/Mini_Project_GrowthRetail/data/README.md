# `data/` — GrowthRetail hypothesis-testing datasets

The three synthetic datasets used by the
[`../growthretail_hypothesis_testing.ipynb`](../growthretail_hypothesis_testing.ipynb)
notebook — one per statistical test:

| File | Feeds which test | Holds |
|------|------------------|-------|
| `store_daily_sales.csv` | Two-sample t-test (did average daily sales differ?) | daily sales figures by group |
| `loyalty_spending.csv`  | Comparing loyalty vs non-loyalty spending | spend by customer group |
| `region_preference.csv` | Chi-square test of independence (does preference depend on region?) | counts by region x product |

The notebook loads these with pandas (`pd.read_csv`). All values are synthetic
sample data — no real customers.

> Data files only — nothing to run here. Open the notebook to use them.
