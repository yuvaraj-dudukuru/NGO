# Mini Challenge — TrendMart Visual Performance Report

## The Scenario
You are a **junior data analyst at "TrendMart"**, a retail chain. The management
team wants a **visual report of the last six months** so they can decide where to
invest next. They hand you the data and ask for charts, comparisons, and clear
insights.

## The Data
A cleaned, six-month performance table:

| Column | Meaning |
|--------|---------|
| `Month`      | Month of the record (Jan–Jun) |
| `Revenue`    | Revenue earned that month |
| `AdSpend`    | Advertising spend that month |
| `Region`     | Sales region (North, South, East) |
| `OrderValue` | Value of an individual order |

## Requirements (and where each is solved in the code)
| # | Requirement | In the script |
|---|-------------|---------------|
| 1 | Inspect with `head()` and `describe()` | "STEP 1 — INSPECT THE DATA" |
| 2 | Line, Bar, Histogram, Scatter charts | "REQUIREMENTS 2 & 3" (2×2 dashboard) |
| 3 | Titles, axis labels, colors on every chart | Each chart block |
| 4 | Compare findings | "INSIGHTS & RECOMMENDATIONS" |
| 5 | Detect the outlier | "ANOMALY DETECTION" + correlation check |
| 6 | ≥ 3 insights, each with a recommendation | "INSIGHTS & RECOMMENDATIONS" (4 given) |
| 7 | Save a high-res PNG (`dpi=300`) | `plt.savefig(...)` |

Plus the **optional stretch goals**: a region-share pie chart and a two-line
Revenue-vs-AdSpend comparison chart.

## How to Run
1. Install the required libraries (one time only):
   ```bash
   pip install pandas matplotlib
   ```
2. Run the script:
   ```bash
   python trendmart_analysis.py
   ```
3. The script prints the analysis and insights to the terminal, opens chart
   windows, and saves three high-resolution images.

## Files Produced
| File | What it is |
|------|------------|
| `trendmart_dashboard.png`         | The main 2×2 dashboard (line, bar, histogram, scatter) |
| `trendmart_region_share.png`      | Stretch goal: pie chart of revenue share by region |
| `trendmart_revenue_vs_adspend.png`| Stretch goal: Revenue and Ad Spend as two lines |

## Expected Findings
- **Revenue trend (line):** Grows steadily from 120 → 300 — strong, consistent growth.
- **Revenue by region (bar):** East and South are strongest; North lags.
- **Order value (histogram):** Most orders are under 1000, but one order of **5000**
  stands out as a clear **outlier**.
- **Ad Spend vs Revenue (scatter):** A strong **positive relationship** —
  higher ad spend goes with higher revenue (correlation near +1).

## Insights & Recommendations
1. **Revenue is growing steadily** → *Sustain the current strategy.*
2. **East and South lead; North lags** → *Replicate East/South success in North.*
3. **One order of 5000 is an outlier** → *Follow up with that high-value customer.*
4. *(bonus)* **Ad spend correlates with revenue** → *Consider increasing ad spend,
   but test first — correlation is not causation.*

## Key Concepts Practiced
- `head()` and `describe()` for quick data inspection.
- `groupby().sum()` to aggregate revenue per region.
- Choosing the right chart: **line** (trend), **bar** (compare), **histogram**
  (distribution/outliers), **scatter** (relationship).
- `.corr()` to confirm a relationship numerically.
- Filtering with a condition (`data[data["OrderValue"] > 2000]`) to flag anomalies.
- Saving high-resolution figures with `dpi=300`.
- **Storytelling:** turning charts into insights, and insights into recommendations.

> **Tip:** Try solving it yourself first, then compare with this sample solution.
