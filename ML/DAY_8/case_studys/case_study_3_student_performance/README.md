# Case Study 3 — Student Performance 🎓

An EDA of a small classroom dataset that explores **how study hours relate to
exam marks** and **how subjects relate to one another**. It is a relatable,
beginner-friendly dataset where every relationship has an intuitive meaning.

---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `student_performance.py` | Fully commented Python script that creates the data and produces every chart below. |
| `README.md` | This file — the explanation and findings. |

---

## ▶️ How to run

1. Install the required libraries (only needed once):
   ```bash
   pip install pandas seaborn matplotlib
   ```
2. Run the script from a terminal:
   ```bash
   python student_performance.py
   ```
3. Each chart opens in its own window. **Close a window to see the next one.**

---

## 📊 The data

| Name  | Class | StudyHours | Math | Science |
|-------|-------|-----------|------|---------|
| Asha  | A     | 6         | 85   | 90      |
| Ravi  | A     | 3         | 60   | 65      |
| Imran | B     | 8         | 92   | 88      |
| Divya | B     | 2         | 45   | 50      |
| Karan | A     | 5         | 78   | 80      |
| Meena | B     | 3         | 55   | 60      |
| Sahil | A     | 7         | 88   | 85      |
| Tara  | B     | 4         | 65   | 68      |

---

## 🔍 What the script does, step by step

### 1. Relationship — Study Hours vs Math (`scatterplot` + `hue`)
A scatter plot of study time against Math marks, colored by class.
- **Interpretation:** A clear **positive** relationship — more study hours,
  higher marks. The `hue="Class"` shows the pattern holds across both classes.

### 2. Correlation heatmap (`heatmap`)
Compares all numeric columns at once.
- **Interpretation:** Study hours correlate strongly with **both** Math and
  Science; Math and Science also correlate strongly with **each other**
  (good students tend to do well in both).

### 3. Category comparison — Average Math by Class (`barplot`)
- **Interpretation:** Reveals which class performs better on average in Math.

---

## ✅ Findings and recommendations

- **Study hours strongly drive marks** — the clearest, most actionable
  relationship in the data.
- Performance in **Math and Science moves together**.
- **Recommendation:** Encourage more study time. Students strong in one science
  subject tend to be strong in the other, so support struggling students
  **broadly** rather than subject-by-subject.

---

## 🧠 Concepts practised
Building a `DataFrame` by hand · `scatterplot` · `hue` for grouping ·
correlation `heatmap` · `barplot` (group means) · reading multi-column
correlations
