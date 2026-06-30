"""
Mini Project - MetroMart Customer Statistical Analysis
======================================================

Role:
    Data analyst at MetroMart, a retail company.

Task:
    Conduct a complete statistical analysis of customer transactions to
    characterize customer behaviour, identify relationships, detect anomalies,
    and produce business recommendations.

The dataset is synthetic (no real customer data). It is constructed so that:
  * spending is right-skewed and contains a clear high-value outlier (C16);
  * visits and spending are positively related;
  * one spending value repeats so the mode is meaningful.

Run:
    python metromart_analysis.py
"""

import numpy as np
import pandas as pd


def build_dataset() -> pd.DataFrame:
    """Construct the synthetic MetroMart customer dataset (16 customers)."""
    df = pd.DataFrame(
        {
            "Customer": [f"C{i}" for i in range(1, 17)],
            "Age": [25, 32, 28, 45, 31, 52, 29, 38, 41, 36, 48, 27, 33, 55, 30, 44],
            "Spending": [
                12000, 25000, 8000, 30000, 18000, 10000, 22000, 15000,
                28000, 20000, 13000, 29000, 20000, 6000, 33000, 150000,
            ],
            "Visits": [5, 12, 3, 15, 8, 4, 11, 7, 13, 9, 6, 14, 10, 2, 16, 20],
            "BasketValue": [
                1500, 2000, 1200, 2200, 1800, 1300, 2100, 1600,
                2150, 1900, 1400, 2300, 2000, 1100, 2500, 4000,
            ],
        }
    )
    return df


