# Mini-Project 3 — Blog Layout

A two-column blog layout: a wide main content area beside a fixed-width sidebar,
which collapses to a single column on mobile.

## Files
- `index.html` — article content plus a sidebar (about, links, etc.).
- `styles.css` — CSS Grid layout with a responsive collapse.

## How it works
The page uses **CSS Grid** with `grid-template-columns: 1fr 300px` — the main
column flexes while the sidebar stays 300px wide. A media query switches to a
single column on narrow screens so the sidebar stacks below the article.

## How to run
Open `index.html` in a browser (double-click or **Live Server**), then resize to
watch the sidebar move below the content.

## How to stop
Close the browser tab.

## Concept
A `1fr 300px` Grid that collapses to one column with a media query.
