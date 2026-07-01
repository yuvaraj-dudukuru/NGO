# `lib/` — practical_exercises_demo Source

Holds the Dart source for the five Day 10 layout exercises.

## Files
| File | What it is |
|------|------------|
| `main.dart` | A menu (`MenuScreen`) that opens each exercise: `RowExercise` (a `StatefulWidget` that cycles `mainAxisAlignment` values), `ColumnExpandedExercise` (`Expanded` filling the middle), `StackExercise` (`Stack` + `Positioned` badge), `ListViewExercise` (`ListView.builder` of 10 items), and `GridViewExercise` (`GridView.count`, 2 columns). |

## How to run / stop
From the project root (one level up): `flutter pub get` then `flutter run`.
Press **q** to stop. See the parent [README](../README.md) for full details.
