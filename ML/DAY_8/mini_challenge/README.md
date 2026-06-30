# 🍽️ Mini Challenge — "DineWell": What Drives Bills and Tips?

**Scenario.** You are a junior data analyst at **DineWell**, a restaurant chain.
Management wants to understand **what drives bills and tips** so they can boost
revenue. Your job is to perform a complete statistical visualization analysis
of the classic **`tips`** dataset and present **business insights**.


---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `tips_analysis.py` | Fully commented Python script that inspects the data and produces every chart below, including optional stretch goals. |
| `README.md` | This file — the explanation, findings and business report. |

---

## ▶️ How to run

1. Install the required libraries (only needed once):
   ```bash
   pip install numpy pandas matplotlib seaborn
   ```
2. Run the script from a terminal:
   ```bash
   python tips_analysis.py
   ```
3. Each chart opens in its own window. **Close a window to see the next one.**
   Data previews, summary statistics and the key correlation are printed to the
   terminal.

> **No CSV needed** — the dataset is built into seaborn (`sns.load_dataset("tips")`).

---

## 📊 The dataset

The `tips` dataset records one row per restaurant bill:

| Column | Meaning |
|--------|---------|
| `total_bill` | Bill amount in dollars (numeric) |
| `tip` | Tip amount in dollars (numeric) |
| `sex` | Gender of the bill payer (category) |
| `smoker` | Whether the party included smokers (category) |
| `day` | Day of week — Thur / Fri / Sat / Sun (category) |
| `time` | Lunch or Dinner (category) |
| `size` | Number of people in the party (numeric) |

---

## 🔍 What the script does, step by step

### 1. Analyze the dataset
`head()` previews the rows, `describe()` gives summary statistics for numeric
columns, and `isnull().sum()` confirms there are **no missing values**. Always
inspect before plotting.

### 2. Statistical visualizations
| Chart | Code | What it tells us |
|-------|------|------------------|
| **Histogram + KDE** of `total_bill` | `histplot(..., kde=True)` | Shape of the bill distribution. |
| **Box plot** of `total_bill` by `day` | `boxplot` | Compare days, spot outliers. |
| **Violin plot** of `total_bill` by `time` | `violinplot` | Lunch vs Dinner spread. |
| **Scatter plot** `total_bill` vs `tip` | `scatterplot(hue="time")` | Bill–tip relationship. |
| **Count plot** per `day` | `countplot` | Which day is busiest. |
| **Bar plot** average bill per `day` | `barplot` | Which day has the highest average bill. |

### 3. Correlation study
`tips.corr(numeric_only=True)` builds the correlation matrix, drawn as an
**annotated heatmap**. The strongest pair is `total_bill` ↔ `tip`.

### 4. Trends and outliers
- **Distribution shape:** `total_bill` is **right-skewed** — most bills are
  small, a few are large.
- **Strongest correlation:** `total_bill` ↔ `tip` (**~0.68**).
- **Outliers:** high-value bills appear in the box plot, mostly on weekends.

---

## ✅ Business insights & recommendations

> Each insight climbs the storytelling ladder: *observation → meaning → action.*

1. **Bigger bills directly produce bigger tips** (~0.68 correlation).
   - 💡 **Recommendation:** Train staff on **upselling** (sides, drinks,
     desserts) — higher bills raise revenue *and* tips at the same time.

2. **Dinners and weekends bring the largest bills** (violin + box plots).
   - 💡 **Recommendation:** Focus **premium menus and promotions** on dinner
     service and weekends, when guests already spend more.

3. **Party size moves with the bill, and Saturday is busiest** (count plot).
   - 💡 **Recommendation:** Encourage **larger parties** (group offers, set
     menus) and schedule the best staff on Saturdays to capture peak demand.

---

## 🚀 Stretch goals (optional)

The script includes three commented-out stretch blocks — **uncomment** any to
explore further:

1. **Box plot with `hue="sex"`** — compare male vs female bills per day.
2. **Pair plot** of `total_bill`, `tip`, `size` colored by `time` — see every
   relationship at once.
3. **Mini EDA report** — an executive-summary / findings / recommendations
   printout in the Day-6 report style.

---

## 🧠 Concepts practised
`head` · `describe` · missing-value checks · `histplot` · `boxplot` ·
`violinplot` · `scatterplot` · `countplot` · `barplot` · correlation `heatmap`
· `pairplot` · turning charts into business storytelling
