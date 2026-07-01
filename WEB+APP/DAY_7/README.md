# Day 7 — Introduction to Git and GitHub

This folder contains all the work for **Day 7**: learning version control with Git and
publishing projects to GitHub. It includes the lesson notes, a hands-on lab, a capstone
portfolio project, and answers to the theory questions.

---

## 📁 Folder Contents

| Item | Type | Description |
|------|------|-------------|
| [Day7_Introduction_to_Git_and_GitHub.md](Day7_Introduction_to_Git_and_GitHub.md) | Notes | The full Day 7 lesson material |
| [Day7_Theory_Answers.md](Day7_Theory_Answers.md) | Answers | Answers to the 10 theory questions |
| [git-practice/](git-practice/) | Lab | Hands-on lab project for the full Git/GitHub workflow |
| [my-portfolio/](my-portfolio/) | Capstone | Responsive portfolio website for version control & deployment |

---

## 🎯 What Day 7 Covers

- What version control is and the problems it solves
- The difference between Git (the tool) and GitHub (the hosting platform)
- Git's four areas: working directory, staging, local repo, remote repo
- Core workflow: `init` → `add` → `commit` → `push`
- Branching, merging, and resolving merge conflicts
- Connecting to a remote, pushing, pulling, and cloning
- Using `.gitignore` and keeping secrets out of repositories
- Deploying a live site with GitHub Pages

---

## 🧪 Practical Lab — `git-practice/`

A step-by-step exercise covering the **entire** Git and GitHub lifecycle: configure Git,
init a repo, commit multiple times, branch and merge, connect to GitHub, push, and clone.

- Starter files are already provided (`index.html`, `README.md`, `styles.css`)
- Follow [git-practice/LAB-GUIDE.md](git-practice/LAB-GUIDE.md) from Step 1

## 🚀 Capstone Project — `my-portfolio/`

A responsive personal portfolio website (HTML, CSS, JavaScript) used to practice putting
a real project under version control and deploying it live.

- See [my-portfolio/README.md](my-portfolio/README.md) for the project details
- See [my-portfolio/GIT-WORKFLOW.md](my-portfolio/GIT-WORKFLOW.md) for the init → push → GitHub Pages steps

---

## ⚙️ Prerequisite — Install Git

> Git is **not yet installed** on this machine. Install it before running any lab commands:
>
> - Download: https://git-scm.com/download/win
> - Or via winget: `winget install --id Git.Git -e`
>
> After installing, reopen your terminal and verify with `git --version`.

---

## ⚡ Git Quick Reference

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
| Push            | `git push`                       |
| Fetch           | `git fetch`                      |
| Pull            | `git pull`                       |
| Clone           | `git clone <url> <folder>`       |
