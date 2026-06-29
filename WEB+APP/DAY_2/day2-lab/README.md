# day2-lab — HTML5 Practical Lab

The completed Day 2 hands-on lab in a single page, `index.html`.

## How to run
- **With Live Server (VS Code):** right-click `index.html` → "Open with Live Server".
- **Without it:** just double-click `index.html` to open it in a browser.

## What the page demonstrates
| Step | Section | Concept |
|------|---------|---------|
| 2 | Headings | `<h1>`, `<h2>`, `<h3>` |
| 3 | Text | paragraphs, `<strong>`, `<em>`, `<hr>`, `<sub>`, `<sup>` |
| 4 | Image | `<img>` with `alt`, `width`, `height` |
| 5 | Links | new-tab (safe), email (`mailto:`), in-page anchor (`#top`) |
| 6 | Table | `<thead>` / `<tbody>` with headers and rows |
| 7 | Form | labeled inputs, required fields, textarea, submit button |

## Things to test (Step 8)
- Click each link — Wikipedia opens in a new tab, "Email me" opens your mail app,
  "Back to top" jumps to the top (the page must be scrollable).
- Submit the form with empty fields → the browser blocks it and warns you.
- Press **F12** → Elements tab to inspect the live DOM.

## Notes
- The image uses `via.placeholder.com`, so it needs an internet connection. If it
  doesn't load, the `alt` text shows instead. Swap the `src` for a local file anytime.
- The `<body>` has `id="top"` so the "Back to top" anchor has a target.
- Keep this folder — on **Day 3** you'll add CSS and restyle this same HTML.
