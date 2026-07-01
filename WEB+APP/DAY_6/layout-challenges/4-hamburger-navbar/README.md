# Challenge 4 — Hamburger Navbar

A responsive navigation bar whose links collapse behind a **hamburger button**
on small screens. Tapping the button toggles the menu open and closed.

## Files
- `index.html` — the navbar (logo, hamburger button, nav links) and some page content.
- `styles.css` — desktop nav + the mobile collapsed state and the icon animation.
- `script.js` — toggles the menu.

## How it works
On screens below 768px the nav links are hidden and a hamburger button appears.
The script:
- toggles an `.open` class on the nav (show/hide) when the button is clicked,
- toggles an `.active` class on the button (morphs the icon into an "X"),
- updates `aria-expanded` for accessibility, and
- closes the menu automatically after any link is clicked (nice on mobile).

The IDs `#hamburger` and `#navLinks` connect the markup to the script.

## How to run
1. Open `index.html` in a browser (double-click or **Live Server**).
2. Press **F12**, then **Ctrl+Shift+M** for device mode, and narrow the width
   below 768px to reveal the hamburger button. Click it to toggle the menu.

## How to stop
Close the browser tab (or stop Live Server from the VS Code status bar).

## Concept
A CSS-collapsed menu toggled by JavaScript (`classList.toggle`) with
`aria-expanded` for accessibility.
