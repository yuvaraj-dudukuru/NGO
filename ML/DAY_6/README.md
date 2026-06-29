# 🛒 FreshCart — Exploratory Data Analysis (EDA)

A mini data-analysis project simulating the work of a **junior data analyst** at
**FreshCart**, an online grocery delivery service. The operations team provides a
small dataset of recent orders; the task is to perform a **complete EDA** to
uncover patterns, detect anomalies, and recommend actions to grow the business.

---

## 📁 Project Structure

```
.
├── eda_freshcart.py     # Full EDA script (run this)
├── EDA_REPORT.md        # Written EDA report (summary, findings, recommendations)
├── requirements.txt     # Dependencies (pandas)
├── .gitignore
└── README.md
```

## ▶️ How to Run

```bash
pip install -r requirements.txt
python eda_freshcart.py
```

The script prints every step of the analysis to the console.

---

## 📊 The Dataset

12 recent orders across 3 cities and 3 product categories.

| Column         | Description                          |
|----------------|--------------------------------------|
| `OrderID`      | Unique order identifier (1–12)       |
| `City`         | Pune / Mumbai / Delhi                |
| `Category`     | Fruits / Dairy / Snacks              |
| `Items`        | Number of items in the order         |
| `OrderValue`   | Order value in ₹                     |
| `DeliveryMins` | Delivery time in minutes             |

---

## 🔍 What the Analysis Covers

1. **Explore** — `shape`, `info()`, `describe()`
2. **Statistics** — mean vs median of `OrderValue` & `DeliveryMins`, with skew interpretation
3. **Patterns** — most orders per city, highest-value category, avg delivery time per city
4. **Anomalies** — IQR method to flag outliers in `OrderValue`
5. **Relationships** — correlation of `Items` vs `OrderValue` and `Items` vs `DeliveryMins`
6. **Insights** — observation → insight → recommendation ladder
7. **Report** — executive summary, key findings, recommendations
8. **Stretch goals** — full correlation matrix + "ideal market" identification

---

## ✅ Key Results

- **12 orders, 3 cities, 3 categories** — demand is **balanced** (4 orders per city).
- **`OrderValue` is right-skewed**: mean **₹1,117** vs median **₹760**, pulled up by one large order.
- **IQR flags Order 10 (₹5,000, Mumbai, Snacks)** as a clear outlier worth investigating.
- **Items ↔ OrderValue: +0.84** (very strong) and **Items ↔ DeliveryMins: +0.99** (very strong) — bigger orders mean more revenue **and** longer deliveries.
- **Snacks** has the highest average order value (₹2,200).

## 💡 Recommendations

- **Nurture the outlier**: verify Order 10 and convert this likely bulk/B2B customer with a loyalty program.
- **Optimize fulfillment for large orders** (dedicated pickers, batching) to cut long delivery times.
- **Promote larger baskets** — more items per order directly increases revenue.

See [EDA_REPORT.md](EDA_REPORT.md) for the full written report.
