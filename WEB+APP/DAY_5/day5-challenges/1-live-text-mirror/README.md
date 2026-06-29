# Challenge 1 — Live Text Mirror

Type in the input box and your text is mirrored on the page **in real time**, on
every keystroke.

## Files
- `index.html` — an input box and an output area.
- `styles.css` — styling.
- `script.js` — listens for the `input` event and copies the value to the output.

## How it works
The `input` event fires on every change to the field. The handler reads
`mirrorInput.value` and writes it into `mirrorOutput.textContent`, falling back
to a placeholder string when the box is empty.

## How to run
Open `index.html` in a browser (double-click or **Live Server**) and start typing.

## How to stop
Close the browser tab.

## Concept
The `input` event for live, character-by-character updates.
