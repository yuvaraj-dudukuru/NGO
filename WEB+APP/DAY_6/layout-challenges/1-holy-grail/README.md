# Challenge 1 — Holy Grail Layout

The classic "Holy Grail" page: a header on top, a footer on the bottom, and a
three-column middle row (left sidebar, main content, right sidebar) that
collapses to a single column on small screens.

## Files
- `index.html` — header, three middle columns, and footer.
- `styles.css` — CSS Grid using `grid-template-areas`.

## How it works
The page uses **CSS Grid** with named `grid-template-areas`. On desktop the areas
form a 3-column middle row; a media query **redraws the same areas** into a single
stacked column for mobile — without changing the HTML order.

## How to run
Open `index.html` in a browser (double-click or **Live Server**), then resize the
window to watch the three columns stack.

## How to stop
Close the browser tab.

## Concept
`grid-template-areas` and re-mapping them at breakpoints.
