# Day 10 — Flutter UI, Layouts & Navigation

All the work for **Day 10**: building real multi-screen Flutter apps. It covers
core widgets and layouts (`Row`, `Column`, `Stack`, `Expanded`, `ListView`,
`GridView`), app chrome (`AppBar`, `Drawer`, `FloatingActionButton`), forms, and
**navigation** (`Navigator.push`/`pop`, named routes, passing data forward, and
returning data on pop).

All names, emails, and other details are **placeholder/sample data only** — no
personal information. Placeholder icons stand in for images so every app runs
fully offline.

## 📁 Folder structure

```
DAY_10/
├── README.md                      ← you are here
├── Day10_Theory_Questions.md      ← the day's theory questions & answers
│
├── student_app/                   ← Practical Lab: Home → List → Details
├── student_management_app/        ← Section 31 demo: hub + named routes + details
│
├── ui_challenges_demo/            ← 5 UI challenges (profile card, login, settings, grid, scaffold)
├── practical_exercises_demo/      ← 5 layout exercises (Row, Column+Expanded, Stack, ListView, GridView)
├── navigation_challenges_demo/    ← 5 navigation challenges (push/pop, named, pass data, hub, return-on-pop)
│
└── mini_projects/                 ← 5 standalone mini-app projects
    ├── 1_student_management_app/
    ├── 2_recipe_app/
    ├── 3_contacts_app/
    ├── 4_portfolio_app/
    └── 5_student_task_manager/
```

## 📦 What's inside

| Folder | Type | What it is |
|--------|------|------------|
| [`student_app/`](student_app/) | Lab | The step-by-step practical lab: Home → List → Details with data passing. |
| [`student_management_app/`](student_management_app/) | Demo | The Section 31 app: a Home hub with named routes to Students, Profile, and Settings, plus a data-passing details screen. |
| [`ui_challenges_demo/`](ui_challenges_demo/) | Demo | Five UI challenges accessed from a menu (profile card, login form, settings list, product grid, full Scaffold with Drawer/FAB). |
| [`practical_exercises_demo/`](practical_exercises_demo/) | Demo | Five layout exercises (Row alignment, Column + Expanded, Stack + Positioned, ListView.builder, GridView.count). |
| [`navigation_challenges_demo/`](navigation_challenges_demo/) | Demo | Five navigation challenges (push/pop, named routes, pass data, hub to three screens, return data on pop). |
| [`mini_projects/`](mini_projects/) | Projects | Five separate apps — Student Management, Recipe, Contacts, Portfolio, and Student Task Manager. |

Each of these folders has its own README with full details.

## ▶️ How to run

> All Flutter apps require the [Flutter SDK](https://docs.flutter.dev/get-started/install).
> If a project has no `android/` / `ios/` / `web/` folders yet, run `flutter create .`
> inside it once first (it keeps the existing `lib/`).

```bash
cd <one-of-the-app-folders>
flutter pub get
flutter run
```

Pick a device (Android emulator, iOS simulator, Chrome, or desktop) when prompted.

## 🛑 How to stop

In the terminal running `flutter run`, press **q** to quit (or **Ctrl+C**). While
it's running you can press **r** for hot reload and **R** for hot restart.

## ✅ Skills exercised

Widgets & layout (`Row`/`Column`/`Stack`/`Expanded`/`ListView`/`GridView`),
`Card`/`ListTile`/`CircleAvatar`/`Chip`, app chrome (`AppBar`/`Drawer`/`FAB`),
forms (`TextField`/`DropdownButtonFormField`/`Checkbox`), state
(`StatefulWidget` + `setState`), theming, and the full navigation toolkit.
