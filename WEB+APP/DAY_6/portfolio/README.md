# Day 6 Portfolio — Responsive Capstone

The Section 30 capstone for Day 6: a polished, fully responsive personal
portfolio. All content uses placeholder/demo data.

## Files
- `index.html` — sticky navbar, full-screen gradient hero, About, Skills, Projects, and Contact sections.
- `styles.css` — the styling: sticky nav, gradient hero, and `auto-fit` skill/project grids.

## What it does
- A **sticky navbar** stays pinned while you scroll, with anchor links to each section.
- A **full-screen gradient hero** introduces the name and tagline.
- **Skills** and **Projects** are laid out with `repeat(auto-fit, minmax(...))`
  grids, so the number of columns adapts automatically to the screen width.
- A **Contact** section provides email/phone placeholders.

## How to run
1. Open `index.html` in a browser (double-click or **Live Server**).
2. Resize the window (or use **Ctrl+Shift+M** device mode) to watch the grids reflow.

## How to stop
Close the browser tab (or stop Live Server from the VS Code status bar).

## Note
Contact details (email, phone) are placeholders — replace them with your own
before publishing.

## Concepts practised
Sticky positioning, gradient backgrounds, CSS Grid with `auto-fit` / `minmax`,
and responsive design.
