# `data/` — Sales (hands-on build) dashboard data

Two copies of the **same synthetic records**, in the two formats a BI workflow needs:

| File | Format | Used by |
|------|--------|---------|
| `sales_data.csv` | comma-separated | **Import into Power BI / Tableau** (or open in Excel) to rebuild the dashboard in those tools |
| `sales_data.js` | JavaScript (`window.SALES_DATA = [ ... ]`) | Loaded by `../dashboard.html` so the offline HTML dashboard has its data with no server |

## How it is generated

Both files are written by the seeded generator
[`../../generate_sample_data.py`](../../generate_sample_data.py):

```bash
cd ../..
python generate_sample_data.py        # rewrites every dashboard's data/ files
```

The random seed is fixed, so re-running produces **identical** output.

> 100% synthetic data — generic ID codes only, no names, emails, or real people.
> Nothing here is "run"; these are data files. Edit the generator, not these files.
