# Day 9 — Basics of Flutter and Dart

This folder contains all the work for **Day 9**: the capstone Flutter app, the
practical lab, the theory answers, and the Flutter & Dart practice exercises.
All code uses **demo / placeholder data only** — no personal information.

## Contents

| Item | Type | Description |
|------|------|-------------|
| [`Day9_Basics_of_Flutter_and_Dart.md`](Day9_Basics_of_Flutter_and_Dart.md) | Notes | The original Day 9 chapter / source material. |
| [`Day9_Theory_Questions.md`](Day9_Theory_Questions.md) | Theory | The 10 theory questions answered. |
| [`student_profile_app/`](student_profile_app/) | Flutter app | The Section 27 capstone — Student Profile App. |
| [`profile_app/`](profile_app/) | Flutter app | The Practical Lab project (create → run → build → hot reload). |
| [`flutter_tasks/`](flutter_tasks/) | Flutter | 5 small Flutter task apps (About Me, profile, container, etc.). |
| [`dart_challenges/`](dart_challenges/) | Dart | 5 standalone Dart programs covering language basics. |

## What Day 9 Covers

- What Flutter and Dart are, and Flutter's three architectural layers.
- `StatelessWidget` vs `StatefulWidget`, and "everything is a widget."
- Core widgets: `Scaffold`, `AppBar`, `Column`, `Row`, `Center`, `Container`,
  `Text`, `Icon`, `CircleAvatar`, `SizedBox`, `SingleChildScrollView`.
- The full workflow: setup → `flutter create` → `flutter run` → hot reload.
- Dart basics: variable types, operators (incl. `~/`), string interpolation,
  ternary, `List`, and `Map`.

## Folder Guide

### `student_profile_app/` — Capstone (Section 27)
The complete Student Profile App: a blue app bar, a centered circular avatar
with name and role, then About / Skills / Contact sections.
→ See [`student_profile_app/README.md`](student_profile_app/README.md).

### `profile_app/` — Practical Lab
The hands-on lab project. The README walks through the full 7-step workflow
(verify install, start emulator, create, run, hot reload, build the UI,
experiment & inspect).
→ See [`profile_app/README.md`](profile_app/README.md).

### `flutter_tasks/` — Flutter Tasks
Five standalone demo apps, one per task:
1. About Me screen · 2. Student Profile · 3. Profile + Education section ·
4. Container with padding/margin/color · 5. Centered CircleAvatar.
→ See [`flutter_tasks/README.md`](flutter_tasks/README.md).

### `dart_challenges/` — Dart Challenges
Five small Dart programs: variable types · arithmetic operators · string
interpolation · ternary even/odd · List & Map.
→ See [`dart_challenges/README.md`](dart_challenges/README.md).

## Running the Code

> **Note:** The Flutter/Dart SDK was **not** installed when these folders were
> created, so files were written by hand. After installing the SDK:
> - For each Flutter project, run `flutter create .` inside its folder once to
>   generate the `android/`, `ios/`, and `web/` platform folders (it keeps the
>   existing `lib/` files), then `flutter pub get` and `flutter run`.
> - For Dart files, use `dart run <file>` — or paste into
>   [dartpad.dev](https://dartpad.dev).

## Web → Flutter Connection

Day 9 mirrors the web portfolio from earlier days as a mobile app:

| Web (Days 2–6) | Flutter |
|----------------|---------|
| `border-radius: 50%` photo | `CircleAvatar` |
| `align-items: flex-start` | `CrossAxisAlignment.start` |
| Flexbox row | `Row` |
| CSS padding / margin | `EdgeInsets` / `SizedBox` |
| Headings & paragraphs | `Text` + `TextStyle` |
