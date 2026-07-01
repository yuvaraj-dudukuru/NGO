# Challenge 5 — Admin Dashboard

An admin dashboard layout: a fixed sidebar, a top bar, a row of stat cards, and a
simple bar chart built entirely with CSS. All figures are placeholder/demo data.

## Files
- `index.html` — sidebar, top bar (with a greeting), stat cards, and the chart.
- `styles.css` — the dashboard layout (Grid/Flexbox) and the pure-CSS bar chart.

## How it works
- A **sidebar + main area** layout is built with CSS Grid/Flexbox.
- A row of **stat cards** uses a responsive grid that reflows on smaller screens.
- The **bar chart** is made from plain `<div>`s whose heights represent values —
  no chart library needed.
- On narrow screens the sidebar and cards collapse via media queries.

## How to run
1. Open `index.html` in a browser (double-click or **Live Server**).
2. Resize the window / use device mode to see the layout adapt.

## How to stop
Close the browser tab.

## Note
The greeting and all numbers are placeholder data.

## Concept
Dashboard layout (sidebar + content), responsive stat-card grid, and a pure-CSS
bar chart.
