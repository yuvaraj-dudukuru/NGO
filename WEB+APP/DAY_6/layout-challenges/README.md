# Day 6 Layout Challenges

Five layout challenges, each in its own folder, practising classic responsive
patterns with Flexbox, CSS Grid, and a little JavaScript.

```
layout-challenges/
├── 1-holy-grail/       ← header/footer + 3-column layout via grid-template-areas
├── 2-pricing-table/    ← equal-height pricing plans with Flexbox
├── 3-photo-gallery/    ← uniform tiles with Grid + object-fit: cover
├── 4-hamburger-navbar/ ← collapsing mobile menu (HTML + CSS + JS)
└── 5-dashboard/        ← admin dashboard: sidebar + stat cards + CSS bar chart
```

| # | Challenge | Key technique |
|---|-----------|---------------|
| 1 | Holy Grail | `grid-template-areas` redrawn at each breakpoint |
| 2 | Pricing Table | Flexbox `align-items: stretch` for equal-height cards |
| 3 | Photo Gallery | Grid + `object-fit: cover` for uniform tiles |
| 4 | Hamburger Navbar | JS toggles an `.open` class to collapse the menu |
| 5 | Dashboard | Sidebar layout with stat cards and a pure-CSS bar chart |

## How to run
Open any challenge's `index.html` in a browser (double-click or **Live Server**),
then resize the window / use device mode (**Ctrl+Shift+M**) to see it respond.

## How to stop
Close the browser tab (or stop Live Server from the VS Code status bar).

> **Note:** The photo gallery (challenge 3) loads images from the internet, so it
> needs a connection to display them.

Each sub-folder has its own README with full details.
