# Case Study 1 — Sales Analysis Dashboard

## Objective
Build a small multi-chart **dashboard** that combines three different charts into
one figure, then read them together to tell a complete business story.

## The Charts
| # | Chart Type | Question It Answers |
|---|------------|---------------------|
| 1 | **Line chart**  | Is revenue growing over time? |
| 2 | **Bar chart**   | Which product earns the most? |
| 3 | **Histogram**   | How are order values distributed? Any outliers? |

## The Data
A 6-month sales table with these columns:

| Column | Meaning |
|--------|---------|
| `Month`      | The month of the record (Jan–Jun) |
| `Revenue`    | Revenue earned that month |
| `Product`    | Product sold (A, B, or C) |
| `OrderValue` | Value of an individual order |

## How to Run
1. Install the required libraries (one time only):
   ```bash
   pip install pandas matplotlib
   ```
2. Run the script:
   ```bash
   python sales_dashboard.py
   ```
3. A window opens with the dashboard, and an image `sales_dashboard.png` is saved
   in the same folder.

## What You Should See
A single wide figure with three charts side by side.

## Interpreting the Dashboard
- **Line chart (Revenue Trend):** Revenue climbs steadily from 120 to 300 — strong,
  consistent growth.
- **Bar chart (Revenue by Product):** Product C contributes the most revenue —
  the top performer.
- **Histogram (Order Value Distribution):** Most orders are small (under 1000),
  but one order of 5000 sits alone in a high bin — a clear **outlier**.

### Combined Insight
> The business is growing, driven largely by Product C, and there is one
> exceptional high-value order worth investigating.

### Recommendation
> Sustain growth, promote Product C, and follow up with the high-value customer.

## Key Concepts Practiced
- Creating a `DataFrame`
- `plt.subplots()` to place multiple charts in one figure
- `groupby().sum()` to aggregate data before plotting
- Line chart vs. bar chart vs. histogram — when to use each
- Spotting an **outlier** visually
