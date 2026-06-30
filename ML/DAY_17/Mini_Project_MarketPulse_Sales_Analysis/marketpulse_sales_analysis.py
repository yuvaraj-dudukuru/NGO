"""
Mini Project — MarketPulse Two-Year Daily Sales: Time Series Analysis
=====================================================================

Role:
    Data analyst at MarketPulse, a retail company.

Problem:
    Given two years of daily sales data, conduct a complete time series analysis:
    assess performance over time, identify trend and seasonality, compute growth
    KPIs (including a seasonality-adjusted year-over-year figure), visualize the
    series, and produce business recommendations.

Pipeline (matches the seven required analysis sections):
    1. Date handling      — datetime index; extract year, quarter, month, day name
    2. Aggregation        — monthly and quarterly totals
    3. Trend              — moving average
    4. Seasonality        — strongest months/quarters; recurrence across years
    5. Growth KPIs        — month-over-month and year-over-year (peak quarter)
    6. Visualization      — daily + moving average; two-year monthly comparison
    7. Insights & report  — printed summary with recommendations

Run:
    python marketpulse_sales_analysis.py

Outputs:
    charts/daily_sales_trend.png
    charts/yearly_monthly_comparison.png

Requires:
    numpy, pandas, matplotlib
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # headless backend so the script runs without a display
import matplotlib.pyplot as plt  # noqa: E402

CHARTS_DIR = Path(__file__).resolve().parent / "charts"


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------
def build_dataset() -> pd.DataFrame:
    """Construct ~730 days of daily sales with trend + annual seasonality + noise.

    - trend     : a straight line rising over the two years (real growth)
    - seasonal  : an annual sine wave engineered to peak in the final quarter
    - noise     : small random day-to-day variation

    A fixed random seed makes the series fully reproducible. The DataFrame uses a
    DatetimeIndex, as required.
    """
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=730, freq="D")
    n = len(dates)

    trend = np.linspace(1000, 1800, n)  # upward trend across two years

    # Annual seasonality: sin peaks at argument pi/2. Phase 238.75 places the
    # peak near day-of-year ~330 (late November) so every year peaks in Q4.
    day_of_year = dates.dayofyear.to_numpy()
    seasonal = 300 * np.sin(2 * np.pi * (day_of_year - 238.75) / 365.25)

    noise = np.random.normal(0, 40, n)

    sales = (trend + seasonal + noise).round(0)

    df = pd.DataFrame({"Sales": sales}, index=dates)
    df.index.name = "Date"
    return df


# ---------------------------------------------------------------------------
# 1. Date handling
# ---------------------------------------------------------------------------
def add_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """Confirm the index is datetime and extract calendar features."""
    print("=" * 70)
    print("1. DATE HANDLING")
    print("=" * 70)
    print("Index is a DatetimeIndex:", isinstance(df.index, pd.DatetimeIndex))
    print("Index dtype           :", df.index.dtype)
    print("Date range            :", df.index.min().date(), "->", df.index.max().date())
    print("Number of days        :", len(df))

    df["Year"] = df.index.year
    df["Quarter"] = df.index.quarter
    df["Month"] = df.index.month
    df["MonthName"] = df.index.month_name()
    df["DayName"] = df.index.day_name()

    print("\nFirst rows with extracted features:")
    print(df[["Sales", "Year", "Quarter", "Month", "DayName"]].head())
    return df


# ---------------------------------------------------------------------------
# 2. Aggregation
# ---------------------------------------------------------------------------
def aggregate(df: pd.DataFrame):
    """Aggregate daily sales into monthly and quarterly totals."""
    print("\n" + "=" * 70)
    print("2. AGGREGATION")
    print("=" * 70)

    monthly = df["Sales"].resample("ME").sum()
    quarterly = df["Sales"].resample("QE").sum()

    print("Monthly totals (first 6):")
    print(monthly.head(6).round(0))
    print("\nQuarterly totals (all):")
    print(quarterly.round(0))
    return monthly, quarterly


# ---------------------------------------------------------------------------
# 3. Trend identification
# ---------------------------------------------------------------------------
def add_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Smooth the daily series with moving averages and describe the trend."""
    print("\n" + "=" * 70)
    print("3. TREND IDENTIFICATION (moving average)")
    print("=" * 70)

    # 30-day window smooths weekly/noise; 90-day window smooths even more,
    # leaving a clean rising baseline once short-term wobble is removed.
    df["MA_30"] = df["Sales"].rolling(window=30, center=True).mean()
    df["MA_90"] = df["Sales"].rolling(window=90, center=True).mean()

    annual_mean = df.groupby("Year")["Sales"].mean().round(1)
    print("Average daily sales by year:")
    print(annual_mean)
    change = (annual_mean.iloc[-1] - annual_mean.iloc[0]) / annual_mean.iloc[0] * 100
    print(f"\nYear-over-year change in average daily sales: {change:.1f}%")
    print("Interpretation: the moving average rises across both years -> upward trend.")
    return df


