# Mini Project 5 — Student Task Manager

The app planned on Day 8, now built: a multi-screen task manager with **state**.
Tick tasks complete, open a task's details, or add a new task via a form that
**returns the new task on pop**. All starting tasks are sample data.

## Screens
- **Home** — an intro screen with a **My Tasks** button.
- **Task List** — tasks in cards with a checkbox, subject, and a colored
  priority chip; tap a task for details. A **+** button opens the Add Task screen.
- **Task Details** — title, subject, priority, and status.
- **Add Task** — a form (title, subject, priority dropdown) that validates the
  title and returns a new `Task` to the list.

## Files
```
5_student_task_manager/
├── lib/main.dart      ← Task model + all four screens (with state)
├── pubspec.yaml       ← project metadata & dependencies
└── README.md          ← this file
```

## How to run
> Requires the Flutter SDK. If `android/` / `ios/` / `web/` are missing, run
> `flutter create .` here once first.
```bash
flutter pub get
flutter run
```
Then tick a task done, open its details, or tap **+** to add a task — the Add
Task screen sends the task back to the list when you save.

## How to stop
Press **q** (or **Ctrl+C**) in the `flutter run` terminal.

## Concepts
`StatefulWidget` + `setState`, a custom `Task` model, `Checkbox`,
`DropdownButtonFormField`, `TextEditingController` (with `dispose`),
returning data via `Navigator.pop(context, value)`, `FloatingActionButton`, and
`SnackBar` validation feedback.
