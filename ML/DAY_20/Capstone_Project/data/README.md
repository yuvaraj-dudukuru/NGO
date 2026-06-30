# `data/` — capstone source data + generator

| File | What it is |
|------|-----------|
| `generate_data.js` | The **seeded** Node.js generator that builds the dataset (deterministic — same output every run) |
| `sales_clean.csv` | The cleaned, analysis-ready dataset (a graded deliverable; also importable into Power BI / Tableau / Excel) |
| `data_dictionary.md` | Definition of every column (name, type, meaning) |

## Regenerate (optional)

```bash
node data/generate_data.js     # run from the Capstone_Project folder
```

This rewrites `sales_clean.csv` and `../assets/data.js`. The PRNG seed is fixed,
so the output is identical each run. The data is entirely synthetic — the header
comment in the generator describes the "story" deliberately built into it.
