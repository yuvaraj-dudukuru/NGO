# Case Study 4 — Inventory Analysis

> Detect a **seasonal demand pattern** and use it to drive **inventory planning**.

---

## 1. Business Context

A retailer wishes to analyze product demand over the year to plan inventory,
particularly for **seasonal stock requirements**.

## 2. Objective

> **Analyze monthly product demand to identify the seasonal pattern and inform
> inventory planning.**

## 3. Dataset

Twelve rows, one per month.

| Field        | Type             | Description                                       |
|--------------|------------------|---------------------------------------------------|
| `Month`      | string           | Month label (`Jan` … `Dec`)                       |
| `Demand`     | integer          | Units demanded that month                         |
| `HighDemand` | boolean (derived)| `True` where demand exceeds the yearly average    |

```
Demand: 500, 480, 510, 530, 600, 650, 620, 580, 700, 850, 1100, 1400
```

## 4. How to Run

```bash
# from this folder
pip install pandas
python inventory_analysis.py
```

## 5. Method — Line by Line

| Code | What it does |
|------|--------------|
| `df["Demand"].mean()` | Average monthly demand, used as a **reference level**. |
| `df["Demand"] > avg_demand` | Boolean flag for **above-average (high-demand)** months. |
| `df.loc[df["HighDemand"], "Month"].tolist()` | Extracts the list of high-demand months. |
| `df.loc[df["Demand"].idxmax(), "Month"]` | Finds the single **peak-demand** month. |

## 6. Expected Output

```
Average monthly demand: 710.0
High-demand months: ['Oct', 'Nov', 'Dec']
Peak demand month: Dec
```

> **Note:** The average is `710`, and September's demand is `700` — just **below**
> the average — so the strictly above-average months are `Oct, Nov, Dec`. (Some
> printed copies list `Sep` as well; that is incorrect for a strict `>` comparison.)

## 7. Business Interpretation

- **Seasonality:** Demand is **below average for most of the year** but rises
  sharply in the final quarter, **peaking in December (1,400 units — roughly twice
  the annual average)**.
- **High-demand window:** The strictly above-average months are **October through
  December**, with the seasonal climb beginning in **September** (700 units, right
  at the average).
- **Findings:** The product has **strong seasonal demand concentrated in the
  final quarter**.

### Recommendations

1. **Build inventory ahead of September** to meet the fourth-quarter surge.
2. Keep stock **lean in the low-demand early months** to minimize holding costs.

## 8. Key Takeaway

Seasonal inventory planning informed by time-series analysis directly reduces
**both** the risk of **stockouts during peak demand** and the cost of **excess
inventory during slow periods** — a clear example of analysis driving
operational efficiency.
