# Mini-Project 4 — Image Gallery

A responsive image gallery whose tiles automatically rearrange to fit the screen
width, with images cropped uniformly.

## Files
- `index.html` — the gallery grid of images.
- `styles.css` — CSS Grid with `auto-fit` / `minmax` and `object-fit: cover`.

## How it works
The grid uses `repeat(auto-fit, minmax(200px, 1fr))`, so columns are added or
removed automatically as the window resizes. Each image uses `object-fit: cover`
to fill its tile without stretching.

## How to run
1. Open `index.html` in a browser (double-click or **Live Server**).
2. Resize the window to see the columns adapt.

> **Note:** Images load from the internet, so an active connection is required
> for them to appear.

## How to stop
Close the browser tab.

## Concept
Auto-responsive Grid (`auto-fit` / `minmax`) + `object-fit: cover`.
