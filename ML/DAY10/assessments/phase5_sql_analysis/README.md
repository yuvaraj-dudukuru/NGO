# Phase 5 — SQL Analysis

**Goal:** Answer the **same** business questions using SQL (Day 9), proving the analysis can be
done directly in a database — not only in Pandas.

## The bridge: Pandas → SQL

We load the **cleaned** DataFrame into an in-memory SQLite database with `df.to_sql("sales", …)`,
then query it with `pd.read_sql(...)`. `sqlite3` ships with Python, so there's nothing to install.

## Run it

```bash
python phase5_sql_analysis.py
```

## The queries

| Section | SQL features | Business question |
|---------|-------------|-------------------|
| 9.2 | `SELECT *` | "Show me all cleaned orders." |
| 9.3 | `WHERE` + `ORDER BY` | "Which orders are above ₹10,000?" |
| 9.4 | `ORDER BY` | "Who placed the biggest orders?" |
| 9.5a | `GROUP BY` + `SUM` | "Top category by revenue?" |
| 9.5b | `GROUP BY` + `SUM` | "Highest-revenue city?" |
| 9.5c | `WHERE` | "Which customers are in Pune?" |

## The key takeaway

> The SQL results **match** the Pandas `groupby()` from Phase 3. The two skill sets reach the
> **same insights**. Real-world flow: **SQL retrieves and filters at the database; Pandas +
> visualization refine and present.** `GROUP BY` + `SUM` here is a gentle preview of the
> aggregation you'll master next.

> ⚠️ Always `conn.close()` when finished with a database connection.
