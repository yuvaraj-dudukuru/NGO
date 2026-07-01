# Mini Projects — Day 10

Five **separate, self-contained Flutter apps**, one per Day 10 mini project. Each lives
in its own folder with its own `lib/main.dart` and `pubspec.yaml`, so you can run them
independently.

> **Note:** All names, emails, recipes, contacts, and tasks are **placeholder/sample
> data** (e.g. "Aisha Verma", "Olivia Bennett", "Sam Keller") — none of your personal
> data is used. Placeholder icons stand in for images so every app runs fully offline.

---

## The Five Projects

| # | Folder | Project | What it does |
| - | ------ | ------- | ------------ |
| **1** | `1_student_management_app/` | **Student Management App** | The complete Section 31 app: Home hub → Student List → Student Details (data passed), plus Profile and Settings, wired with named routes. Sample students. |
| **2** | `2_recipe_app/` | **Recipe App** | A list of recipes; tap one to open a details screen with ingredients and step-by-step instructions. |
| **3** | `3_contacts_app/` | **Contacts App** | A divided list of contacts; tap one to open a details screen with phone, email, and city. |
| **4** | `4_portfolio_app/` | **Portfolio App** | A multi-screen portfolio: a Home profile, a Projects list, and a Contact screen, navigated with named routes. |
| **5** | `5_student_task_manager/` | **Student Task Manager** | The app planned on Day 8: Home → Task List → Task Details, with a checkbox to complete tasks and an **Add Task** screen that returns a new task on `pop`. |

---

## Concepts Across the Projects

- **Navigation:** `Navigator.push`/`pop`, named routes, passing data via constructors,
  and returning data on `pop` (projects 1, 4, 5).
- **Lists & cards:** `ListView.builder`, `Card`, `ListTile`, `Divider`, `CircleAvatar`.
- **Forms & state:** `TextField`, `DropdownButtonFormField`, `Checkbox`,
  `StatefulWidget`, `setState` (project 5).
- **App chrome:** `AppBar`, `FloatingActionButton`, `Chip`, theming.

---

## Folder Structure

```
mini_projects/
├── 1_student_management_app/   # lib/main.dart + pubspec.yaml
├── 2_recipe_app/               # lib/main.dart + pubspec.yaml
├── 3_contacts_app/             # lib/main.dart + pubspec.yaml
├── 4_portfolio_app/            # lib/main.dart + pubspec.yaml
├── 5_student_task_manager/     # lib/main.dart + pubspec.yaml
└── README.md                   # this file
```

---

## Running a Project

You need the [Flutter SDK](https://docs.flutter.dev/get-started/install) installed.
Each project runs on its own:

```bash
# pick a project folder, e.g.
cd 2_recipe_app
flutter pub get
flutter run
```

Pick a device (Android emulator, iOS simulator, Chrome, or desktop) when prompted.

### Highlights to try

- **Project 1:** From Home, open Students, tap a student to see details passed forward.
- **Project 2:** Tap a recipe to read its ingredients and numbered steps.
- **Project 3:** Tap a contact to see full details; use the back button to return.
- **Project 4:** From Home, jump to Projects or Contact via the buttons.
- **Project 5:** Tick a task done, open its details, or tap **+** to add a new task —
  the Add Task screen sends the task back to the list when you save.
