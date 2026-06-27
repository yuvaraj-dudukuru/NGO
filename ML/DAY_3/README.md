# 📊 EduTrack — NumPy Performance Report (Mini Challenge)

> **Day 3 · NumPy Fundamentals** — Summer Internship Program, Data Analytics Track

A beginner-friendly NumPy mini challenge. You play a **junior data analyst at "EduTrack"**, an online learning platform. The academics team hands you the final exam scores of 10 students and asks for a quick performance report — built entirely with NumPy.

---

## 🎯 Problem Statement

The scores of 10 students are:

```
78, 92, 56, 88, 95, 43, 67, 81, 73, 60
```

Write a NumPy program (in a Python script or Jupyter notebook) that produces a performance report.

## ✅ Requirements

1. Store the scores in a NumPy array.
2. Calculate and print the **total**, **average**, **highest**, and **lowest** scores.
3. Calculate and print the **median** and **standard deviation**.
4. Identify the **position (index)** of the top scorer using `argmax`.
5. Use **Boolean indexing** to list all students who passed (score ≥ 60).
6. Count and print how many students passed.
7. Use at least one **vectorized operation** (e.g., add 5 grace marks to every score and show the new array).

## 📤 Expected Output

```
Scores: [78 92 56 88 95 43 67 81 73 60]
Total: 733
Average: 73.3
Highest: 95
Lowest: 43
Median: 75.5
Standard Deviation: 16.0
Top scorer is at index: 4
Passed students (>=60): [78 92 88 95 67 81 73 60]
Number of students who passed: 8
Scores after 5 grace marks: [ 83  97  61  93 100  48  72  86  78  65]
```

> ℹ️ **Note on standard deviation:** `np.std()` computes the **population** standard deviation by default (`ddof=0`), which gives `15.975…` → rounds to **`16.0`**. If you want the **sample** standard deviation, use `np.std(scores, ddof=1)`, which gives ≈ `16.8`.

## 🌟 Stretch Goals (Optional)

- Compute the **pass percentage** (passed students ÷ total students × 100).
- Use `argmin` to find the position of the **lowest scorer**.
- **Cap** the grace-mark scores at 100 so no score exceeds 100 (hint: combine with Boolean indexing or `np.clip`).

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Try it yourself first!

Open [`starter.py`](starter.py) and fill in the `TODO`s, or work through the notebook:

```bash
jupyter notebook solution.ipynb
```

### 3. Run the solution

```bash
python solution.py
```

> 💡 **Learn by doing:** Attempt the challenge in `starter.py` **before** peeking at `solution.py`. The struggle is where the learning happens.

---

## 📁 Repository Structure

```
numpy-mini-challenge/
├── README.md          # You are here
├── requirements.txt   # Python dependencies (numpy, jupyter)
├── starter.py         # Skeleton with TODOs — try this first
├── solution.py        # Full reference solution + stretch goals
├── solution.ipynb     # Jupyter notebook walkthrough
└── .gitignore         # Ignores caches, checkpoints, venvs
```

---

## 🧠 Concepts Practiced

| Concept | NumPy Tool |
|---|---|
| Array creation | `np.array()` |
| Aggregations | `np.sum`, `np.mean`, `np.max`, `np.min` |
| Statistics | `np.median`, `np.std` |
| Finding positions | `np.argmax`, `np.argmin` |
| Boolean indexing / filtering | `scores[scores >= 60]` |
| Vectorized operations | `scores + 5` |
| Capping values | `np.clip` |

---