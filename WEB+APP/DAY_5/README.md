# Day 5 — ES6 Concepts & DOM Manipulation

This folder contains all the practical work for **Day 5**: a hands-on lab, five coding
challenges, a full project, and written theory answers. Everything uses the professional
standard of **external files** — separate `index.html`, `styles.css`, and `script.js`.

> Open any `index.html` in a browser to run it. Press **F12** to open the DevTools console
> and watch for logs and errors.

---

## 📂 Folder Structure

```
DAY_5/
├── README.md                  ← you are here
├── Day5_Theory_Answers.md     ← answers to the 10 theory questions
│
├── day5-lab/                  ← Practical Lab (step-by-step DOM reference)
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── day5-challenges/           ← 5 coding challenges + landing page
│   ├── index.html             (links to all five)
│   ├── styles.css
│   ├── 1-live-text-mirror/
│   ├── 2-color-changer/
│   ├── 3-todo-list/
│   ├── 4-counter/
│   └── 5-form-validator/
│
└── student-dashboard/         ← Practical Project (the Day 5 capstone)
    ├── index.html
    ├── styles.css
    └── script.js
```

---

## 🧪 1. Practical Lab — `day5-lab/`

A step-by-step reference covering **every core DOM operation**:

- Selecting elements (`getElementById`)
- Modifying content and classes (`textContent`, `classList`)
- Handling click events (`addEventListener`)
- Creating elements dynamically (`createElement`, `appendChild`)
- Removing elements via **event delegation**

**Run:** open [day5-lab/index.html](day5-lab/index.html). Update the message, add list
items, and click items to delete them.

---

## 🎯 2. Coding Challenges — `day5-challenges/`

Five focused mini-projects. Start from the landing page
[day5-challenges/index.html](day5-challenges/index.html).

| # | Challenge | Key concept |
|---|-----------|-------------|
| 1 | **Live Text Mirror** | `input` event → real-time text update |
| 2 | **Color Changer** | changing styles via `style` property |
| 3 | **To-Do List** | `createElement` + **event delegation** to delete |
| 4 | **Counter** | `let` state + `+` / `-` / `Reset` listeners |
| 5 | **Form Validator** | `preventDefault()` + validation messages |

---

## 🚀 3. Practical Project — `student-dashboard/`

The Day 5 capstone: a **Dynamic Student Dashboard** that adds, removes, and counts
students live.

**Features:**
- Add a student (name + course) via a form
- Display students dynamically as cards
- Remove a student with a delete button (event delegation)
- Live total-student count
- Form validation and processing
- A data-driven `renderStudents()` pattern that mirrors how modern frameworks work

**Run:** open [student-dashboard/index.html](student-dashboard/index.html).

---

## 📖 4. Theory Answers — `Day5_Theory_Answers.md`

Short written answers to the 10 Day 5 theory questions, covering ES6, `let`/`const`/`var`
and the Temporal Dead Zone, arrow functions and `this`, rest vs. spread, destructuring,
the DOM, `textContent`/`innerText`/`innerHTML` (with the XSS concern),
`getElementById` vs. `querySelector`, `addEventListener` vs. `onclick`, and
`event.preventDefault()`.

See [Day5_Theory_Answers.md](Day5_Theory_Answers.md).

---

## 🧠 Day 5 Concepts Practiced

**ES6:** `let` / `const`, arrow functions, template literals, object property shorthand,
rest/spread, destructuring, array methods (`forEach`, `push`, `splice`).

**DOM:** element selection, `textContent` / `innerHTML`, `classList`, `createElement` /
`appendChild` / `remove`, `data-*` attributes, event handling, **event delegation**,
form processing with `preventDefault()`, and the data-driven render pattern.
