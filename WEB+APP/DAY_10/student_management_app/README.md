# Student Management App

> **Day 10 Capstone — the culmination of the Foundation Phase.**

A complete, navigable **multi-screen Flutter application** that combines today's UI
components (Scaffold, ListView, Card, ListTile, buttons, CircleAvatar) with
**navigation** (named routes, `push`/`pop`, and passing data between screens),
reusable widgets (composition), and a centralized theme.

This is exactly the kind of app you planned conceptually on Day 8 (the Student Task
Manager) — now built for real.

---

## App Map

```
STUDENT MANAGEMENT APP

[Home Screen]                     <- hub with navigation buttons
   |
   +--> [Student List Screen]     <- a ListView of students
   |        |
   |        +--> [Student Details]  <- shows one student (data passed)
   |
   +--> [Profile Screen]          <- the user's profile
   |
   +--> [Settings Screen]         <- app settings

Navigation: named routes + push/pop + passing data
```

---

## Screens

| Screen | What it does | Key concepts |
| ------ | ------------ | ------------ |
| **Home** | A hub centering a school icon, a welcome message, and three navigation buttons. | `Navigator.pushNamed`, reusable `_buildNavButton` helper (DRY) |
| **Student List** | A scrollable list of student cards built with `ListView.builder`. | `ListView.builder`, `Card`, `ListTile`, `CircleAvatar` |
| **Student Details** | Shows one student's name, course, and year. Data is passed in through the constructor. | Passing data via constructor, `MaterialPageRoute`, auto back button |
| **Profile** | A simple centered profile screen. | `Center`, `Column`, `CircleAvatar` |
| **Settings** | A `ListView` of settings options separated by dividers. | Settings-list pattern, `Divider` |

---

## How Navigation Works

- **Named routes** (`/`, `/students`, `/profile`, `/settings`) are registered in
  `MaterialApp.routes`. The Home buttons navigate with
  `Navigator.pushNamed(context, route)`.
- **Passing data** to the details screen is done with `Navigator.push` +
  `MaterialPageRoute`, sending the tapped student's `Map` into the
  `StudentDetailsScreen` constructor. (That's why the details screen is *not* a
  simple named route.)
- **Going back** is automatic: any screen pushed onto the stack gets a back button
  in its `AppBar`, which pops back to the previous screen.

---

## Project Structure

```
student_management_app/
├── lib/
│   └── main.dart      # app setup + all five screen classes
├── pubspec.yaml       # project metadata and dependencies
└── README.md          # this file
```

> For clarity, all screens live in one file (`main.dart`). In a production app you
> would split each screen into its own file (e.g. `lib/screens/home_screen.dart`).

---

## Running the App

You need the [Flutter SDK](https://docs.flutter.dev/get-started/install) installed.

```bash
# from inside the student_management_app folder
flutter pub get
flutter run
```

Pick a target device (Android emulator, iOS simulator, Chrome, or desktop) when
prompted.

### Expected result

1. The **Home** screen shows a welcome and three navigation buttons.
2. Tapping **View Students** opens the **Student List** (a scrollable list of cards).
3. Tapping a student opens **Student Details** showing that student's info (data passed).
4. The back button returns to the list, then to home.
5. **Profile** and **Settings** open their respective screens.
6. Every screen has a back button to return.

---

## Concepts Practiced

- **UI components:** `Scaffold`, `AppBar`, `ListView` / `ListView.builder`, `Card`,
  `ListTile`, `ElevatedButton.icon`, `CircleAvatar`, `Icon`, `Divider`.
- **Layout:** `Column`, `Padding`, `Center`, `SizedBox`, `EdgeInsets`.
- **Navigation:** named routes, `push`/`pop`, passing data between screens.
- **Composition (DRY):** reusable helper widgets `_buildNavButton` and
  `_buildDetailCard`.
- **Theming:** a centralized `ThemeData` for consistent styling.

---

🎓 **Milestone:** You've moved from a single screen (Day 9) to a full multi-screen
app — which is what real mobile applications are.
