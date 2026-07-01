# Mini Project 1 — Student Management App

A complete multi-screen Flutter app (Section 31): a **Home hub** that navigates
via **named routes** to a **Student List**, a **Profile**, and a **Settings**
screen. Tapping a student opens a **Details** screen with the student's data
passed in through the constructor. All data is sample/placeholder data.

## Screens
- **Home** — a welcome hub with three navigation buttons.
- **Students** — a `ListView` of students in cards; tap one for details.
- **Student Details** — avatar, name, course, and year (data passed in).
- **Profile** — a demo admin profile.
- **Settings** — a list of settings rows.

## Files
```
1_student_management_app/
├── lib/main.dart      ← all screens + named routes + theme
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
Then: from **Home**, open **Students**, tap a student to see details passed forward.

## How to stop
Press **q** (or **Ctrl+C**) in the `flutter run` terminal.

## Concepts
Named routes (`initialRoute` + `routes`), `Navigator.pushNamed`,
`MaterialPageRoute` with constructor data passing, `ListView.builder`, `Card`,
`ListTile`, `CircleAvatar`, and centralized theming.
