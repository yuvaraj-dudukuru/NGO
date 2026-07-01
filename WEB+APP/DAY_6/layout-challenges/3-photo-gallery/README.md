# Challenge 3 — Photo Gallery

A responsive photo grid of uniform tiles. Images of different sizes are cropped
to fill identical cells without distortion.

## Files
- `index.html` — the gallery grid of images.
- `styles.css` — CSS Grid with `object-fit: cover` tiles.

## How it works
The gallery is a **CSS Grid** using `repeat(auto-fit, minmax(...))`, so the
number of columns adapts to the screen width. Each image uses
`object-fit: cover`, which crops it to fill its tile while keeping its aspect
ratio — every tile looks uniform.

## How to run
1. Open `index.html` in a browser (double-click or **Live Server**).
2. Resize the window to watch the column count change.

> **Note:** Images load from the internet, so you need an active connection for
> them to appear.

## How to stop
Close the browser tab.

## Concept
Responsive Grid (`auto-fit` / `minmax`) + `object-fit: cover`.
