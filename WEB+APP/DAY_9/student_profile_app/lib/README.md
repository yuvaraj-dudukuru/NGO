# `lib/` — Student Profile App Source

This folder holds the Dart source for the Day 9 **capstone** (Section 27). All
data is demo/placeholder data — no personal information.

## Files

| File | What it is |
|------|------------|
| `main.dart` | The whole app: `main()` → `StudentProfileApp` (root `MaterialApp`) → `ProfileScreen`. A blue `AppBar` sits above a scrollable column with a centered circular avatar (name + role), then About, Skills, and Contact sections. |

## How it works

- `main()` runs the root `StudentProfileApp` widget.
- `StudentProfileApp` (a `StatelessWidget`) returns a `MaterialApp`.
- `ProfileScreen` (a `StatelessWidget`) returns a `Scaffold`. Its body is a
  `SingleChildScrollView` containing a `Column` of sections, each built from
  `Text` headings and `Row`s of `Icon` + `Text`. Because the content never
  changes, a `StatelessWidget` is the right choice.

## How to run

> Requires the Flutter SDK. If `android/` / `ios/` / `web/` don't exist yet, run
> `flutter create .` in the project root once, then `flutter pub get`.

```bash
flutter run
```

## How to stop

Press **q** (or **Ctrl+C**) in the terminal running `flutter run`.

## Concepts

`StatelessWidget`, `MaterialApp`, `Scaffold`, `AppBar`, `SingleChildScrollView`,
`Column`, `Row`, `Center`, `CircleAvatar`, `Icon`, `Text`, `SizedBox`,
`CrossAxisAlignment`, `EdgeInsets`.
