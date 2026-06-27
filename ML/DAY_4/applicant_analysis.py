"""
TechHire - Job Applicant Analysis
=================================
A quick exploratory data analysis (EDA) of a job-applicant dataset using Pandas.

What is EDA? It is the first step of any data project: we "get to know" the data
by looking at its size, summarizing it, filtering it, and pulling out insights
before doing anything more advanced.

Author: TechHire Data Analyst
"""

# 'import pandas as pd' loads the Pandas library and gives it the short
# nickname 'pd'. From now on we write 'pd.something' instead of 'pandas.something'.
# Pandas is the standard Python tool for working with tables of data (DataFrames).
import pandas as pd


def build_dataset() -> pd.DataFrame:
    """Create the applicants dataset (simulates loading a real file).

    In a real job you would usually read a CSV/Excel file, e.g.
        pd.read_csv("applicants.csv")
    Here we build the same kind of table by hand so the project is self-contained.
    """
    # A DataFrame is a table (rows + columns), like a spreadsheet.
    # We build it from a dictionary: each key is a COLUMN name, and each value
    # is a LIST holding that column's values, one per applicant (per row).
    # All lists must be the same length (8 here) so the rows line up.
    return pd.DataFrame({
        "Name": ["Asha", "Ravi", "Imran", "Divya", "Karan", "Meena", "Sahil", "Tara"],
        "Age": [25, 32, 28, 45, 23, 38, 29, 41],
        "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Pune", "Delhi", "Mumbai"],
        "Experience": [2, 8, 4, 20, 1, 12, 5, 17],
        "Expected_Salary": [40000, 90000, 55000, 150000, 35000, 110000, 60000, 130000],
    })


def inspect(df: pd.DataFrame) -> None:
    """1. Load / inspect the dataset.

    The goal here is just to answer: "How big is the data and what's in it?"
    """
    # These print lines are just headers to keep the console output readable.
    print("=" * 60)
    print("1. INSPECT")
    print("=" * 60)

    # .shape returns a tuple (number_of_rows, number_of_columns) -> (8, 5).
    print("Shape:", df.shape)

    # .columns lists the column names. .tolist() turns it into a plain Python
    # list so it prints cleanly as ['Name', 'Age', ...].
    print("Columns:", df.columns.tolist())

    # .head() shows the FIRST 5 rows by default - a quick peek at the data.
    print("\nHead:")
    print(df.head())


def explore(df: pd.DataFrame) -> None:
    """2. Explore with describe() and value_counts()."""
    print("\n" + "=" * 60)
    print("2. EXPLORE")
    print("=" * 60)

    # .describe() computes summary statistics for every NUMERIC column:
    # count, mean (average), std (spread), min, the 25/50/75% quartiles, and max.
    # This instantly tells us the typical and extreme values.
    print("Statistical summary:")
    print(df.describe())

    # df["City"] selects a single column (called a Series).
    # .value_counts() counts how many times each unique value appears,
    # so here it tells us how many applicants come from each city.
    print("\nApplicants per city:")
    print(df["City"].value_counts())


def filter_data(df: pd.DataFrame) -> None:
    """3. Filter the data (keep only the rows that match a condition)."""
    print("\n" + "=" * 60)
    print("3. FILTER")
    print("=" * 60)

    # df["Experience"] > 5 creates a column of True/False values (a "mask"),
    # one per row. Putting that mask inside df[...] keeps ONLY the rows
    # where the value is True -> applicants with more than 5 years experience.
    print("Experienced applicants (> 5 years):")
    print(df[df["Experience"] > 5])

    # To combine two conditions we wrap each in ( ) and join them with '&' (AND).
    # Note: in Pandas use '&' for AND and '|' for OR (NOT the words 'and'/'or').
    # This keeps rows that are in Mumbai AND expect more than 100,000.
    print("\nMumbai applicants expecting > 100,000:")
    print(df[(df["City"] == "Mumbai") & (df["Expected_Salary"] > 100000)])


