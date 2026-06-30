# `data/` — InsightRetail dashboard data

| File | Format | Used by |
|------|--------|---------|
| `insightretail_sales.csv` | CSV | Import into Power BI / Tableau / Excel |
| `insightretail_sales.js`  | JS (`window.SALES_DATA`) | Loaded by `../dashboard.html` (charts, KPIs, slicers) |
| `us-states.geojson`       | GeoJSON | Boundaries of US states for the choropleth map |
| `us-states-geo.js`        | JS (`window.US_STATES_GEO`) | The same map geometry, embedded so the map renders offline |

The sales files are produced by the seeded generator
[`../../generate_sample_data.py`](../../generate_sample_data.py) (fixed seed ->
identical output each run). The geo files are static reference geometry.

> 100% synthetic state-level sales, no real people. Data files only — nothing here is executed.
