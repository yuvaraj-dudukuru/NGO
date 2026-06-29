# Day 3 Lab — CSS3 Practical Reference

A small, self-contained page that demonstrates the core building blocks of CSS3
in clearly numbered steps. It is meant to be **read alongside the styling** so
you can see exactly which CSS rule produces which visual result.

## Files

| File | What it is |
|------|------------|
| `index.html` | The page markup — a header, two content cards (About, Skills), and a footer. |
| `styles.css` | The external stylesheet. Each section is labelled `/* Step N: ... */`. |

## What it does

When opened in a browser the page shows:

- A dark **header** banner with the page title.
- A centered **container** holding two white **cards**.
- A **skills list** rendered as rounded "pill" badges using Flexbox.
- A dark **footer** with a copyright line.
- A **responsive tweak**: below 500px the heading shrinks and card padding reduces.

## How the styling is organised (the "steps")

1. **Step 2 — Reset & base:** `* { margin:0; padding:0; box-sizing:border-box }`.
2. **Step 3 — Typography:** heading sizes and colors.
3. **Step 4 — Header/Footer:** dark background, centered text, padding.
4. **Step 5 — Container:** `width: 90%; max-width: 700px; margin: auto` to center content.
5. **Step 6 — Cards:** white background, `border-radius`, and a soft `box-shadow`.
6. **Step 7 — Skills list:** `display: flex` + `gap` + pill badges.
7. **Step 8 — Responsive:** a `@media (max-width: 500px)` block.

## How to run it

1. Double-click `index.html` (or right-click → **Open with** → your browser).
2. No internet connection or server is required — it runs locally.
3. Resize the browser window narrower than 500px to see the responsive rules apply.

## How to stop it

Close the browser tab. (If you opened it with VS Code Live Server, stop the
server from the VS Code status bar.)

## Key takeaways

- Keep CSS in a **separate file** and link it with `<link rel="stylesheet">`.
- A universal reset plus `box-sizing: border-box` makes layouts predictable.
- `max-width` + `margin: auto` is the classic way to center a content column.
- `@media` queries let one stylesheet adapt to different screen sizes.
