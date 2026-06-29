# Day 5 Lab — DOM Manipulation Reference

A step-by-step reference page covering **every core DOM operation**: selecting
elements, modifying content and classes, handling click events, creating
elements dynamically, and removing them with **event delegation**.

## Files

| File | What it is |
|------|------------|
| `index.html` | The page: a title, a message line, a text input, "Update" and "Add" buttons, and a list. |
| `styles.css` | Styling, including a `.highlight` class toggled from JavaScript. |
| `script.js` | Numbered steps demonstrating each DOM operation. |

## What it does (step by step)

1. **Step 2 — Select:** grab elements with `getElementById` (and log one to confirm).
2. **Step 3 — Modify:** change the title's `textContent` and add a `.highlight` class.
3. **Step 4 — Click event:** the **Update** button echoes the input into the message line (with an empty-input check).
4. **Step 5 — Create:** the **Add** button builds a new `<li>` with `createElement` and `appendChild`, then clears the input.
5. **Step 6 — Event delegation:** one listener on the list deletes any `<li>` you click.

## How to run it

1. Open `index.html` in your browser (double-click or **Live Server**).
2. Type in the box, click **Update** to echo it, click **Add** to add list items.
3. Click any list item to delete it. Open **F12 → Console** to see the logged element.

## How to stop it

Close the browser tab (or stop Live Server from the VS Code status bar).

## Concepts practised

`getElementById`, `textContent`, `classList.add`, `addEventListener`,
`createElement` / `appendChild`, `.remove()`, and **event delegation**.
