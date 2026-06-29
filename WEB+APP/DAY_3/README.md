# Day 3 — CSS3 Styling & a Personal Profile Page

This folder contains all the work for **Day 3** of the Web & Mobile App
Development course. Day 3 moves from plain HTML into **external CSS3**: resets,
typography, the box model, colors, cards, Flexbox basics, hover effects, and
responsive design with media queries.

All content uses **placeholder/demo data only** — no personal information.

## 📁 Folder Structure

```
DAY_3/
├── README.md                 ← you are here
├── Theory Questions.md       ← the day's theory questions & answers
│
├── day3-lab/                 ← Practical Lab: a step-by-step CSS3 reference page
│   ├── index.html
│   └── styles.css
│
└── profile-project/          ← Practical Project: a styled personal profile page
    ├── index.html
    └── styles.css
```

## 📦 What's Inside

### 1. CSS3 Practical Lab — `day3-lab/`
A minimal page that demonstrates every core CSS concept in numbered steps
(reset → base styles → typography → header/footer → container → cards →
skills list → responsive media query). Use it as a reference for the building
blocks. See [day3-lab/README.md](day3-lab/README.md).

### 2. Personal Profile Page — `profile-project/`
The Day 3 capstone: a complete, responsive personal profile with a sticky
navigation bar, a circular avatar, About / Skills / Projects / Contact cards,
and hover effects on buttons. See
[profile-project/README.md](profile-project/README.md).

## 🚀 How to Run

These are static web pages — **no build step and no server required**.

1. Open the project folder (`day3-lab/` or `profile-project/`).
2. Double-click `index.html`, or right-click → **Open with** → your browser.
3. (Optional) In VS Code, use the **Live Server** extension for auto-reload.

## 🛑 How to Stop

Just close the browser tab. If you used Live Server, click **Port: 5500** in
the VS Code status bar (or press the stop button) to shut the server down.

## 🧠 Concepts Covered

| Concept | Where |
|---|---|
| External stylesheet (`<link rel="stylesheet">`) | both |
| CSS reset & `box-sizing: border-box` | both |
| Typography (`font-size`, `line-height`, `color`) | both |
| Box model (margin, padding, border) | both |
| Cards with `border-radius` & `box-shadow` | both |
| Flexbox (`display: flex`, `gap`, `flex-wrap`) | both |
| `border-radius: 50%` circular avatar | profile-project |
| Sticky navigation bar | profile-project |
| Hover effects (`:hover`, `transition`) | profile-project |
| Responsive design (`@media`) | both |
