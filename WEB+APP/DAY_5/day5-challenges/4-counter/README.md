# Challenge 4 — Counter

A number you can increment, decrement, and reset with three buttons.

## Files
- `index.html` — the count display and **+** / **−** / **Reset** buttons.
- `styles.css` — styling.
- `script.js` — keeps the count in a `let` variable and re-renders on each click.

## How it works
State lives in a `let count = 0` variable. Each button's `click` listener
changes `count` (`++`, `--`, or back to `0`) and then calls `render()`, which
writes the value into the display element. Using `let` (not `const`) is the
point — the value changes over time.

## How to run
Open `index.html` in a browser (double-click or **Live Server**) and click the buttons.

## How to stop
Close the browser tab.

## Concept
Mutable state with `let`, plus a tiny `render()` function to keep the UI in sync.
