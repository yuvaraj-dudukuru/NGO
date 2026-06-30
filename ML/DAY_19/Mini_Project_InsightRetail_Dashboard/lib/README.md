# `lib/` — vendored JavaScript libraries

| File | What it is |
|------|-----------|
| `chart.umd.min.js` | [Chart.js](https://www.chartjs.org/) — base charting library |
| `chartjs-chart-geo.umd.min.js` | Chart.js **geo** plugin — adds the choropleth (US-state) map |

Both are vendored locally so `../dashboard.html` (with its interactive state map)
works fully **offline**.

> Third-party, minified code — **do not edit**.
