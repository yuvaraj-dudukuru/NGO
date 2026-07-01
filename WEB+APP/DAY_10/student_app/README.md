# student_app — Day 10 Practical Lab

A hands-on **multi-screen Flutter app** built step by step in the Day 10 lab.
You navigate from a **Home** screen to a **List** of names, then tap a name to open
a **Details** screen that shows it — passing data between screens along the way.

This is a portfolio piece: it exercises every core Day 10 skill — building UI with
widgets, layouts, lists, cards, and buttons, plus navigation with `push`/`pop` and
data passing.

---

## App Flow

```
[Home Screen]  --tap "View List"-->  [List Screen]  --tap a name-->  [Details Screen]
   (button)                          (ListView of names)            (shows the name)

         <-- back button -- <-- back button --
```

---

## What Each Step Built

| Step | What you did | Result |
| ---- | ------------ | ------ |
| **1** | `flutter create student_app` | A fresh Flutter project |
| **2** | Built the **Home** screen (Scaffold + AppBar + button) | A "View List" button on a title bar |
| **3** | Built the **List** screen (`ListView.builder` of name cards) | A scrollable list of names |
| **4** | Added navigation from Home → List | Tapping the button opens the list (auto back button) |
| **5** | Built the **Details** screen and passed the tapped name to it | Tapping a name shows it on its own screen |
| **6** | Combined everything into one working app | Home → List → Details, with data passing |

---

## Key Concepts

- **UI components:** `Scaffold`, `AppBar`, `ElevatedButton`, `ListView.builder`,
  `Card`, `ListTile`, `Icon`, `Center`, `Column`, `Text`.
- **Navigation:** `Navigator.push` with `MaterialPageRoute`; the automatic back
  button from `pop`.
- **Passing data:** the tapped name is sent into `DetailsScreen` through its
  constructor (`DetailsScreen({required this.name})`).

---

## Project Structure

```
student_app/
├── lib/
│   └── main.dart     # MyApp + HomeScreen + ListScreen + DetailsScreen
├── pubspec.yaml      # project metadata and dependencies
└── README.md         # this file
```

---

## Running the App

You need the [Flutter SDK](https://docs.flutter.dev/get-started/install) installed.

```bash
# from inside the student_app folder
flutter pub get
flutter run
```

Pick a device (Android emulator, iOS simulator, Chrome, or desktop) when prompted.

### Expected result

1. **Home** screen shows a "View List" button.
2. Tapping it opens the **List** screen — cards of names (Priya, Arjun, Sara, Ravi).
3. Tapping a name opens the **Details** screen showing that name (data passed).
4. Back buttons return you through Details → List → Home.

---

## Next Step

> Keep this project and commit it to GitHub (Day 7). Run the lab until building
> screens and connecting them with navigation feels natural — this is the core skill
> for building real Flutter apps. Optionally, extend it with the full Student
> Management App from Section 31 (see the sibling `student_management_app/` folder).
