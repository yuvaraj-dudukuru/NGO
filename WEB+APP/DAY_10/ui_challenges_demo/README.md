# UI Challenges Demo — Day 10

A single runnable Flutter app containing all **five Day 10 UI challenges**. The app
opens to a menu; tap an item to open that challenge, and use the back button to return.

> **Note:** All names, emails, and products are **placeholder/sample data** (e.g.
> "Jordan Doe", "Alex Rivera", `you@example.com`) — none of your personal data is used.
> The product "images" are placeholder icons so the app runs fully offline.

---

## The Five Challenges

| # | Challenge | What it demonstrates |
| - | --------- | -------------------- |
| **1** | **Profile Card** | A `Card` holding a `Row` of an avatar and an `Expanded` `Column` of name + details (role, location, email). Shows how `Expanded` lets the text fill the remaining width. |
| **2** | **Login Form** | Two `TextField`s (email + password) with icons, a show/hide password toggle, and a submit button. Submitting shows a `SnackBar`. |
| **3** | **Settings Screen** | A `ListView` of `ListTile`s separated by `Divider`s — the standard settings-list pattern, including a switch and chevrons. |
| **4** | **Product Grid** | A 2-column `GridView.builder` of product cards, each with a placeholder image area, a name, and a price. |
| **5** | **Full Scaffold** | A complete `Scaffold`: an `AppBar` with action buttons, a body, a `FloatingActionButton`, and a `Drawer` with a header and menu items. |

---

## Key Concepts

- **Layout:** `Card`, `Row`, `Column`, `Expanded`, `Padding`, `CircleAvatar`.
- **Input:** `TextField`, `TextEditingController`, password obscuring, `SnackBar`.
- **Lists:** `ListView`, `ListTile`, `Divider`.
- **Grids:** `GridView.builder` with `SliverGridDelegateWithFixedCrossAxisCount`.
- **App chrome:** `AppBar` actions, `FloatingActionButton`, `Drawer`, `DrawerHeader`.

---

## Project Structure

```
ui_challenges_demo/
├── lib/
│   └── main.dart     # menu + all five challenge screens
├── pubspec.yaml      # project metadata and dependencies
└── README.md         # this file
```

---

## Running the Demo

You need the [Flutter SDK](https://docs.flutter.dev/get-started/install) installed.

```bash
# from inside the ui_challenges_demo folder
flutter pub get
flutter run
```

Pick a device (Android emulator, iOS simulator, Chrome, or desktop) when prompted,
then tap each menu item to explore the challenge.

### Expected result

1. **Profile Card** — an avatar beside name, role, location, and email in a card.
2. **Login Form** — email + password fields with a working show/hide toggle and a Sign In button.
3. **Settings** — a divided list of settings rows.
4. **Product Grid** — a 2-column grid of sample products with placeholder images and prices.
5. **Full Scaffold** — open the drawer (top-left), tap the AppBar actions, or press the + FAB.
