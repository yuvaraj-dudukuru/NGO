# Day 4 Coding Challenges — JavaScript

Five button-driven coding challenges on a single page. Each button runs one
challenge through `prompt()` dialogs and prints the answer into the on-page
**Result** area (`#result`).

## Files

| File | What it is |
|------|------------|
| `index.html` | Five buttons + a result area. |
| `styles.css` | Header, card, button, and footer styling. |
| `script.js` | The five challenge functions plus a `showResult()` helper. |

## The five challenges

| # | Button → Function | What it does |
|---|-------------------|--------------|
| 1 | `temperatureConverter()` | Celsius → Fahrenheit using `C * 9/5 + 32`. |
| 2 | `evenOrOdd()` | Uses the modulus operator (`% 2`) to report even/odd. |
| 3 | `simpleCalculator()` | `+ - * /` via a `switch`, with invalid-input and divide-by-zero handling. |
| 4 | `gradeCalculator()` | Averages three subjects → grade A (≥90) / B (≥75) / C (≥60) / F. |
| 5 | `rollDice()` | Two dice with `Math.floor(Math.random()*6)+1`, plus the total. |

Every numeric input is converted with `Number()` and validated with `isNaN()`
before use.

## How to run it

1. Double-click `index.html` (or open with **Live Server** / your browser).
2. Click any challenge button and follow the prompts.
3. Read the answer in the **Result** box. (Open **F12 → Console** to see errors, if any.)

## How to stop it

Close the browser tab (or stop Live Server from the VS Code status bar).

## Concepts practised

Functions, operators (arithmetic, modulus, comparison), `Number()`/`isNaN()`,
the ternary operator, `switch` statements, `if/else if` chains, `Math.random()`
/ `Math.floor()`, `toFixed()`, and DOM updates via `textContent`.
