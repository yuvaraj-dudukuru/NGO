# Navigation Challenges Demo — Day 10

A single runnable Flutter app containing all **five Day 10 navigation challenges**.
The app opens to a menu; tap an item to run that challenge, and use the back button
(or each screen's button) to navigate.

> **Note:** All names and items are **placeholder/sample data** (e.g. "Nova Carter",
> "Liam Brooks", fruit names) — none of your personal data is used.

---

## The Five Challenges

| # | Challenge | What it demonstrates |
| - | --------- | -------------------- |
| **1** | **push / pop** | Two screens connected with `Navigator.push` (forward) and `Navigator.pop` (back). |
| **2** | **Named routes** | The same flow, but using routes registered in `MaterialApp.routes` and navigated with `Navigator.pushNamed`. |
| **3** | **List → Details (pass data)** | A list of people; tapping one pushes a details screen, passing the person's data through the **constructor**. |
| **4** | **Home → three screens** | A hub screen with three buttons that navigate to three different (red / green / blue) screens via named routes. |
| **5** | **Return data on pop** | A screen pushes a picker, `await`s its result, and the picker returns the chosen value with `Navigator.pop(context, value)`. |

---

## Key Concepts

- **Forward / back:** `Navigator.push(MaterialPageRoute(...))` and `Navigator.pop()`.
- **Named routes:** central registration in `MaterialApp.routes` + `Navigator.pushNamed`.
- **Passing data forward:** through the destination screen's constructor.
- **Returning data backward:** `Navigator.pop(context, result)` + `await`ing the push.
- **The navigation stack:** screens stacked last-in-first-out, with automatic back buttons.

---

## Project Structure

```
navigation_challenges_demo/
├── lib/
│   └── main.dart     # menu + all five challenge screens + named routes
├── pubspec.yaml      # project metadata and dependencies
└── README.md         # this file
```

---

## Running the Demo

You need the [Flutter SDK](https://docs.flutter.dev/get-started/install) installed.

```bash
# from inside the navigation_challenges_demo folder
flutter pub get
flutter run
```

Pick a device (Android emulator, iOS simulator, Chrome, or desktop) when prompted,
then tap each menu item to explore the challenge.

### Expected result

1. **push / pop** — go forward to Screen Two, then back to Screen One.
2. **Named routes** — navigate A → B and back using `pushNamed`.
3. **List → Details** — tap a person to see their details on a new screen.
4. **Hub** — three buttons open three differently-colored screens.
5. **Return data on pop** — pick a fruit and watch the home screen update with your choice.
