# Day 6 Mini-Projects

Five small responsive builds. Each is a self-contained `index.html` + `styles.css`.

```
mini-projects/
├── 1-responsive-portfolio/ ← a personal portfolio made fully responsive
├── 2-landing-page/         ← "FocusFlow" product landing page
├── 3-blog-layout/          ← main content + sidebar that stacks on mobile
├── 4-image-gallery/        ← responsive image gallery (auto-fit / minmax)
└── 5-deploy-portfolio/     ← a portfolio prepared for GitHub Pages (see its README)
```

| # | Project | Highlights |
|---|---------|------------|
| 1 | Responsive Portfolio | The earlier portfolio reworked to reflow on every screen size. |
| 2 | Landing Page | Hero + 6-card features grid + call-to-action + footer. |
| 3 | Blog Layout | A `1fr 300px` Grid that collapses to one column on mobile. |
| 4 | Image Gallery | `repeat(auto-fit, minmax(...))` grid with `object-fit: cover`. |
| 5 | Deploy Portfolio | A personalised portfolio plus a GitHub Pages deploy guide. |

## How to run
Open any project's `index.html` in a browser (double-click or **Live Server**),
then resize / use device mode (**Ctrl+Shift+M**) to test responsiveness.

## How to stop
Close the browser tab (or stop Live Server from the VS Code status bar).

> **Note:** The image gallery (project 4) loads photos from the internet and
> needs a connection to display them.

Each sub-folder has its own README with full details.
