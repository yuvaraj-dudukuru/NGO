# Day 9 — Theory Questions & Answers

*Basics of Flutter and Dart*

---

## 1. What is Flutter and why do companies use it?

Flutter is Google's open-source UI toolkit for building applications from a
**single codebase** that run on mobile (Android/iOS), web, and desktop.
Companies use it because one codebase means lower cost and faster delivery than
maintaining separate native apps, it produces fast **native-compiled**
performance, and its **hot reload** makes the develop-and-iterate cycle very
quick.

---

## 2. Flutter's three architectural layers

- **Framework (Dart):** the layer you write against — widgets, rendering,
  animation, gestures, and the Material/Cupertino libraries.
- **Engine (C/C++):** the low-level core that handles rendering (via
  Skia/Impeller), text layout, and the Dart runtime; it paints what the
  framework describes.
- **Embedder (platform-specific):** the OS-level glue that hosts the engine on
  each platform, managing the window/surface, input events, and the app
  lifecycle.

---

## 3. What is Dart and how does it relate to Flutter?

Dart is the programming language Flutter apps are written in — a typed,
object-oriented language by Google. It pairs well with Flutter because it
supports **JIT** compilation in development (enabling hot reload) and **AOT**
compilation to fast native code for release builds. Every widget, screen, and
piece of logic in a Flutter app is written in Dart.

---

## 4. StatelessWidget vs StatefulWidget

A **StatelessWidget** is immutable — it has no internal state that changes, so
it's used for fixed UI like a profile screen or a label. A **StatefulWidget**
holds mutable state and can rebuild itself when that state changes by calling
`setState()`, so it's used for interactive UI like a counter, form, or toggle.

---

## 5. What is a widget, and what does "everything is a widget" mean?

A widget is the basic building block of a Flutter UI — a description of part of
the interface (a button, text, padding, or even layout/structure). **"Everything
is a widget"** means not just visible elements but also layout, spacing,
alignment, and even the app itself are all widgets, composed together in a
**tree** to build the whole UI.

---

## 6. The build method and what it returns

`build(BuildContext context)` is the method that describes a widget's UI.
Flutter calls it to render the widget and again whenever the widget needs to
update. It **returns a Widget** (usually a tree of nested widgets) that Flutter
then renders to the screen.

---

## 7. What does a Scaffold provide?

`Scaffold` provides the basic visual structure of a Material Design screen —
pre-built slots for common elements like an `appBar` (top bar), `body` (main
content), `floatingActionButton`, `drawer`, and `bottomNavigationBar` — so you
don't have to lay out a standard screen from scratch.

---

## 8. Hot reload vs hot restart vs full restart

- **Hot reload** injects changed code into the running app and rebuilds the
  widget tree — near-instant and **keeps the current state** (e.g., the counter
  value stays). Best for UI tweaks.
- **Hot restart** restarts the app and rebuilds from scratch — **state is
  reset** to initial values, but it's still faster than a full rebuild. Needed
  for changes hot reload can't apply (like changing `main()` or global/state
  initialization).
- **Full restart** stops and recompiles the whole app from zero — the slowest;
  needed for things like adding native dependencies or changing `pubspec.yaml`.

---

## 9. Dart `var` / `final` / `const` vs JavaScript

- **`var`** infers a type that is then fixed (the value can change but the type
  can't), similar to JS `let` but type-locked.
- **`final`** is a single-assignment variable set at runtime — like JS `const`
  for a reference (can't be reassigned, but the object's contents can change).
- **`const`** is a true **compile-time** constant — fully fixed and known at
  compile time, stronger than JS `const`.

*(Dart's `var` ≈ JS `let`; Dart has no direct equivalent of JS `var`'s
function-scoping/hoisting.)*

---

## 10. The Flutter app lifecycle (high level)

The app starts at `main()`, which calls `runApp()` with a root widget. Flutter
builds the widget tree by calling each widget's `build` method and renders it to
the screen. As the user interacts, state changes trigger rebuilds of affected
widgets. At the app level, the OS moves the app through lifecycle states —
**resumed** (visible/active), **inactive**, **paused** (backgrounded), and
**detached** — which you can respond to (e.g., to save data) via an app
lifecycle observer.