# ---------------------------------------------------------------------------
# 4. Seasonality analysis
# ---------------------------------------------------------------------------
def analyze_seasonality(df: pd.DataFrame):
    """Find the strongest months/quarters and confirm recurrence across years."""
    print("\n" + "=" * 70)
    print("4. SEASONALITY ANALYSIS")
    print("=" * 70)

    month_avg = df.groupby("MonthName")["Sales"].mean().round(0)
    # Order months calendar-wise for readability.
    month_order = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    month_avg = month_avg.reindex(month_order)
    print("Average daily sales by month (both years combined):")
    print(month_avg)

    quarter_avg = df.groupby("Quarter")["Sales"].mean().round(0)
    print("\nAverage daily sales by quarter:")
    print(quarter_avg)
    print("Strongest quarter overall: Q%d" % int(quarter_avg.idxmax()))

    # Recurrence: which quarter is strongest within EACH year?
    q_by_year = df.groupby(["Year", "Quarter"])["Sales"].sum().unstack("Year").round(0)
    print("\nQuarterly totals by year (rows = quarter, columns = year):")
    print(q_by_year)
    strongest_per_year = q_by_year.idxmax()
    print("\nStrongest quarter in each year:")
    for year, q in strongest_per_year.items():
        print(f"  {year}: Q{int(q)}")
    recurs = strongest_per_year.nunique() == 1
    print("Seasonal peak recurs in the same quarter both years:", recurs)
    return month_avg, quarter_avg, q_by_year


# ---------------------------------------------------------------------------
# 5. Growth KPIs
# ---------------------------------------------------------------------------
def growth_kpis(df: pd.DataFrame, monthly: pd.Series):
    """Month-over-month growth and year-over-year growth for the peak quarter."""
    print("\n" + "=" * 70)
    print("5. GROWTH KPIs")
    print("=" * 70)

    mom = (monthly.pct_change() * 100).round(1)
    print("Month-over-month growth %% (first 6):")
    print(mom.head(6))
    print(f"Average month-over-month growth: {mom.mean():.1f}%")
    print("Note: MoM is volatile here because it mixes growth with the annual"
          " seasonal swing (e.g. the Q4 climb and the post-peak fall).")

    # Year-over-year for the peak quarter (Q4) — compares like with like season.
    q4 = df[df["Quarter"] == 4].groupby("Year")["Sales"].sum()
    yoy_q4 = (q4.iloc[-1] - q4.iloc[0]) / q4.iloc[0] * 100

    annual_total = df.groupby("Year")["Sales"].sum()
    yoy_annual = (annual_total.iloc[-1] - annual_total.iloc[0]) / annual_total.iloc[0] * 100

    print("\nQ4 (peak quarter) total by year:")
    print(q4.round(0))
    print(f"\nYear-over-year Q4 growth : {yoy_q4:.1f}%")
    print(f"Year-over-year total growth: {yoy_annual:.1f}%")
    print("\nWhy YoY is the more reliable measure:")
    print("  Comparing the same quarter across years holds the season constant,")
    print("  so the change reflects REAL growth rather than the seasonal cycle.")
    return mom, yoy_q4, yoy_annual


