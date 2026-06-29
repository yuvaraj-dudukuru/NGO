# Challenge 2 — Color Changer

Click a button to change the page's background color; click **Reset** to restore
the default.

## Files
- `index.html` — Red / Green / Blue / Reset buttons.
- `styles.css` — styling.
- `script.js` — each button sets `document.body.style.backgroundColor`.

## How it works
Each button has a `click` listener that assigns a pastel color to
`document.body.style.backgroundColor`. **Reset** sets it back to `""`, which
removes the inline style and lets the stylesheet's default take over.

## How to run
Open `index.html` in a browser (double-click or **Live Server**) and click the buttons.

## How to stop
Close the browser tab.

## Concept
Changing CSS at runtime through the `style` property.
