# `lib/` — vendored JavaScript library

| File | What it is |
|------|-----------|
| `chart.umd.min.js` | [Chart.js](https://www.chartjs.org/) — the charting library that renders the dashboard's KPI charts |

The library is **vendored** (kept locally) so `../dashboard.html` works fully
**offline** — no CDN or internet connection is required. `dashboard.html` loads
it with `<script src="lib/chart.umd.min.js"></script>`.

> Third-party, minified code — **do not edit**. Nothing here is run directly.