def statistics(df: pd.DataFrame) -> None:
    """4. Calculate statistics on individual columns."""
    print("\n" + "=" * 60)
    print("4. STATISTICS")
    print("=" * 60)

    # .mean() = average of the column. .max()/.min() = largest/smallest value.
    # We call them on a single column (a Series) to get a single number back.
    print("Average expected salary:", df["Expected_Salary"].mean())
    print("Max experience:", df["Experience"].max())
    print("Min experience:", df["Experience"].min())


def top_earners(df: pd.DataFrame) -> None:
    """5. Sort by expected salary (descending) and show the top 3."""
    print("\n" + "=" * 60)
    print("5. TOP 3 BY EXPECTED SALARY")
    print("=" * 60)

    # .sort_values("Expected_Salary", ascending=False) reorders the rows from
    # highest salary to lowest. .head(3) then keeps the first 3 rows = top 3.
    print(df.sort_values("Expected_Salary", ascending=False).head(3))


def stretch_goals(df: pd.DataFrame) -> None:
    """Optional stretch goals: new column, grouping, and a 'best' lookup."""
    print("\n" + "=" * 60)
    print("STRETCH GOALS")
    print("=" * 60)

    # .copy() makes a separate copy of the table so the new column we add here
    # does not accidentally change the original DataFrame used elsewhere.
    df = df.copy()

    # Create a NEW column by dividing two existing columns element-by-element.
    # .clip(lower=1) forces any experience below 1 up to 1, which avoids
    # dividing by 0 (or by tiny numbers) that would give misleading results.
    # .round(2) keeps the result to 2 decimal places for readability.
    df["Salary_Per_Year_Exp"] = (df["Expected_Salary"] / df["Experience"].clip(lower=1)).round(2)
    print("Salary per year of experience:")
    # df[[...]] with a LIST of column names selects MULTIPLE columns to display.
    print(df[["Name", "Experience", "Expected_Salary", "Salary_Per_Year_Exp"]])

    # .groupby("City") splits the rows into groups by city, then we pick the
    # Expected_Salary column and take the .mean() of each group -> average
    # salary expectation per city.
    avg_by_city = df.groupby("City")["Expected_Salary"].mean()
    print("\nAverage expected salary per city:")
    print(avg_by_city)

    # .idxmax() returns the INDEX (here, the city name) of the largest value,
    # i.e. the city with the highest average expected salary.
    print("\nCity with highest average expected salary:", avg_by_city.idxmax())


def conclusions() -> None:
    """6. Written observations about the applicant pool.

    These are plain-English takeaways a human would write after looking at the
    numbers above - the real point of an analysis.
    """
    print("\n" + "=" * 60)
    print("6. CONCLUSIONS")
    print("=" * 60)

    # A list of the observations; we loop over it below to print them numbered.
    observations = [
        "The dataset has 8 applicants across 5 columns, with Pune and Mumbai "
        "being the most common cities.",
        "Four applicants (Ravi, Divya, Meena, Tara) have more than 5 years of "
        "experience, forming the senior segment of the pool.",
        "Expected salary tracks experience closely - the highest expectations "
        "(Divya, Tara, Meena) come from the most experienced applicants.",
        "The average expected salary is about 83,750, ranging widely from "
        "35,000 (Karan) to 150,000 (Divya).",
    ]
    # enumerate(..., 1) gives us a counter starting at 1 along with each item,
    # so we can print "1. ...", "2. ...", etc.
    for i, obs in enumerate(observations, 1):
        print(f"{i}. {obs}")


def main() -> None:
    """Run the whole analysis from start to finish, step by step."""
    df = build_dataset()   # create the table
    inspect(df)            # step 1
    explore(df)            # step 2
    filter_data(df)        # step 3
    statistics(df)         # step 4
    top_earners(df)        # step 5
    stretch_goals(df)      # optional extras
    conclusions()          # step 6


# This standard Python guard means: "only run main() when this file is executed
# directly (python applicant_analysis.py)". If the file were imported by another
# script instead, main() would NOT run automatically.
if __name__ == "__main__":
    main()
