# Day 7 — Theory Questions & Answers

## 1. What is version control and four problems it solves

Version control is a system that records changes to files over time so you can review history, recover earlier versions, and collaborate without overwriting each other's work. Four problems it solves:

1. **Lost work / no backup** — every committed version is saved, so you can restore any previous state.
2. **No history** — it tracks who changed what, when, and why (commit messages), giving a clear timeline.
3. **Collaboration chaos** — multiple people can work on the same project and merge their changes safely instead of emailing files around.
4. **Fear of breaking things** — you can experiment on branches and roll back easily, so changes are reversible.

## 2. The three types of version control systems, and which one Git is

- **Local VCS** — versions are stored only on your own machine (e.g. RCS). Simple but no real collaboration and no off-machine backup.
- **Centralized VCS (CVCS)** — a single central server holds all versions and everyone checks out from it (e.g. SVN, CVS). Collaboration works, but the server is a single point of failure.
- **Distributed VCS (DVCS)** — every contributor has a full copy of the repository, including its entire history (e.g. Git, Mercurial). Work offline, no single point of failure.

**Git is a distributed version control system (DVCS).**

## 3. Git's four areas

1. **Working directory** — the actual files on your disk that you edit; the current checked-out version of the project.
2. **Staging area (index)** — a holding area where you place the specific changes you want in your next commit (`git add`).
3. **Local repository** — the `.git` folder on your machine that stores all committed snapshots and history (`git commit`).
4. **Remote repository** — a copy hosted on a server (e.g. GitHub) used for backup and sharing; you sync with it via `git push` and `git pull`.

## 4. Difference between `git add` and `git commit`

`git add` moves changes from the working directory into the **staging area**, marking exactly which changes you want to include next. `git commit` takes everything currently staged and permanently records it as a **snapshot in the local repository** with a message. In short: `add` selects/prepares changes, `commit` saves them to history.

## 5. What a branch is and why branches matter

A branch is an independent, movable line of development — essentially a lightweight pointer to a commit — that lets you work on something without affecting the main line of code. Branches matter because they let you develop features, fix bugs, or experiment in isolation, keep `main` stable, and enable multiple people to work in parallel before merging their work together.

## 6. Fast-forward merge vs. three-way merge

A **fast-forward merge** happens when the target branch (e.g. `main`) hasn't moved since the feature branch was created, so Git simply slides the branch pointer forward to the latest commit — no new merge commit is needed. A **three-way merge** happens when both branches have new commits; Git combines the two branch tips using their common ancestor (the three "points") and creates a new **merge commit** to tie the histories together.

## 7. What a merge conflict is and how to resolve it

A merge conflict occurs when two branches change the **same lines of the same file** (or one edits a file the other deleted), so Git can't decide automatically which version to keep. To resolve it: open the conflicted file(s), find the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), manually edit the content to the correct final version and remove the markers, then `git add` the resolved files and `git commit` to complete the merge.

## 8. Difference between Git and GitHub

**Git** is the version control software (a command-line tool) that runs locally and tracks your project's history. **GitHub** is an online platform/service that **hosts** Git repositories in the cloud, adding collaboration features like pull requests, issues, code review, and access control. Git works without GitHub; GitHub exists to host and share Git repositories.

## 9. Difference between `git pull` and `git fetch`

`git fetch` downloads new commits and references from the remote into your local repo but **does not change your working files** — it just updates your knowledge of the remote, so you can inspect changes first. `git pull` does a `fetch` **and then immediately merges** (or rebases) those changes into your current branch. In short: `fetch` = download only; `pull` = download **and** integrate.

## 10. What a `.gitignore` file is, and why you should never commit secrets

A `.gitignore` file lists patterns of files and folders that Git should intentionally **not track** — such as OS junk (`.DS_Store`, `Thumbs.db`), logs, build output, and `node_modules/`. You should never commit secrets (passwords, API keys, tokens, `.env` files) because once committed they live in the repository's **history forever** — even if deleted later — and if the repo is public or shared, anyone can retrieve them and abuse the credentials. Keep secrets out via `.gitignore` and environment variables.
