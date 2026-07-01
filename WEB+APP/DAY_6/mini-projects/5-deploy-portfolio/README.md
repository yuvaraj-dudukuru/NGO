# Deploy-Ready Portfolio

This is the Section 30 portfolio, customized and ready to deploy on **Day 7**.

## Before you deploy — personalize it
Open `index.html` and replace every `<!-- TODO -->` marked spot:
- [ ] Your name (navbar logo, hero, footer)
- [ ] Hero tagline
- [ ] About Me paragraph
- [ ] Skills (edit/add/remove `.skill-card` items)
- [ ] Projects (titles, descriptions, and real `href` links)
- [ ] Contact email & phone
- [ ] GitHub and LinkedIn links in the `.social` block

## Deploy to GitHub Pages (Day 7)
1. Create a new repository on GitHub (e.g. `my-portfolio`).
2. Push these two files (`index.html`, `styles.css`) to the repo:
   ```bash
   git init
   git add index.html styles.css
   git commit -m "Add responsive portfolio"
   git branch -M main
   git remote add origin https://github.com/<your-username>/my-portfolio.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment**.
4. Set **Source** to `Deploy from a branch`, branch `main`, folder `/ (root)`, then **Save**.
5. Wait ~1 minute — your site goes live at:
   `https://<your-username>.github.io/my-portfolio/`

## Test before pushing
Open `index.html`, press `F12`, then `Ctrl+Shift+M` and check 375px, 768px, and 1440px.
Confirm: navbar stacks on mobile, grids reflow, no horizontal scrolling.
