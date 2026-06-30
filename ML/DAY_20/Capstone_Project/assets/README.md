# `assets/` — dashboard data bundle

| File | What it is |
|------|-----------|
| `data.js` | The cleaned capstone dataset as `window.CAPSTONE_DATA = [ ... ]`, loaded by `../dashboard.html` and `../index.html` so the dashboard runs offline |

`data.js` is **generated** (do not edit by hand) by
[`../data/generate_data.js`](../data/generate_data.js) — see
[`../data/README.md`](../data/README.md). Synthetic data only.
