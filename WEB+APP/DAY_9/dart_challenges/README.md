# Day 9 — Dart Challenges

Five small standalone Dart programs covering core language basics. All use
**demo / placeholder data only** — no personal information.

## The Challenges

| # | File | What it shows |
|---|------|---------------|
| 1 | [`challenge1_variable_types.dart`](challenge1_variable_types.dart) | Declaring `String`, `int`, `double`, `bool` and printing them. |
| 2 | [`challenge2_arithmetic.dart`](challenge2_arithmetic.dart) | All arithmetic operators including `~/` (integer division). |
| 3 | [`challenge3_interpolation.dart`](challenge3_interpolation.dart) | String interpolation (`$var` and `${expr}`). |
| 4 | [`challenge4_even_odd.dart`](challenge4_even_odd.dart) | Ternary operator with `%` to test even/odd. |
| 5 | [`challenge5_list_and_map.dart`](challenge5_list_and_map.dart) | A `List` of skills and a `Map` of contact info, printed. |

## How to Run

Each file is independent. With the Dart (or Flutter) SDK installed:

```bash
dart run challenge1_variable_types.dart
dart run challenge2_arithmetic.dart
dart run challenge3_interpolation.dart
dart run challenge4_even_odd.dart
dart run challenge5_list_and_map.dart
```

No SDK handy? Paste any file into [dartpad.dev](https://dartpad.dev) and press
**Run**.

## Expected Output (summary)

- **1:** the four typed variables, each labelled with its type.
- **2:** `17 + 5 = 22`, `17 / 5 = 3.4`, `17 ~/ 5 = 3`, `17 % 5 = 2`, etc.
- **3:** `Demo User is a year-1 student learning Flutter.`
- **4:** `7 is odd.`
- **5:** the skills list and contact map printed line by line.
