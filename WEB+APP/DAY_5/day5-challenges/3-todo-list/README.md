# Challenge 3 — To-Do List

Add tasks to a list and click any task to delete it.

## Files
- `index.html` — a text input, an **Add** button, and the task list.
- `styles.css` — styling.
- `script.js` — adds tasks and deletes them via event delegation.

## How it works
- **Add:** `addTask()` reads the input, ignores empty text, creates a new `<li>`
  with `createElement`, appends it, clears the box, and refocuses the input.
- You can add either by clicking **Add** or by pressing **Enter** (a `keydown`
  listener checks for the Enter key).
- **Delete:** one listener on the `<ul>` uses **event delegation** — when a
  clicked target is an `<li>`, it is removed.

## How to run
Open `index.html` in a browser (double-click or **Live Server**). Type a task,
press Enter or click **Add**, then click a task to remove it.

## How to stop
Close the browser tab.

## Concept
`createElement` / `appendChild`, the `keydown` (Enter) shortcut, and **event delegation**.
