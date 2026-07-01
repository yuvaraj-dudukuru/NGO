# Day 6 — Responsive Design, Flexbox & Grid

All practical work for Day 6: building layouts that look great on **desktop, tablet, and
mobile** using the viewport tag, responsive images, **Flexbox**, **CSS Grid**, `auto-fit` /
`minmax()`, media queries, and a touch of JavaScript.

Every project uses **external CSS** (`index.html` + `styles.css`) — the professional standard.

---

## 📁 Folder structure

```
DAY_6/
├── README.md                              ← you are here
├── Day6_Responsive_Design_and_Flexbox_Grid.md   ← the day's notes/lesson
├── Day6_Theory_Questions.md               ← answers to the 10 theory questions
│
├── portfolio/                             ← Section 30 capstone portfolio
├── day6-lab/                              ← step-by-step practical lab
│
├── mini-projects/
│   ├── 1-responsive-portfolio/            ← responsive personal portfolio
│   ├── 2-landing-page/                    ← "FocusFlow" product landing page
│   ├── 3-blog-layout/                     ← main content + sidebar (stacks on mobile)
│   ├── 4-image-gallery/                   ← responsive image gallery
│   └── 5-deploy-portfolio/               ← customized, ready for GitHub Pages (Day 7)
│
└── layout-challenges/
    ├── 1-holy-grail/                      ← header/footer/3-column Grid layout
    ├── 2-pricing-table/                   ← equal-height Flexbox pricing plans
    ├── 3-photo-gallery/                   ← Grid + object-fit: cover
    ├── 4-hamburger-navbar/                ← collapsing menu (HTML + CSS + JS)
    └── 5-dashboard/                       ← admin dashboard with stat cards
```

---

## 📚 What's inside

### Reference & theory
| File | What it is |
|------|-----------|
| [Day6_Responsive_Design_and_Flexbox_Grid.md](Day6_Responsive_Design_and_Flexbox_Grid.md) | The full Day 6 lesson notes. |
| [Day6_Theory_Questions.md](Day6_Theory_Questions.md) | Written answers to all 10 theory questions. |

### Core builds
| Project | Highlights |
|---------|-----------|
| [portfolio/](portfolio/) | The Section 30 capstone: sticky navbar, full-screen gradient hero, auto-fit skill & project grids. |
| [day6-lab/](day6-lab/) | The hands-on lab (Steps 1–5): viewport, Flexbox navbar, centered hero, responsive card grid, media queries. |

### Mini-projects
| Project | Highlights |
|---------|-----------|
| [1-responsive-portfolio/](mini-projects/1-responsive-portfolio/) | Day 2/3 portfolio made fully responsive. |
| [2-landing-page/](mini-projects/2-landing-page/) | Product landing page: hero, 6-card features grid, CTA, footer. |
| [3-blog-layout/](mini-projects/3-blog-layout/) | `1fr 300px` Grid that collapses to one column on mobile. |
| [4-image-gallery/](mini-projects/4-image-gallery/) | `auto-fit` / `minmax` gallery with `object-fit: cover`. |
| [5-deploy-portfolio/](mini-projects/5-deploy-portfolio/) | Personalized portfolio + [deploy guide](mini-projects/5-deploy-portfolio/README.md) for GitHub Pages. |

### Layout challenges
| Challenge | Key technique |
|-----------|--------------|
| [1-holy-grail/](layout-challenges/1-holy-grail/) | `grid-template-areas` redrawn at each breakpoint. |
| [2-pricing-table/](layout-challenges/2-pricing-table/) | Flexbox `align-items: stretch` for equal-height plans. |
| [3-photo-gallery/](layout-challenges/3-photo-gallery/) | Grid + `object-fit: cover` uniform tiles. |
| [4-hamburger-navbar/](layout-challenges/4-hamburger-navbar/) | JavaScript toggles a collapsing mobile menu. |
| [5-dashboard/](layout-challenges/5-dashboard/) | Sidebar + 8 stat cards + CSS bar chart. |

---

## ▶️ How to run

1. Open any project's `index.html` in your browser (double-click), **or** in VS Code
   right-click → **Open with Live Server**.
2. Press `F12` to open DevTools, then `Ctrl+Shift+M` to toggle device mode.
3. Test at **375px** (phone), **768px** (tablet), and **1440px** (desktop), and drag the
   width slider to watch layouts reflow.

> **Note:** The image galleries (mini-project 4, challenge 3) load photos from
> `picsum.photos`, so they need an internet connection to display images.

---

## ✅ Day 6 skills exercised
- Viewport meta tag & responsive images (`max-width: 100%`)
- **Flexbox** — navbars, centering, equal-height cards, button rows
- **CSS Grid** — page layouts, `grid-template-areas`, responsive card grids
- `repeat(auto-fit, minmax(...))` and the `fr` unit
- Media queries & mobile-first refinements
- Responsive units (`rem`, `vw`, `vmin`)
- A little JavaScript for the hamburger menu (Day 5 carryover)

**Next up (Day 7):** deploy the portfolio to GitHub Pages — see the
[deploy guide](mini-projects/5-deploy-portfolio/README.md).
