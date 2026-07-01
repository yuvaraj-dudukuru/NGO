# Mini Project 4 — Portfolio App

A multi-screen Flutter portfolio navigated with **named routes**: a **Home**
profile, a **Projects** list, and a **Contact** screen. All details are
placeholder/sample data.

## Screens
- **Home** — an avatar, name, role, and buttons to **View Projects** / **Contact Me**.
- **Projects** — a list of demo projects with short descriptions.
- **Contact** — email, phone, website, and location rows.

## Files
```
4_portfolio_app/
├── lib/main.dart      ← all three screens + named routes
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
Then from **Home**, jump to **Projects** or **Contact** via the buttons.

## How to stop
Press **q** (or **Ctrl+C**) in the `flutter run` terminal.

## Concepts
Named routes (`initialRoute` + `routes`), `Navigator.pushNamed`,
`ElevatedButton`/`OutlinedButton`, `ListView.builder`, `Card`, and `ListTile`.
