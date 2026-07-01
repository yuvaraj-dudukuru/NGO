# Mini Project 2 — Recipe App

A two-screen Flutter app: a **list of recipes**, and a **details screen** showing
each recipe's ingredients and numbered step-by-step instructions. All recipes are
sample data; a colored icon stands in for a photo so it runs offline.

## Screens
- **Recipe List** — recipes in cards (name, time, difficulty); tap to open details.
- **Recipe Details** — a colored header, time/difficulty chips, an ingredients
  list, and numbered steps.

## Files
```
2_recipe_app/
├── lib/main.dart      ← both screens + the sample recipe data
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
Then tap any recipe to read its ingredients and steps.

## How to stop
Press **q** (or **Ctrl+C**) in the `flutter run` terminal.

## Concepts
`ListView.builder`, `Navigator.push` with `MaterialPageRoute`, passing a data
map into a screen, `Chip`, `Container` with `BoxDecoration`, and spreading a list
of widgets with `...` and `List.generate`.
