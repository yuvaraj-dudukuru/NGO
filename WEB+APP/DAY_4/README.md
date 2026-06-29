# Day 4 — JavaScript Basics

This folder contains all the work for **Day 4** of the Web Development course: the practical project, the hands-on lab, the coding challenges, and the theory answers. Every concept from Day 4 is exercised here — variables, data types, operators, type conversion, strings, numbers, input/output, conditionals, functions, template literals, arrays, and a first taste of DOM manipulation.

## 📁 Folder Structure

```
DAY_4/
├── README.md                     ← you are here
├── Day4_JavaScript_Basics.md     ← the day's notes / reference material
├── Day4_Theory_Answers.md        ← answers to the 10 theory questions
│
├── student-info-page/            ← Practical Project (Section 21)
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── day4-lab/                     ← Practical Lab (Steps 1–8)
│   ├── index.html
│   └── script.js
│
└── day4-challenges/              ← 5 Coding Challenges
    ├── index.html
    ├── styles.css
    └── script.js
```

## 🚀 How to Run

Each sub-folder is a self-contained mini-project. To run any of them:

1. Open the folder in **VS Code**.
2. Open its `index.html` with **Live Server** (or just double-click it to open in a browser).
3. Press **F12 → Console** to see `console.log` output where relevant.
4. Follow the on-screen prompts / click the buttons.

## 📦 What's Inside

### 1. Student Information Page — `student-info-page/`
An interactive page that displays student info and reacts to button clicks:
- **Enter Your Name** — `prompt()` for a name, validates it, greets with an `alert()`, and updates the page.
- **Calculate Average Marks** — three marks, `Number()` conversion, `isNaN()` validation, average to 2 decimals, Pass/Fail via a ternary.
- **Change Page Title** — toggles the heading between two texts (a preview of DOM manipulation).

### 2. Practical Lab — `day4-lab/`
A console-driven walkthrough of every core fundamental, step by step:
- Console messages, variables & data types (`typeof`)
- Input with `prompt()` and template literals
- Calculations with string-to-number conversion
- Arrays (`[]`, indexing, `.length`, `.push()`)
- Conditionals with `isNaN()` validation and Pass/Fail logic

### 3. Coding Challenges — `day4-challenges/`
Five button-driven challenges on one page:
1. **Temperature Converter** — Celsius → Fahrenheit (`C * 9/5 + 32`)
2. **Even or Odd** — using the modulus operator (`% 2`)
3. **Simple Calculator** — `+ - * /` with a `switch`, invalid-input and divide-by-zero handling
4. **Grade Calculator** — average of three subjects → grade A/B/C/F
5. **Random Dice** — two rolls with `Math.random()` and `Math.floor()`, plus the total

### 4. Theory Answers — `Day4_Theory_Answers.md`
Short written answers to the 10 Day 4 theory questions (JavaScript vs HTML/CSS, `var`/`let`/`const`, primitive types, `null` vs `undefined`, `==` vs `===`, `prompt()` conversion, type conversion, template literals, objects vs arrays, and error types/debugging).

## 🧠 Concepts Covered

| Concept | Where it's used |
|---|---|
| Variables (`let`, `const`) | all projects |
| Data types & `typeof` | lab, theory |
| Operators (math, modulus, comparison) | challenges, project |
| Type conversion (`Number()`, `isNaN()`) | lab, project, challenges |
| Strings & template literals | everywhere |
| `Math.random()` / `Math.floor()` / `toFixed()` | challenges, project |
| Input/output (`prompt`, `alert`, `console.log`) | all projects |
| Conditionals (`if/else`, ternary, `switch`) | project, challenges |
| Functions | project, challenges |
| Arrays | lab |
| DOM update (`getElementById`, `textContent`) | project, challenges |

---

*Day 4 of the Web Development Internship — JavaScript Basics.*
