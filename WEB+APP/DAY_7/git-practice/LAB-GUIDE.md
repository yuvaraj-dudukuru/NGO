# Day 7 Practical Lab — Full Git & GitHub Workflow

Run each command in order, in a real terminal, inside this `git-practice` folder.
Replace `<your-username>` with your GitHub username and use your own name/email.

> **Note:** Git is not currently installed on this machine. Install it first from
> https://git-scm.com/download/win , then reopen your terminal and start at Step 1.

---

## Step 1 — Verify and Configure Git

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --list
```

## Step 2 — Create a Repository

```bash
# (this folder already exists; just cd into it)
cd git-practice
git init
git status
```

Expected:

```
Initialized empty Git repository in .../git-practice/.git/
On branch main
No commits yet
```

## Step 3 — Create Files and Commit

`index.html` and `README.md` are already here.

```bash
git status                 # files are untracked
git add .
git status                 # files are now staged
git commit -m "Initial commit: add index.html and README"
git log --oneline
```

## Step 4 — Make Changes and Commit Again

```bash
# edit index.html (add a heading or paragraph)
git diff
git add .
git commit -m "Add page heading and content"
git log --oneline
```

## Step 5 — Practice Branching

```bash
git switch -c feature-styling
# styles.css is already provided and linked in index.html
git add .
git commit -m "Add basic CSS styling"
git switch main
git merge feature-styling
git branch -d feature-styling
git log --oneline
```

> Tip: If you want to practice the *creation* yourself, delete `styles.css` first
> and recreate it on the branch.

## Step 6 — Create a GitHub Repo and Connect

1. On GitHub, create a new repository named `git-practice` (do **not** add a README).
2. Copy its HTTPS URL.

```bash
git remote add origin https://github.com/<your-username>/git-practice.git
git remote -v
git branch -M main
```

## Step 7 — Push the Project

```bash
git push -u origin main
```

## Step 8 — Clone the Repository (Simulate Another Computer)

```bash
cd ..
git clone https://github.com/<your-username>/git-practice.git git-practice-clone
cd git-practice-clone
git log --oneline
```

Expected: a full copy of the repo with the complete commit history intact.

---

## Quick Reference

| Action          | Command                          |
| --------------- | -------------------------------- |
| Init repo       | `git init`                       |
| Status          | `git status`                     |
| Stage all       | `git add .`                      |
| Commit          | `git commit -m "message"`        |
| History         | `git log --oneline`             |
| New branch      | `git switch -c <name>`           |
| Switch branch   | `git switch <name>`              |
| Merge           | `git merge <name>`               |
| Delete branch   | `git branch -d <name>`           |
| Add remote      | `git remote add origin <url>`    |
| Push (first)    | `git push -u origin main`        |
| Clone           | `git clone <url> <folder>`       |
