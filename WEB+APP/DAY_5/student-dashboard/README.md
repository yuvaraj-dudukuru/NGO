# Dynamic Student Dashboard — Day 5 Project

The Day 5 capstone: a **Dynamic Student Dashboard** that adds, removes, and
counts students live, using a data-driven render pattern that mirrors how modern
front-end frameworks work. All data is placeholder/demo data.

## Files

| File | What it is |
|------|------------|
| `index.html` | A form (name + course), a live student count, and the student list container. |
| `styles.css` | Styling for the form, cards, count, and delete buttons. |
| `script.js` | State (`students` array) + `renderStudents()` + add/delete handlers. |

## How it works

- A single source of truth — the `students` array — holds the data.
- `renderStudents()` rebuilds the list from that array every time the data
  changes (clearing `innerHTML` first, then appending a card per student, and
  updating the live count). When the array is empty it shows a friendly
  "No students yet" message.
- **Add:** the form's `submit` handler calls `event.preventDefault()`, validates
  both fields, `push()`es a `{ name, course }` object, clears the inputs, and re-renders.
- **Delete:** one delegated listener on the list reads the `data-index` of the
  clicked **Delete** button, `splice()`s that student out, and re-renders.

This **data → render** loop is the key idea: you never hand-patch the DOM; you
change the data and re-render.

## How to run it

1. Open `index.html` in your browser (double-click or **Live Server**).
2. Enter a name and course, click **Add Student**.
3. Click **Delete** on any card to remove it. Watch the count update live.

## How to stop it

Close the browser tab (or stop Live Server from the VS Code status bar).

## Concepts practised

ES6 object shorthand (`{ name, course }`), array methods (`push`, `splice`,
`forEach`), `event.preventDefault()`, **event delegation**, `data-*` attributes,
and the data-driven `renderStudents()` pattern.
