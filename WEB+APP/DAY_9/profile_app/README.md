# profile_app — Day 9 Practical Lab

My first Flutter app, built end-to-end during the **Day 9 Practical Lab**:
verify the toolchain, create a project, run it, hot reload, build the
**Student Profile UI**, and customize it.

> **Note:** Flutter was **not** installed on this machine when the folder was
> created, so `lib/main.dart` and `pubspec.yaml` were written by hand. To get a
> fully runnable project (with `android/`, `ios/`, `web/` platform folders),
> install the Flutter SDK and run `flutter create .` inside this folder once —
> it keeps the existing `lib/main.dart`.

## The Lab — Step by Step

### Step 1: Verify Flutter installation
```bash
flutter --version
flutter doctor
flutter doctor --android-licenses   # if licenses are unaccepted
```
Resolve any critical issues the doctor reports before continuing.

### Step 2: Start an emulator
1. Open Android Studio → **Device Manager**.
2. Launch an emulator (or connect a physical phone with USB debugging on).
3. Confirm it's detected:
```bash
flutter devices
```

### Step 3: Create the project
```bash
flutter create profile_app
cd profile_app
code .
```

### Step 4: Run the starter app
```bash
flutter run
```
The default counter app appears. Tap **+** and watch the counter increase —
this confirms your environment works.

### Step 5: Try hot reload
1. With the app running, open `lib/main.dart`.
2. Change the app bar title text (e.g. to `'My First App'`).
3. Save (`Ctrl+S`).

The title updates almost instantly **without restarting**, and the counter
keeps its value. (In the terminal, `r` = hot reload, `R` = hot restart.)

### Step 6: Build the Student Profile UI
Replace `lib/main.dart` with the complete Student Profile App (already done in
this folder) and save. Hot reload shows the app bar plus the Profile, About,
Skills, and Contact sections.

### Step 7: Experiment and inspect
1. Change a color (e.g. the AppBar's `backgroundColor` to `Colors.green`) and save.
2. Change the name and details to your own.
3. Add a new skill row (copy a `Row(...)` block in the Skills section).
4. Open the **Flutter Inspector** in VS Code and explore the widget tree.

## Project Structure
```
profile_app/
├── lib/
│   └── main.dart     # the Student Profile app
├── pubspec.yaml      # project metadata & dependencies
└── README.md
```

## Skills Exercised
Setup & `flutter doctor` · project creation · running on an emulator · hot
reload / hot restart · building UI with widgets (`Scaffold`, `AppBar`,
`Column`, `Row`, `Text`, `Icon`, `CircleAvatar`, `SizedBox`) · inspecting the
widget tree.

## Keep It
This is a real portfolio piece — consider committing it to GitHub (Day 7) and
re-running the lab until the create → run → build → hot reload workflow feels
natural.
