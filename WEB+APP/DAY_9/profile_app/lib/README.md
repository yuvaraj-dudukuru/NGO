# `lib/` — Profile App Source

This folder holds the Dart source for the Day 9 **Practical Lab** project. All
data is demo/placeholder data — no personal information.

## Files

| File | What it is |
|------|------------|
| `main.dart` | The whole app: `main()` → `StudentProfileApp` (root `MaterialApp`) → `ProfileScreen`. The screen shows a centered `CircleAvatar`, name, and role, followed by About, Skills, and Contact sections inside a `SingleChildScrollView`. |

## How it works

- `main()` calls `runApp()` with the root widget.
- `StudentProfileApp` is a `StatelessWidget` that returns a `MaterialApp`.
- `ProfileScreen` builds a `Scaffold` with an `AppBar` and a scrollable `Column`
  of sections. Everything is static, so a `StatelessWidget` is appropriate.

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
`EdgeInsets`.
