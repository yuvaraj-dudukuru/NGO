# CityCab Rides — Exploratory Data Analysis Report

**Analyst:** Jordan Lee  |  **Role:** Lead Junior Analyst  |  **Date:** 27 June 2026
**Data:** `citycab_clean.csv`  |  **Tools:** Python (Pandas, Matplotlib, Seaborn, SQLite)

---

## 1. Executive Summary

CityCab's recent ride export (10 raw rides) was cleaned to **9 valid rides** across 3 cities.
The analysis shows **Mumbai is the top-earning market (₹680 total fare)**, narrowly ahead of
**Pune (₹660)**, with Delhi well behind (₹310). Fare and distance are **strongly positively
correlated (+0.93)** — longer rides cost more, confirming the pricing model behaves sensibly.
Two clear data errors (a 200 km ride and a ₹5,000 fare) were detected and corrected. We
recommend **allocating more drivers to Mumbai and Pune, adding input validation to block
impossible distances/fares, and using the distance–fare relationship as a pricing sanity check.**

## 2. Business Problem

CityCab management asked for a complete analysis of a messy ride export to **improve operations**:
which city earns the most, how fare relates to distance, and whether the data can be trusted.

## 3. Dataset Description

| Property | Value |
|----------|-------|
| Source | CityCab ride export (raw) → `citycab_clean.csv` |
| Period | 1–8 May 2026 |
| Raw size | 10 rows × 6 columns |
| Clean size | **9 unique rides** × 6 columns (1 duplicate removed) |
| Columns | RideID, Driver, City, Distance, Fare, RideDate |

## 4. Data Cleaning Summary

| Issue found | Fix applied |
|-------------|-------------|
| Duplicate ride (RideID 3) | `drop_duplicates(subset=["RideID"])` |
| Missing fare (RideID 3) | filled with median (= ₹160) |
| Inconsistent text (`"  ravi"`, `"ASHA"`, `"meena "`, `"mumbai"`) | `.str.strip().str.title()` |
| Invalid distance (−4.0 km) | replaced with median of valid distances (= 7.25 km) |
| Outlier distance (200 km) | IQR-flagged (fence ≈ 22 km) → treated as error → median fill |
| Outlier fare (₹5,000) | IQR-flagged (fence ≈ ₹624) → treated as error → median fill |
| RideDate stored as text | `pd.to_datetime()` |

**Result:** a clean, validated dataset — **0 missing, 0 duplicates, all distances and fares
positive, correct data types.**

> *Note on the duplicate:* the two copies of RideID 3 differed (one fare was missing), so a
> full-row duplicate check would have missed it — we deduplicated on the **business key**
> (`RideID`) and then filled the remaining missing fare.

## 5. Key Findings

1. **Mumbai earns the most** total fare (**₹680**), just ahead of **Pune (₹660)**; **Delhi**
   trails at ₹310.
2. **Strong distance–fare relationship (+0.93).** Longer rides reliably cost more — the scatter
   plot shows a near-linear trend.
3. **Typical ride:** average fare **₹183**, average distance **7.4 km**.
4. **Two impossible values** (200 km, ₹5,000) were data-entry errors, now corrected.
5. **High-value rides (> ₹150):** led by Sahil (₹380, Pune) and Asha (₹300, Mumbai).

## 6. Visualizations

Saved at dpi=300 in [`charts/`](charts/):

| Chart | File | Interpretation |
|-------|------|----------------|
| Bar — Fare by City | `01_fare_by_city.png` | Mumbai & Pune are the top markets |
| Histogram — Fares | `02_fare_distribution.png` | Most fares are low; a few larger ones |
| Box plot — Fare | `03_fare_box.png` | Spread of fares after outlier removal |
| Scatter — Distance vs Fare | `04_distance_vs_fare.png` | Clear upward (positive) trend |
| Heatmap — Correlation | `05_correlation_heatmap.png` | Quantifies the +0.93 relationship |

## 7. Recommendations

1. **Allocate more drivers to Mumbai and Pune** — they generate almost all the fare; match
   supply to demand, especially at peak times.
2. **Add input validation** at ride logging — range checks would have blocked the 200 km
   distance, the −4 km value, and the ₹5,000 fare.
3. **Use the distance–fare relationship as a pricing check** — flag any ride that sits far off
   the +0.93 trend line as a possible mispricing or data error.

## 8. Conclusion

After cleaning, the data clearly shows that **Mumbai and Pune drive CityCab's fares**, and that
**fare scales predictably with distance**. The 200 km / ₹5,000 errors highlight a real
data-quality gap. Acting on these recommendations — rebalancing drivers, validating input, and
monitoring the distance–fare line — should improve both operations and data trustworthiness.
