# Mini Project 3 — Contacts App

A two-screen Flutter app: a **divided list of contacts**, and a **details screen**
showing each contact's phone, email, and city. All contacts are sample data.

## Screens
- **Contact List** — contacts separated by dividers (avatar initial, name, phone);
  tap one to open details.
- **Contact Details** — a large avatar, the name, and phone/email/city rows.

## Files
```
3_contacts_app/
├── lib/main.dart      ← both screens + the sample contact data
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
Then tap a contact to see full details; use the back button to return.

## How to stop
Press **q** (or **Ctrl+C**) in the `flutter run` terminal.

## Concepts
`ListView.builder`, `Divider`, `CircleAvatar` initials, `Navigator.push` with
constructor data passing, and reusable helper widgets.
