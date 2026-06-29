# Phase 3 — Exploratory Data Analysis (EDA)

**Goal:** Now that the data is clean, *explore* it to discover the patterns that answer the
business questions. (Day 6 techniques.)

## Run it

```bash
python phase3_eda.py
```

## The five analyses

| Section | Technique | Question it answers |
|---------|-----------|---------------------|
| 7.1 | `describe()` | What's a typical order now? |
| 7.2 | `value_counts()` | How many orders per category/city? |
| 7.3 | `groupby().sum()` | Which category/city brings the most **money**? |
| 7.4 | `corr()` | Does ordering more items mean spending more? |
| 7.5 | `describe()` again | Did any outlier survive cleaning? |

## Expected highlights

```
Orders per category:   Electronics 3, Grocery 2, Clothing 2
Orders per city:       Pune 3, Mumbai 2, Delhi 2
```

## What the patterns mean

- **Electronics** is the top **revenue** category (high-value items).
- **Pune** is the most **active** city.
- **Grocery** sells in **high quantities** but **low amounts** — volume, not revenue.
- The **Quantity ↔ Amount correlation is weak**: expensive Electronics sell in small
  quantities while cheap Grocery sells in bulk — *two different buying patterns*.

> **Remember:** correlation is **not** causation. A weak number here is itself an insight, not
> a failure.

These findings feed directly into Phase 4 (charts) and Phase 6 (insights).
