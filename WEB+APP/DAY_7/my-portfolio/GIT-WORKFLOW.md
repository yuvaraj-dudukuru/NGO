# Day 7 Capstone — Portfolio Version Control & Deployment

This guide walks through putting this portfolio under version control, pushing it to
GitHub, building a commit history, and deploying it live with GitHub Pages.

> Replace `<your-username>` with your own GitHub username wherever it appears.

---

## Step 1 — Initialize Git

```bash
cd my-portfolio          # navigate into the project folder
git init                 # start tracking this folder with Git
```

Expected:

```
Initialized empty Git repository in .../my-portfolio/.git/
```

## Step 2 — .gitignore and README

Both are already included in this folder:

- `.gitignore` — excludes OS/editor junk (`.DS_Store`, `Thumbs.db`, `*.log`, etc.)
- `README.md` — describes the project

## Step 3 — Stage and Commit

```bash
git status                                   # see untracked files
git add .                                    # stage everything
git status                                   # confirm what's staged
git commit -m "Initial commit: responsive portfolio website"
```

Expected:

```
[main (root-commit) a1b2c3d] Initial commit: responsive portfolio website
 5 files changed, ... insertions(+)
```

## Step 4 — Create the GitHub Repository

On GitHub:

1. Click **+** → **New repository**
2. Name it `my-portfolio`
3. Add a description
4. Choose **Public**
5. **Do not** initialize with a README (you already have one)
6. Click **Create repository** and copy the HTTPS URL

## Step 5 — Connect and Push

```bash
git remote add origin https://github.com/<your-username>/my-portfolio.git
git remote -v                  # verify the connection
git branch -M main             # ensure the branch is named main
git push -u origin main        # first push, sets up tracking
```

## Step 6 — Make an Update and Track History

```bash
# edit a file (e.g. add a project to index.html or update README)
git status
git diff
git add .
git commit -m "feat: add projects section to portfolio"
git push                       # -u from step 5 means plain 'git push' works
```

Check the history:

```bash
git log --oneline
```

```
e4f5g6h (HEAD -> main, origin/main) feat: add projects section to portfolio
a1b2c3d Initial commit: responsive portfolio website
```

## Step 7 — Deploy Live with GitHub Pages

1. On GitHub: **Settings → Pages**
2. Under **Source**, select the `main` branch and `/ (root)` folder
3. Click **Save** and wait 1–2 minutes
4. Visit:

```
https://<your-username>.github.io/my-portfolio/
```

Finally, add that URL to the **Live Site** section of `README.md`, commit, and push —
the live site updates automatically.

---

## Everyday Workflow Cheat Sheet

| Action            | Command                          |
| ----------------- | -------------------------------- |
| Check status      | `git status`                     |
| See changes       | `git diff`                       |
| Stage all         | `git add .`                      |
| Commit            | `git commit -m "message"`        |
| Push              | `git push`                       |
| View history      | `git log --oneline`              |
