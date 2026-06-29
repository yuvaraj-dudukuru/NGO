# Real-World Case Studies — Data Visualization with Pandas & Matplotlib

Welcome! This folder contains **three hands-on case studies** that bring together
everything practiced during the course: loading data into a table, summarising it,
and turning it into clear charts that tell a story.

Each case study takes a small, realistic dataset and answers real business
questions using the right chart for the job.

---

## What's Inside

| # | Case Study | Charts Used | The Big Idea |
|---|------------|-------------|--------------|
| 1 | [Sales Analysis Dashboard](./case_study_1_sales_dashboard) | Line + Bar + Histogram | A 3-chart dashboard that tells a complete sales story at a glance |
| 2 | [Student Performance Analysis](./case_study_2_student_performance) | Bar + Scatter | Compare students, and link study hours to marks |
| 3 | [Customer Dataset Analysis](./case_study_3_customer_analysis) | Pie + Bar + Histogram | Volume vs. value — most customers ≠ most spending |

Each case study has its **own folder** containing:
- A fully **commented Python script** (`.py`) you can run.
- A **README.md** that explains the data, how to run it, and how to read the charts.

---

## Folder Structure
```
case_studys/
├── README.md                          <- you are here (overview of all case studies)
│
├── case_study_1_sales_dashboard/
│   ├── sales_dashboard.py             <- commented code
│   └── README.md                      <- explanation
│
├── case_study_2_student_performance/
│   ├── student_performance.py
│   └── README.md
│
└── case_study_3_customer_analysis/
    ├── customer_analysis.py
    └── README.md
```

---

## Getting Started

### 1. Install Python libraries (one time only)
All three case studies use the same two libraries:
```bash
pip install pandas matplotlib
```

### 2. Run a case study
Open a terminal **inside that case study's folder** and run its script. For example:
```bash
cd case_study_1_sales_dashboard
python sales_dashboard.py
```
Each script will:
1. Print the data table and the written insights in the terminal.
2. Open a window showing the chart(s).
3. Save a `.png` image of the chart(s) in the same folder.

> **Tip:** Run them in order (1 → 2 → 3). The comments build on each other and get
> a little richer each time.

---

## Which Chart for Which Job?
A quick reference you can reuse beyond these case studies:

| Chart | Best For | Example Here |
|-------|----------|--------------|
| **Line chart**  | A trend over time | Revenue per month |
| **Bar chart**   | Comparing categories | Revenue by product, marks by student |
| **Histogram**   | Distribution of one numeric column / spotting outliers | Order values, customer ages |
| **Scatter plot**| Relationship between two numeric columns | Study hours vs. marks |
| **Pie chart**   | Share / proportion of a whole | Customer share by city |

---

## Learning Outcomes
By the end of these case studies you will be able to:
- Build a `pandas` DataFrame and summarise it with `groupby`, `mean`, `sum`, and `value_counts`.
- Choose the **right chart** for a given question.
- Place multiple charts in one figure with `plt.subplots()`.
- Read charts critically — spotting trends, top performers, outliers, and contrasts.
- Translate charts into a plain-English **insight** and an actionable **recommendation**.

Happy analysing! 📊
