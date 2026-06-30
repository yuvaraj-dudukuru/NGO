# `data/` — HR source data + generator

| File | What it is |
|------|-----------|
| `generate_data.js` | The **seeded** Node.js generator (deterministic — same output every run) |
| `employees.csv` | The generated employee dataset (importable into Power BI / Tableau / Excel) |
| `data_dictionary.md` | Definition of every column |

## Regenerate (optional)

```bash
node data/generate_data.js     # run from the HR_Dashboard_Activity folder
```

Rewrites `employees.csv` and `../assets/data.js`. Fixed seed -> identical output.
All employee records are synthetic — no real people, names, or contact details.