# ---------------------------------------------------------------------------
# 6. Visualization
# ---------------------------------------------------------------------------
def visualize(df: pd.DataFrame):
    """Save (a) daily sales + moving average and (b) two-year monthly comparison."""
    print("\n" + "=" * 70)
    print("6. VISUALIZATION")
    print("=" * 70)
    CHARTS_DIR.mkdir(exist_ok=True)

    # Chart 1: daily sales with the moving-average trend line.
    plt.figure(figsize=(13, 5))
    plt.plot(df.index, df["Sales"], alpha=0.35, label="Daily Sales")
    plt.plot(df.index, df["MA_30"], color="red", linewidth=2,
             label="30-Day Moving Average")
    plt.plot(df.index, df["MA_90"], color="black", linewidth=2, linestyle="--",
             label="90-Day Moving Average")
    plt.title("MarketPulse — Daily Sales with Moving-Average Trend (2 Years)")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.tight_layout()
    chart1 = CHARTS_DIR / "daily_sales_trend.png"
    plt.savefig(chart1, dpi=120)
    plt.close()

    # Chart 2: monthly totals for each year, overlaid to compare the patterns.
    monthly_by_year = (
        df.groupby(["Year", "Month"])["Sales"].sum().unstack("Year")
    )
    plt.figure(figsize=(11, 5))
    for year in monthly_by_year.columns:
        plt.plot(monthly_by_year.index, monthly_by_year[year],
                 marker="o", linewidth=2, label=str(year))
    plt.title("MarketPulse — Monthly Sales Pattern: Year 1 vs Year 2")
    plt.xlabel("Month")
    plt.ylabel("Monthly Total Sales")
    plt.xticks(range(1, 13))
    plt.legend(title="Year")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    chart2 = CHARTS_DIR / "yearly_monthly_comparison.png"
    plt.savefig(chart2, dpi=120)
    plt.close()

    print("Saved:", chart1.name)
    print("Saved:", chart2.name)


# ---------------------------------------------------------------------------
# 7. Insights & recommendations
# ---------------------------------------------------------------------------
def report(df: pd.DataFrame, yoy_q4: float, yoy_annual: float):
    """Print the closing business report."""
    print("\n" + "=" * 70)
    print("7. INSIGHTS & RECOMMENDATIONS")
    print("=" * 70)
    print(
        "TREND       : A genuine upward trend runs across both years; the moving\n"
        "              average rises steadily once noise and seasonality are smoothed.\n"
        "SEASONALITY : A strong, recurring final-quarter (Q4) peak appears in BOTH\n"
        "              years, with the slow period in mid-year (Q2).\n"
        f"GROWTH      : Year-over-year Q4 growth is +{yoy_q4:.1f}% and total YoY growth\n"
        f"              is +{yoy_annual:.1f}% - positive growth that is real, not just\n"
        "              the seasonal effect (YoY holds the season constant).\n"
        "\nRECOMMENDATIONS:\n"
        "  1. INVENTORY: Build stock and staffing ahead of Q4 every year to capture\n"
        "     the recurring seasonal peak without stockouts; keep stock lean in the\n"
        "     mid-year low to reduce holding costs.\n"
        "  2. SUSTAIN GROWTH: The positive YoY figure confirms the strategy is\n"
        "     working beyond seasonality - keep investing in what drives the trend.\n"
        "  3. PLAN ON YoY, NOT MoM: Use year-over-year (same-season) comparisons for\n"
        "     targets and reporting, since month-over-month is distorted by the\n"
        "     annual cycle.\n"
        "  4. MARKETING TIMING: Concentrate campaigns and promotions in the Q4 ramp\n"
        "     to amplify the period that already converts best."
    )


def main() -> None:
    df = build_dataset()
    df = add_date_features(df)
    monthly, quarterly = aggregate(df)
    df = add_trend(df)
    analyze_seasonality(df)
    mom, yoy_q4, yoy_annual = growth_kpis(df, monthly)
    visualize(df)
    report(df, yoy_q4, yoy_annual)


if __name__ == "__main__":
    main()
