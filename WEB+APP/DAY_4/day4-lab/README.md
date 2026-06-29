# Day 4 Lab — JavaScript Fundamentals (Console)

A **console-driven** walkthrough of every core JavaScript fundamental, step by
step. The page itself is almost empty on purpose — all the action happens in the
browser's **DevTools Console** and in a few `prompt()`/`alert()` dialogs.

## Files

| File | What it is |
|------|------------|
| `index.html` | A minimal page that just loads the script and tells you to open the console. |
| `script.js` | The lab — numbered steps from messages → variables → input → calculations → arrays → conditionals. |

## What it does (step by step)

1. **Step 2 — Messages:** `console.log()` greeting lines.
2. **Step 3 — Variables & types:** `const`/`let`, string/number/boolean, `typeof`.
3. **Step 4 — Input:** `prompt()` for a name; greets with `+` concatenation and a template literal.
4. **Step 5 — Calculations:** two numbers via `Number(prompt())`, then sum and product.
5. **Step 6 — Arrays:** create an array, index it, read `.length`, and `.push()` a new item.
6. **Step 7 — Output & conditionals:** a marks input with `isNaN()` validation and Pass/Fail (≥ 40) logic shown via `alert()`.

## How to run it

1. Open `index.html` in your browser (double-click, or **Open with** → browser).
2. Press **F12** (or **Ctrl+Shift+I**) and switch to the **Console** tab.
3. Reload the page — answer the `prompt()` dialogs and watch the console output.

> Tip: because the script runs top-to-bottom on load, just **refresh** the page
> to run it again.

## How to stop it

Close the browser tab. There is no long-running process to stop — the script
finishes as soon as it reaches the end.

## Concepts practised

`console.log`, `const`/`let`, primitive types, `typeof`, `prompt`/`alert`,
string concatenation vs. template literals, `Number()` conversion, arrays
(`[]`, indexing, `.length`, `.push()`), and `if/else if/else` with `isNaN()`.
