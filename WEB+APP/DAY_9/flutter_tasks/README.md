# Day 9 — Flutter Tasks (Demo)

Five small Flutter exercises, each a **standalone app** in its own file under
`lib/`. All use **demo / placeholder data only** (e.g. "Alex Demo",
`alex@example.com`) — no personal information.

## The Tasks

| # | File | What it demonstrates |
|---|------|----------------------|
| 1 | [`lib/task1_about_me.dart`](lib/task1_about_me.dart) | An "About Me" `StatelessWidget` with a name, description, and an icon. |
| 2 | [`lib/task2_student_profile.dart`](lib/task2_student_profile.dart) | The Student Profile App from Section 27 (Profile / About / Skills / Contact). |
| 3 | [`lib/task3_profile_with_education.dart`](lib/task3_profile_with_education.dart) | The profile app with a **4th section** added: **Education**. |
| 4 | [`lib/task4_container.dart`](lib/task4_container.dart) | A `Container` with `padding`, `margin`, and a background color wrapping a `Text`. |
| 5 | [`lib/task5_centered_avatar.dart`](lib/task5_centered_avatar.dart) | A `CircleAvatar` + name centered with `Center` and `Column`. |

## How to Run

Each file has its own `main()`, so you choose which one to run with the
`-t` (target) flag:

```bash
flutter pub get

flutter run -t lib/task1_about_me.dart
flutter run -t lib/task2_student_profile.dart
flutter run -t lib/task3_profile_with_education.dart
flutter run -t lib/task4_container.dart
flutter run -t lib/task5_centered_avatar.dart
```

A plain `flutter run` (no `-t`) launches **Task 2** by default
(via `lib/main.dart`).

## Notes

- Flutter was **not** installed when this folder was created, so the files were
  written by hand. Install the Flutter SDK and run `flutter create .` inside
  this folder once to generate the `android/`, `ios/`, and `web/` platform
  folders (it keeps everything in `lib/`).
- All data is fictional/demo — swap in your own details later if you wish.

## Key Widgets Used

`Scaffold` · `AppBar` · `Column` · `Row` · `Center` · `Container` ·
`Padding` · `SizedBox` · `Text` · `Icon` · `CircleAvatar` ·
`SingleChildScrollView` · `Expanded` · `BoxDecoration`