def section(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def central_tendency(df: pd.DataFrame) -> None:
    """Mean, median, and mode - the three "typical value" measures.

    Comparing mean vs median is the quickest skew check: if the mean is dragged
    above the median, a few large values are pulling it up (right skew).
    """
    section("1. CENTRAL TENDENCY (Spending)")
    mean = df["Spending"].mean()
    median = df["Spending"].median()
    mode = df["Spending"].mode().tolist()
    print(f"Mean:   {mean:,.1f}")
    print(f"Median: {median:,.1f}")
    print(f"Mode:   {mode}")
    if mean > median:
        print("-> Mean > Median: distribution is RIGHT-SKEWED (pulled up by high values).")
    elif mean < median:
        print("-> Mean < Median: distribution is LEFT-SKEWED.")
    else:
        print("-> Mean == Median: distribution is roughly SYMMETRIC.")


def dispersion(df: pd.DataFrame) -> None:
    """How spread out the data is: range, standard deviation, and the IQR.

    Std is sensitive to outliers; the IQR (middle 50%) is not. When std looks
    large but the IQR is modest, the spread is being driven by extreme values.
    """
    section("2. DISPERSION (Spending)")
    spending = df["Spending"]
    rng = spending.max() - spending.min()
    std = spending.std()
    q1, q3 = spending.quantile(0.25), spending.quantile(0.75)
    iqr = q3 - q1
    print(f"Range:              {rng:,.1f}  (min {spending.min():,} to max {spending.max():,})")
    print(f"Standard deviation: {std:,.1f}")
    print(f"Q1 / Q3:            {q1:,.1f} / {q3:,.1f}")
    print(f"IQR:                {iqr:,.1f}")
    print("-> A large std relative to the IQR indicates the spread is driven by extreme values.")


def distribution(df: pd.DataFrame) -> None:
    """Classify the distribution shape from the mean-vs-median gap.

    A gap beyond +/-10% of the median is treated as meaningful skew; otherwise
    the distribution is considered roughly symmetric.
    """
    section("3. DISTRIBUTION SHAPE (Spending)")
    mean = df["Spending"].mean()
    median = df["Spending"].median()
    diff_pct = (mean - median) / median * 100
    print(f"Mean - Median = {mean - median:,.1f}  ({diff_pct:+.1f}% of the median)")
    if diff_pct > 10:
        shape = "RIGHT-SKEWED"
    elif diff_pct < -10:
        shape = "LEFT-SKEWED"
    else:
        shape = "approximately SYMMETRIC"
    print(f"-> Based on the mean-vs-median gap, the distribution is {shape}.")


def percentiles(df: pd.DataFrame) -> None:
    """Use the 90th percentile to isolate the top 10% of spenders.

    A percentile is the value below which that share of the data falls, so the
    90th-percentile threshold cleanly separates the highest-value customers.
    """
    section("4. PERCENTILES - TOP 10% OF CUSTOMERS (Spending)")
    threshold = df["Spending"].quantile(0.90)
    top = df[df["Spending"] >= threshold].sort_values("Spending", ascending=False)
    print(f"90th-percentile threshold: {threshold:,.1f}")
    print("Customers in the top 10% of spending:")
    print(top[["Customer", "Spending"]].to_string(index=False))


def correlation(df: pd.DataFrame) -> None:
    """Pairwise correlations between the numeric columns.

    r ranges from -1 to +1: near +1 = move together, near -1 = move oppositely,
    near 0 = no linear link. We report the strongest pair, with the standard
    "correlation is not causation" caveat.
    """
    section("5. CORRELATION MATRIX")
    cols = ["Age", "Spending", "Visits", "BasketValue"]
    corr = df[cols].corr()
    print(corr.round(2).to_string())

    # Strongest relationship (ignore the diagonal / self-correlations).
    pairs = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            pairs.append((cols[i], cols[j], corr.iloc[i, j]))
    a, b, r = max(pairs, key=lambda p: abs(p[2]))
    vs = corr.loc["Visits", "Spending"]
    print(f"\n-> Strongest relationship: {a} <-> {b}  (r = {r:.2f})")
    print(f"-> Visits <-> Spending is moderate-to-strong (r = {vs:.2f}).")
    print(f"-> CAVEAT: correlation does not imply causation. A strong r between")
    print(f"   {a} and {b} does not prove that one CAUSES the other; a third")
    print("   factor (loyalty, income, or promotions) may drive both.")


def outliers(df: pd.DataFrame) -> None:
    """Detect anomalies two ways: the IQR rule and the Z-score rule.

    IQR: anything outside Q1-1.5*IQR .. Q3+1.5*IQR is an outlier (robust).
    Z-score: how many std devs a value is from the mean; |z|>3 is extreme. Note
    a single dominant outlier inflates the std and can hide its own z-score - a
    good lesson in why no single method is sufficient.
    """
    section("6. OUTLIER DETECTION (Spending)")
    spending = df["Spending"]

    # IQR method
    q1, q3 = spending.quantile(0.25), spending.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    iqr_out = df[(spending < lower) | (spending > upper)]
    print(f"IQR method   -> bounds [{lower:,.1f}, {upper:,.1f}]")
    print(iqr_out[["Customer", "Spending"]].to_string(index=False) or "  none")

    # Z-score method (population std, ddof=0)
    mean, std = spending.mean(), spending.std(ddof=0)
    z = (spending - mean) / std
    df_z = df.assign(Z=z.round(2))
    z_out = df_z[df_z["Z"].abs() > 3]
    print(f"\nZ-score method -> |z| > 3   (mean {mean:,.1f}, std {std:,.1f})")
    if z_out.empty:
        z_out = df_z[df_z["Z"].abs() > 2]
        print("  (no |z| > 3; showing |z| > 2 instead - the single dominant")
        print("   outlier inflates the std, shrinking its own z-score)")
    print(z_out[["Customer", "Spending", "Z"]].to_string(index=False))

    print("\n-> Business explanation: the flagged customer is a genuine high-value")
    print("   shopper (e.g. bulk/wholesale or premium buyer), not a data error.")
    print("-> Treatment: keep the record, but report the MEDIAN for 'typical'")
    print("   customers and analyse high-value customers as a separate segment.")


def recommendations(df: pd.DataFrame) -> None:
    """Translate the statistics into a typical-customer profile and actions.

    Deliberately profiles the "typical" customer with MEDIANS (robust to the
    high-value outlier) and turns the strongest correlations into levers to pull.
    """
    section("7. INSIGHTS & RECOMMENDATIONS")
    median = df["Spending"].median()
    top_customer = df.loc[df["Spending"].idxmax()]
    print("Typical customer profile (using medians):")
    print(f"  Age ~ {df['Age'].median():.0f}, Spending ~ {median:,.0f}, "
          f"Visits ~ {df['Visits'].median():.0f}, Basket ~ {df['BasketValue'].median():,.0f}")
    print(f"\nMost valuable customer: {top_customer['Customer']} "
          f"(spending {top_customer['Spending']:,})")
    print("\nRecommendations:")
    print("  1. Plan around the MEDIAN customer (~20,000), not the inflated mean.")
    print("  2. Grow spending through its two strongest drivers - visit FREQUENCY")
    print("     (loyalty programs, app nudges) and BASKET size (bundling, upsell).")
    print("  3. Protect and grow high-value customers (top 10%) with dedicated")
    print("     account management and premium perks.")


def main() -> None:
    df = build_dataset()
    section("DATASET")
    print(df.to_string(index=False))

    central_tendency(df)
    dispersion(df)
    distribution(df)
    percentiles(df)
    correlation(df)
    outliers(df)
    recommendations(df)


if __name__ == "__main__":
    main()
