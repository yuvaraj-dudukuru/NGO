# Student Information Page — Day 4 Project

The Day 4 practical project: an interactive page that displays student info and
reacts to button clicks using core JavaScript (input/output, type conversion,
validation, conditionals, and a first taste of DOM updates). All data is
placeholder/demo data.

## Files

| File | What it is |
|------|------------|
| `index.html` | Page markup — a profile card, three action buttons, and a result area. |
| `styles.css` | Styling for the header, cards, buttons, and footer. |
| `script.js` | The three button handlers. |

## What each button does

| Button | Function | Behaviour |
|--------|----------|-----------|
| **Enter Your Name** | `enterName()` | `prompt()` for a name, trims/validates it, greets with `alert()`, and writes it into `#studentName`. Shows an error alert if blank. |
| **Calculate Average Marks** | `calculateAverage()` | Prompts for three marks, converts with `Number()`, validates with `isNaN()`, computes the average (`toFixed(2)`), and shows Pass/Fail (≥ 40 = Pass) in `#result`. |
| **Change Page Title** | `changeTitle()` | Toggles the `#pageTitle` heading between "Student Information" and "Welcome to Day 4!" — a preview of DOM manipulation. |

## How to run it

1. Double-click `index.html`, or right-click → **Open with** → your browser.
   (In VS Code, **Live Server** also works.)
2. Click the buttons and follow the `prompt()` dialogs.
3. Press **F12 → Console** if you want to watch for errors.

## How to stop it

Close the browser tab (or stop Live Server from the VS Code status bar).

## Concepts practised

`prompt()` / `alert()`, `Number()` conversion, `isNaN()` validation, the ternary
operator, `toFixed()`, `getElementById()`, and `textContent`.
