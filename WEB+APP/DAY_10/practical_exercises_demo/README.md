# Practical Exercises Demo — Day 10

A single runnable Flutter app that demonstrates all **five Day 10 practical
exercises**. The app opens to a menu; tap any item to open that exercise's screen,
and use the back button to return.

---

## The Five Exercises

| # | Exercise | What it demonstrates |
| - | -------- | -------------------- |
| **1** | **Row + `mainAxisAlignment`** | A `Row` of three colored boxes (A, B, C). Tap the chips at the bottom to switch between `start`, `center`, `end`, `spaceBetween`, `spaceAround`, and `spaceEvenly` and watch the spacing change live. |
| **2** | **Column + `Expanded`** | A `Column` with a fixed top bar, a fixed bottom bar, and a middle child wrapped in `Expanded` that grows to fill all the leftover vertical space. |
| **3** | **Stack + `Positioned`** | A background `Container` with a notification icon, and a red badge placed in the top-right corner using `Positioned` — the classic overlapping-UI pattern. |
| **4** | **`ListView.builder` (10 items)** | A list of 10 items generated from data (`List.generate`) and built lazily, each shown as a `Card` with a numbered `CircleAvatar`. |
| **5** | **`GridView.count` (2 columns)** | A two-column grid (`crossAxisCount: 2`) of rounded, colored containers with spacing between them. |

---

## Key Concepts

- **`Row` / `Column` alignment:** `mainAxisAlignment` controls spacing along the main axis.
- **`Expanded`:** forces a child to fill the remaining space along the main axis.
- **`Stack` / `Positioned`:** layer widgets and pin one to a precise corner.
- **`ListView.builder`:** efficient, on-demand list building from a data source.
- **`GridView.count`:** a fixed-column grid layout.

---

## Project Structure

```
practical_exercises_demo/
├── lib/
│   └── main.dart     # menu + all five exercise screens
├── pubspec.yaml      # project metadata and dependencies
└── README.md         # this file
```

---

## Running the Demo

You need the [Flutter SDK](https://docs.flutter.dev/get-started/install) installed.

```bash
# from inside the practical_exercises_demo folder
flutter pub get
flutter run
```

Pick a device (Android emulator, iOS simulator, Chrome, or desktop) when prompted,
then tap each menu item to explore the exercise.

### Expected result

- The home menu lists the five exercises.
- **Exercise 1** lets you toggle `mainAxisAlignment` and see the row re-space.
- **Exercise 2** shows the green middle section stretching between fixed bars.
- **Exercise 3** shows a red "3" badge pinned to the corner of the indigo box.
- **Exercise 4** scrolls through 10 numbered cards.
- **Exercise 5** shows a 2-column grid of colored tiles.
