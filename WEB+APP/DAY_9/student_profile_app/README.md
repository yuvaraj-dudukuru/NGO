# Student Profile App

My first complete Flutter application — the **Day 9 capstone**. It displays a
student's profile (info, profile section, skills, and contact details) and is
built entirely with `StatelessWidget`s, since the information does not change.

This is the mobile parallel of the personal portfolio built for the web on
Days 2, 3, and 6 — the same idea, now as a Flutter app.

## Screen Layout

```
+-------------------------------+
|  Student Profile     (AppBar) |
+-------------------------------+
|        [Profile Icon]         |
|         Priya Sharma          |  <- profile section
|    Web Development Student     |
+-------------------------------+
|  About                        |  <- info section
|  A first-year student...       |
+-------------------------------+
|  Skills                       |
|  - HTML, CSS, JavaScript       |  <- skills section
|  - Flutter & Dart              |
|  - Git & GitHub                |
+-------------------------------+
|  Contact                      |  <- contact section
|  Email: priya@example.com      |
|  Phone: +91 98765 43210        |
+-------------------------------+
```

## Project Structure

```
student_profile_app/
├── lib/
│   └── main.dart      # the entire app
├── pubspec.yaml       # project metadata & dependencies
└── README.md
```

## How to Run

You need the Flutter SDK installed and an emulator or device connected.

```bash
flutter pub get   # fetch dependencies
flutter run       # launch on the emulator/device
```

In VS Code you can also press the **Run** button (or `F5`) with `lib/main.dart`
open.

## What It Demonstrates

| Concept | Where it's used |
|---------|-----------------|
| `StatelessWidget` | `StudentProfileApp`, `ProfileScreen` |
| `MaterialApp` | app setup, title, `home` screen |
| `Scaffold` + `AppBar` | screen structure and blue top bar |
| `SingleChildScrollView` | makes the content scrollable |
| `Column` / `Row` | vertical and horizontal layout |
| `Center`, `SizedBox` | alignment and spacing |
| `Text` + `TextStyle` | typography (size, weight, color) |
| `Icon` / `Icons` | check, email, and phone icons |
| `CircleAvatar` | circular profile picture (like `border-radius: 50%`) |
| `EdgeInsets` | padding (the box model) |

## Web → Flutter Mapping

| Web (Days 2–6) | Flutter |
|----------------|---------|
| `border-radius: 50%` photo | `CircleAvatar` |
| `align-items: flex-start` | `CrossAxisAlignment.start` |
| Flexbox row | `Row` |
| CSS padding / margins | `EdgeInsets` / `SizedBox` |
| Headings & paragraphs | `Text` + `TextStyle` |

## Expected Result

A blue app bar titled **"Student Profile,"** a centered circular profile icon
with the name and role, followed by **About**, **Skills**, and **Contact**
sections with icons and text — scrollable if the content is taller than the
screen.
