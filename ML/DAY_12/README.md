# Day 12 — Feature Engineering

A collection of feature-engineering material: three worked **case studies**, a
hands-on **Jupyter notebook**, and a **mini challenge**. Each one shows how raw
tabular data is transformed into analysis- and dashboard-ready datasets.

## Contents

| Folder | Type | Theme |
|---|---|---|
| [Case_Study_1_Retail](Case_Study_1_Retail/) | Case study | Revenue, profit, margin, time & size features |
| [Case_Study_2_Customer_Analytics](Case_Study_2_Customer_Analytics/) | Case study | RFM features + loyalty segmentation |
| [Case_Study_3_HR_Analytics](Case_Study_3_HR_Analytics/) | Case study | Tenure, performance bands, pay equity |
| [Hands_On_Activity](Hands_On_Activity/) | Jupyter notebook | 9-step guided feature-engineering workflow |
| [Mini_Challenge](Mini_Challenge/) | Challenge + solution | MartPro retail: end-to-end transform, validate, summarize |

Each folder contains:
- a runnable Python script (or `.ipynb` notebook), and
- a `README.md` explaining the goal, engineered features, how to run, expected
  output, and the resulting insight.

## Requirements

```bash
pip install pandas numpy
```

The hands-on activity additionally needs Jupyter to open the notebook:

```bash
pip install jupyter
```

## Running everything

```bash
# Case studies
python Case_Study_1_Retail/retail_feature_engineering.py
python Case_Study_2_Customer_Analytics/customer_analytics_feature_engineering.py
python Case_Study_3_HR_Analytics/hr_analytics_feature_engineering.py

# Mini challenge
python Mini_Challenge/martpro_mini_challenge.py

# Hands-on activity (opens in the browser)
jupyter notebook Hands_On_Activity/Day12_Feature_Engineering.ipynb
```

## The takeaway

In every example, the most valuable columns did **not** exist in the raw data
— they were *engineered*. Profit by category, RFM customer segments, pay-equity
gaps, and B2B vs B2C revenue splits only become visible after transformation.
That is the core value of feature engineering.

> Note: All names, emails, and values across this material are fictional sample
> data used purely for demonstration.
