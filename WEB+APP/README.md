# Web & Mobile App Development — 10-Day Course

A hands-on, day-by-day learning curriculum that goes from a first HTML page all
the way to multi-screen Flutter mobile apps. Each `DAY_*` folder is
self-contained, with its own README, practical lab, coding challenges, mini
projects, and theory answers.

> **Privacy note:** Every project uses **placeholder / demo data only** (names
> like "Alex Carter", "Priya Sharma", emails like `alex.carter@example.com`).
> No personal information is included — replace the placeholders with your own
> details before publishing anything.

## 🗺️ Course Map

| Day | Topic | Stack | Folder |
|-----|-------|-------|--------|
| 1 | First web page — HTML basics | HTML | [DAY_1/](DAY_1/) |
| 2 | HTML5 basics (semantic tags, forms, media) | HTML | [DAY_2/](DAY_2/) |
| 3 | CSS3 styling & a personal profile page | HTML + CSS | [DAY_3/](DAY_3/) |
| 4 | JavaScript basics (variables, functions, DOM) | HTML + CSS + JS | [DAY_4/](DAY_4/) |
| 5 | ES6 concepts & DOM manipulation | HTML + CSS + JS | [DAY_5/](DAY_5/) |
| 6 | Responsive design, Flexbox & Grid | HTML + CSS (+ JS) | [DAY_6/](DAY_6/) |
| 7 | Introduction to Git and GitHub | Git + web | [DAY_7/](DAY_7/) |
| 8 | Mobile apps & cross-platform planning | Planning docs | [DAY_8/](DAY_8/) |
| 9 | Basics of Flutter and Dart | Dart + Flutter | [DAY_9/](DAY_9/) |
| 10 | Flutter UI, layouts & navigation | Flutter | [DAY_10/](DAY_10/) |

## 📂 Structure

Each day generally follows the same pattern:

```
DAY_N/
├── README.md                 ← overview of the day (start here)
├── <Theory>.md               ← the day's theory questions & answers
├── <lab>/                    ← a step-by-step practical lab
├── <challenges>/             ← focused coding challenges
└── <mini-projects>/          ← larger, self-contained builds
```

Every folder and sub-folder has its own README explaining what it is, how it
works, how to run it, and how to stop it.

## ▶️ How to run the projects

**Web projects (Days 1–7)** are static — no build step or server needed:

1. Open the project folder.
2. Double-click `index.html`, or right-click → **Open with** → your browser.
3. (Optional) In VS Code, use the **Live Server** extension for auto-reload.
4. For JavaScript exercises, press **F12** to open the DevTools **Console**.

**Flutter projects (Days 9–10)** need the
[Flutter SDK](https://docs.flutter.dev/get-started/install):

```bash
cd <a-flutter-project-folder>
flutter create .      # only if android/ ios/ web/ are missing (keeps lib/)
flutter pub get
flutter run
```

**Dart-only files (Day 9 challenges):** run with `dart run <file>.dart`, or paste
them into [dartpad.dev](https://dartpad.dev).

## 🛑 How to stop the projects

- **Web:** close the browser tab. If you used **Live Server**, stop it from the
  VS Code status bar.
- **Flutter:** in the terminal running `flutter run`, press **q** to quit (or
  **Ctrl+C**). While running, **r** = hot reload, **R** = hot restart.

## ✅ Status

- All web pages: valid JavaScript syntax, no broken local CSS/JS references, and
  balanced HTML tags.
- All Flutter/Dart files: balanced and reviewed; `pubspec.yaml` files are valid.
- All personal data has been replaced with neutral placeholder data.

> **Tooling note:** the Flutter/Dart SDK was not installed in the authoring
> environment, so the Dart/Flutter apps were verified by static review (syntax,
> structure, and pubspec validity) rather than by a live `flutter run`. Run
> `flutter analyze` once the SDK is installed for a full compile check.
