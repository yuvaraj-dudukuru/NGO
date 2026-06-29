# 📊 Case Studies — Statistical Visualization & EDA

Welcome! This folder contains **three complete, real-world style case studies**
that bring together the data-visualization charts learned in this course. Each
case study takes a dataset, asks questions about it, and answers them with
**Exploratory Data Analysis (EDA)** — that is, by *looking* at the data through
well-chosen charts before drawing conclusions.

---

## 🗂️ Folder structure

```
case_studys/
│
├── README.md                          ← you are here (overview of everything)
│
├── case_study_1_titanic/
│   ├── titanic_analysis.py            ← commented code
│   └── README.md                      ← explanation + findings
│
├── case_study_2_sales/
│   ├── sales_analysis.py              ← commented code
│   └── README.md                      ← explanation + findings
│
└── case_study_3_student_performance/
    ├── student_performance.py         ← commented code
    └── README.md                      ← explanation + findings
```

---

## 📚 The three case studies

| # | Case study | Dataset | Main question | Key charts |
|---|------------|---------|---------------|------------|
| 1 | **Titanic** 🚢 | Real passenger data (built into seaborn) | Who survived, and why? | histplot, boxplot, countplot, heatmap |
| 2 | **Sales** 📈 | Small hand-built table | Does ad spend drive revenue? Which region wins? | scatterplot, barplot, boxplot |
| 3 | **Student Performance** 🎓 | Small hand-built table | Do study hours raise marks? | scatterplot, heatmap, barplot |

Open each sub-folder's `README.md` for the full write-up of that case study.

---

## ▶️ How to run any case study

All three use the same Python libraries. Install them once:

```bash
pip install pandas seaborn matplotlib
```

Then run the script inside any case-study folder, for example:

```bash
cd case_study_1_titanic
python titanic_analysis.py
```

Each chart opens in its own window — **close a window to advance to the next
chart.** Some scripts also print text (data previews, correlation values) to
the terminal.

---

## 🧰 Libraries used

| Library | Why we use it |
|---------|---------------|
| **pandas** | Stores data in tables called *DataFrames* and computes things like `.corr()`. |
| **seaborn** | High-level statistical plotting — makes attractive charts in one line. |
| **matplotlib** | The engine seaborn is built on; we use it for titles and to display charts. |

---

## 🎯 Skills you will practise across all three

- Loading / building a dataset and **inspecting it before plotting**
- **Distribution** charts: `histplot`, `boxplot`
- **Relationship** charts: `scatterplot` (+ `hue` for grouping)
- **Comparison** charts: `countplot`, `barplot`
- **Correlation heatmaps** to compare many numeric columns at once
- Reading a story out of the numbers — and the crucial reminder that
  **correlation is not causation**

---

## 💡 A note on correlation vs causation

Every case study ends with a caution: just because two things move together
(**correlation**) does not mean one *causes* the other (**causation**).
- Titanic: class correlates with survival, but the *cause* was lifeboat access.
- Sales: ad spend correlates with revenue, but a controlled test is needed to
  prove ads cause sales.

Keeping this distinction in mind is what separates careful analysis from
jumping to conclusions.

---

*Happy analysing! Start with Case Study 1 (Titanic) — it uses real data and is
the most fun to explore.* 🚀
