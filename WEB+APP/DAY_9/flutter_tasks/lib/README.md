# `lib/` — Flutter Tasks Source

This folder holds the Dart source for the **Flutter Tasks** project. Each task is
a **standalone app** with its own `main()`, so any one of them can be run on its
own. All data is demo/placeholder data — no personal information.

## Files

| File | What it is |
|------|------------|
| `main.dart` | The default entry point. It imports Task 2 and runs it, so a plain `flutter run` shows the Student Profile screen. |
| `task1_about_me.dart` | **Task 1** — a simple "About Me" screen (icon, name, description). |
| `task2_student_profile.dart` | **Task 2** — the Student Profile App (avatar, About, Skills, Contact). |
| `task3_profile_with_education.dart` | **Task 3** — Task 2 plus an extra "Education" section. |
| `task4_container.dart` | **Task 4** — a `Container` demo (padding, margin, background color, rounded corners). |
| `task5_centered_avatar.dart` | **Task 5** — a `CircleAvatar` + name centered with `Center` + `Column`. |

## How to run

> Requires the Flutter SDK. If the platform folders (`android/`, `ios/`, `web/`)
> don't exist yet, run `flutter create .` in the project root once first, then
> `flutter pub get`.

- **Default (Task 2):**
  ```bash
  flutter run
  ```
- **A specific task** (use its file as the entry point):
  ```bash
  flutter run -t lib/task1_about_me.dart
  flutter run -t lib/task4_container.dart
  ```

## How to stop

Press **q** in the terminal running `flutter run` (or **Ctrl+C**). With hot
reload active you can also press **R** to restart.

## Concepts

`StatelessWidget`, `MaterialApp`, `Scaffold`, `AppBar`, `Column`, `Row`,
`Center`, `Container`, `CircleAvatar`, `Icon`, `Text`, `SizedBox`,
`SingleChildScrollView`, and `EdgeInsets`.
