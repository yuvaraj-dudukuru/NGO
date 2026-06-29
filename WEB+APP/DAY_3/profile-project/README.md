# Personal Profile Page — Day 3 Project

The Day 3 capstone: a complete, responsive **personal profile / portfolio** page
styled entirely with external CSS. All details (name, email, photo) are
**placeholder data** — replace them with your own before publishing.

## Files

| File | What it is |
|------|------------|
| `index.html` | The page markup: sticky navbar, hero with avatar, and four cards (About, Skills, Projects, Contact). |
| `styles.css` | The external stylesheet: reset, typography, navbar, hero, cards, buttons, hover effects, and a responsive media query. |

## What it does

- A **sticky navigation bar** stays pinned to the top while you scroll; its
  links jump to the matching section via `#id` anchors.
- A **hero header** shows a circular avatar (`border-radius: 50%`), the name,
  and a tagline.
- Four **cards** present About, Skills (pill badges), Projects, and Contact.
- The **Contact** card has buttons with **hover effects** (an "Email Me"
  `mailto:` link and a placeholder "View GitHub" link).
- The layout is **responsive** — it reflows on small screens via a
  `@media (max-width: 600px)` query.

## Requirements demonstrated

1. External CSS only (no inline styles).
2. Circular profile photo via `border-radius: 50%`.
3. A sticky navigation bar.
4. Hover effects on buttons/links.

## How to run it

1. Double-click `index.html`, or right-click → **Open with** → your browser.
2. No server is needed; it runs locally.
3. Click the nav links to smooth-jump between sections.

## How to stop it

Close the browser tab. (If you used VS Code Live Server, stop it from the status bar.)

## Customising it

- Replace the placeholder name **Alex Carter** with your own.
- Replace `alex.carter@example.com` with your real email.
- Swap the `placehold.co` avatar URL for a real photo.
- Update the **Projects** cards with links to your real work.
