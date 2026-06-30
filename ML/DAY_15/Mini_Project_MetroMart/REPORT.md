# MetroMart — Customer Behaviour Analysis Report

**Prepared by:** Data Analytics
**Dataset:** 16 customers (synthetic) — Age, Annual Spending, Visits, Average Basket Value

---

## 1. Central tendency
| Statistic | Spending |
|-----------|----------|
| Mean | 27,437.5 |
| Median | 20,000 |
| Mode | 20,000 |

The **mean (27,438) sits well above the median (20,000)** — about 37% higher.
This gap is the classic signature of a **right-skewed** distribution: a small
number of very large values pull the average upward, so the mean overstates the
"typical" customer. The **median (20,000)** is the honest measure of the typical
customer.

## 2. Dispersion
| Statistic | Spending |
|-----------|----------|
| Range | 144,000 (6,000 → 150,000) |
| Standard deviation | 33,704.5 |
| Q1 / Q3 | 12,750 / 28,250 |
| IQR | 15,500 |

Spending is **highly variable**. Note that the standard deviation (33,705) is
larger than the IQR (15,500); the IQR describes the middle 50% of customers
(12,750–28,250), while the inflated standard deviation is driven by the single
extreme value. The middle of the customer base is actually fairly tight — the
spread is dominated by one outlier.

## 3. Distribution shape
With **mean − median = +7,438 (+37% of the median)**, the spending distribution
is **right-skewed (positively skewed)**, not symmetric or bimodal. Reporting the
mean alone would mislead stakeholders.

## 4. Percentiles — the top 10%
The **90th-percentile threshold is 31,500**. Customers at or above it are the
top tier:

| Customer | Spending |
|----------|----------|
| C16 | 150,000 |
| C15 | 33,000 |

These are MetroMart's most valuable customers and should be managed as a
distinct, high-priority segment.

## 5. Correlation
Correlation matrix (Pearson):

|              | Age | Spending | Visits | BasketValue |
|--------------|-----|----------|--------|-------------|
| Age          | 1.00 | 0.11 | -0.17 | -0.11 |
| Spending     | 0.11 | 1.00 | **0.73** | **0.92** |
| Visits       | -0.17 | 0.73 | 1.00 | **0.93** |
| BasketValue  | -0.11 | 0.92 | 0.93 | 1.00 |

- **Strongest relationship:** Visits ↔ BasketValue (**r = 0.93**) — customers who
  come more often also tend to buy larger baskets.
- **Spending is strongly tied to both basket value (r = 0.92) and visits
  (r = 0.73)** — unsurprising, since annual spending is essentially visits ×
  basket value.
- **Age is essentially unrelated** to spending, visits, or basket value
  (|r| ≤ 0.17).

> **Correlation ≠ causation.** A high correlation between visits and basket value
> (or between visits and spending) does not prove one *causes* the other. A third
> factor — customer loyalty, disposable income, or a promotion — could drive both
> at once. Experiments (e.g. A/B-tested loyalty incentives) would be needed to
> establish causation.

## 6. Outlier detection
Two independent methods agree on a single outlier:

| Method | Rule | Flagged |
|--------|------|---------|
| IQR | spending > Q3 + 1.5·IQR = 51,500 | **C16 (150,000)** |
| Z-score | \|z\| > 3 | **C16 (z = 3.76)** |

- **Business explanation:** C16 is most likely a **genuine high-value customer**
  (bulk/wholesale buyer or premium account), not a data-entry error — their
  visits (20) and basket value (4,000) are also the highest, which is internally
  consistent.
- **Treatment:** **Keep the record.** For describing the *typical* customer, use
  the **median** so this customer doesn't distort the picture. Analyse C16 (and
  the top tier) as a **separate high-value segment** rather than discarding the
  data.

## 7. Insights & recommendations

### Typical customer profile (medians)
Age ≈ 34, Annual spending ≈ 20,000, Visits ≈ 10, Average basket ≈ 1,950.

### Most valuable customers
**C16** (150,000) is the single most valuable customer by a wide margin, followed
by **C15** (33,000). Together they form the top 10% (spending ≥ 31,500).

### Key relationships
Visit frequency and basket value move together (r = 0.93) and both drive annual
spending (r = 0.73 and 0.92). Age does not predict spending.

### Recommendations
1. **Report the median, not the mean.** Plan capacity, targets, and "average
   customer" messaging around the **median (~20,000)**; the mean (27,438) is
   inflated by one outlier and will mislead.
2. **Grow spending through its two strongest drivers — visit frequency and
   basket size.** Use loyalty programs and app nudges to increase visits, and
   bundling / upselling to increase basket value. (Treat these as hypotheses to
   validate with controlled tests, given the correlation-vs-causation caveat.)
3. **Build a high-value-customer program.** Give the top 10% (C16, C15) dedicated
   account management, early access, and premium perks to protect and grow this
   disproportionately valuable revenue.
4. **Don't segment on age.** Age shows no meaningful link to value here, so
   target on *behaviour* (visits, basket value, spending tier) instead of
   demographics.

---

*All figures in this report were computed by `metromart_analysis.py` and verified
by executing the script on the dataset described in the README.*
