# Case Study 1 — Titanic Dataset 🚢

A complete **Exploratory Data Analysis (EDA)** of the famous Titanic passenger
dataset using statistical visualizations. This is a great first case study
because the data is real, slightly messy (it has missing values), and tells a
genuine human story about who survived the disaster.

---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `titanic_analysis.py` | Fully commented Python script that loads the data and produces every chart below. |
| `README.md` | This file — the explanation and findings. |

---

## ▶️ How to run

1. Install the required libraries (only needed once):
   ```bash
   pip install seaborn matplotlib pandas
   ```
2. Run the script from a terminal:
   ```bash
   python titanic_analysis.py
   ```
3. Each chart opens in its own window. **Close a window to see the next one.**
   The first thing printed in the terminal is a preview of the data and a count
   of missing values.

> **No CSV needed** — the dataset is built into seaborn (`sns.load_dataset("titanic")`).

---

## 🔍 What the script does, step by step

### 1. Loading and inspecting
We load the data and **immediately check for missing values** with
`isnull().sum()` — a cleaning habit from Day 5. The Titanic data has real
missing ages, a reminder that **cleaning comes before visualization**.

### 2. Distribution plot — Age (`histplot`)
Shows how passenger ages are spread out.
- **Interpretation:** Most passengers were young adults (20–40). The shape is
  slightly **right-skewed** because there were fewer elderly passengers.

### 3. Box plot — Fare by Class (`boxplot`)
Compares ticket fares across the three passenger classes.
- **Interpretation:** First-class fares are much higher with many high
  **outliers** (wealthy passengers); third-class fares are low and tightly
  clustered.

### 4. Count plot — Survival by Sex (`countplot` with `hue`)
Counts survivors and non-survivors for each sex.
- **Interpretation:** A far higher proportion of women survived — the famous
  **"women and children first"** pattern, revealed instantly.

### 5. Correlation heatmap (`heatmap`)
Shows how strongly the numeric columns move together.
- **Interpretation:** `fare` is **positively** correlated with `survived`
  (wealthier → more likely to survive), while `pclass` is **negatively**
  correlated (lower class number = higher social class = better survival).

---

## ✅ Findings and recommendations

- **Finding:** Survival was strongly linked to **sex** (women survived more)
  and to **class/fare** (wealthier passengers survived more).
- **Insight:** Social factors — gender norms and wealth/class — heavily
  influenced survival.
- **Conclusion:** The Titanic data vividly shows how category and wealth
  affected outcomes — a powerful example of EDA revealing a human story.

> ⚠️ **Causation caution:** Class *correlates* with survival, but the real
> cause was **lifeboat access tied to class**, not the class label itself.
> Correlation is not causation.

---

## 🧠 Concepts practised
`histplot` · `boxplot` · `countplot` · `heatmap` · missing-value checks ·
correlation · skewness · outliers · correlation-vs-causation
