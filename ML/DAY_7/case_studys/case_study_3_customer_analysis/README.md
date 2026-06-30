# Case Study 3 — Customer Dataset Analysis

## Objective
Explore a customer dataset (**EDA — Exploratory Data Analysis**) with three
charts, and uncover a key contrast: the city with the **most customers** is not
necessarily the city that **spends the most**.

## The Charts
| # | Chart Type | Question It Answers |
|---|------------|---------------------|
| 1 | **Pie chart**   | What share of customers comes from each city? |
| 2 | **Bar chart**   | What is the average spend per city? |
| 3 | **Histogram**   | How are customer ages distributed? |

## The Data
| Column | Meaning |
|--------|---------|
| `City`       | The city the customer lives in |
| `Age`        | The customer's age |
| `TotalSpent` | Total amount the customer has spent |

## How to Run
1. Install the required libraries (one time only):
   ```bash
   pip install pandas matplotlib
   ```
2. Run the script:
   ```bash
   python customer_analysis.py
   ```
3. A window opens with the report, and an image `customer_analysis.png` is saved
   in the same folder.

## Interpreting the Report
- **Pie chart:** Mumbai has the largest customer share — the biggest customer base.
- **Bar chart:** Average spend is highest in Delhi, even though it has fewer
  customers — revealing **high-value customers** there.
- **Histogram:** Customers span a wide age range, with most in their late twenties
  to early thirties.

### Combined Insight
> Mumbai brings volume; Delhi brings high spenders. Our core customers are
> young adults.

### Recommendation
> Grow the customer base in Delhi to capture more high-value spenders, and tailor
> marketing to young adults.

## Key Concepts Practiced
- **Pie chart** for showing shares/proportions of a whole.
- `value_counts()` to count occurrences of each category.
- `groupby().mean()` to compute an average per group.
- **Histogram** for understanding the distribution of a numeric column (age).
- Spotting a **contrast** between volume (count) and value (average spend).
