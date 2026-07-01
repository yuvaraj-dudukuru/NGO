# Challenge 2 — Pricing Table

A row of pricing plans (cards) that all stay the **same height** even when their
content differs, and that wrap onto multiple rows on narrow screens.

## Files
- `index.html` — three or more pricing-plan cards.
- `styles.css` — Flexbox layout with equal-height cards.

## How it works
The cards sit in a **Flexbox** row. `align-items: stretch` (Flexbox's default
cross-axis behaviour) makes every card match the tallest one, so the plans line
up neatly regardless of how much text each contains. `flex-wrap` lets them wrap
on small screens.

## How to run
Open `index.html` in a browser (double-click or **Live Server**) and resize to
see the cards wrap.

## How to stop
Close the browser tab.

## Concept
Flexbox equal-height cards via `align-items: stretch` + `flex-wrap`.
