# TechHire — Job Applicant Analysis 📊

A beginner-friendly **Exploratory Data Analysis (EDA)** mini-project built with
[Pandas](https://pandas.pydata.org/). It simulates a junior data-analyst task at a
recruitment company ("TechHire"): explore a small dataset of job applicants and
produce a quick summary with insights.

## 🎯 Problem Statement

The HR team provides a dataset of job applicants. The task is to load it, explore
it, filter it, compute statistics, and draw conclusions about the applicant pool.

## 📂 Dataset

The dataset is created in code (no external file needed) with 8 applicants and 5 columns:

| Column            | Description                          |
|-------------------|--------------------------------------|
| `Name`            | Applicant name                       |
| `Age`             | Applicant age                        |
| `City`            | City of residence                    |
| `Experience`      | Years of work experience             |
| `Expected_Salary` | Salary expectation (INR)             |

## ✅ What the script does

1. **Inspect** — prints `shape`, `columns`, and `head()`.
2. **Explore** — runs `describe()` and counts applicants per city with `value_counts()`.
3. **Filter** —
   - applicants with more than 5 years of experience, and
   - applicants from Mumbai expecting a salary above 100,000.
4. **Statistics** — average expected salary, plus max/min experience.
5. **Sort** — top 3 applicants by expected salary (descending).
6. **Conclusions** — written observations about the applicant pool.

### ✨ Stretch goals (included)
- A `Salary_Per_Year_Exp` column (`Expected_Salary / Experience`, guarded against very low experience).
- Average expected salary **per city** via `groupby`.
- The city with the **highest average** expected salary.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+

### Installation
```bash
pip install -r requirements.txt
```

### Run
```bash
python applicant_analysis.py
```

## 🔍 Key Insights

- The dataset has **8 applicants** and **5 columns**.
- **Pune** and **Mumbai** are the most common cities.
- Four applicants have **more than 5 years** of experience: Ravi, Divya, Meena, Tara.
- The **highest expected salaries** belong to the most experienced applicants (Divya, Tara, Meena).
- The **average expected salary** is around **83,750**, ranging from **35,000** to **150,000**.

## 🛠️ Built With
- Python
- Pandas

---
*A learning project for practising Pandas fundamentals.*
