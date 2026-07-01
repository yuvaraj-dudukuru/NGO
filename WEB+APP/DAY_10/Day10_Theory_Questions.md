# Day 10 — Theory Questions & Answers

UI Components and Navigation in Flutter

---

### 1. Explain what a user interface is and how Flutter builds it.

A **user interface (UI)** is everything the user sees and interacts with on screen —
text, buttons, images, lists, and the layout that arranges them. Flutter builds its
UI entirely out of **widgets**: small, composable building blocks that describe what
the UI should look like for a given state. You nest widgets inside one another to form
a **widget tree**, and Flutter renders that tree to the screen, rebuilding the parts
that change when the state updates.

---

### 2. Explain widget composition and why it matters.

**Composition** means building complex UI by combining many small, single-purpose
widgets rather than using a few large, configurable ones. For example, a button with
an icon and label is just an `Icon` and a `Text` placed inside a `Row` inside a button.
It matters because it keeps code **reusable, readable, and DRY** — you can extract a
piece of UI (like a navigation button) into a helper widget and reuse it everywhere,
avoiding repetition and making changes in one place.

---

### 3. Explain the difference between Row and Column, including their axes.

`Row` arranges its children **horizontally** (left to right), while `Column` arranges
them **vertically** (top to bottom). For a `Row`, the **main axis is horizontal** and
the **cross axis is vertical**; for a `Column`, the **main axis is vertical** and the
**cross axis is horizontal**. You control positioning along the main axis with
`mainAxisAlignment` and along the cross axis with `crossAxisAlignment`.

---

### 4. Explain Expanded and Flexible and what they do.

Both are used inside a `Row` or `Column` to control how a child shares the available
space along the main axis. **`Expanded`** forces its child to fill **all** the
remaining space (you can split space using the `flex` factor). **`Flexible`** lets its
child take **up to** the available space but only as much as it needs, so it won't
necessarily fill everything. In short: `Expanded` is `Flexible` with
`fit: FlexFit.tight`.

---

### 5. Explain the Stack widget and when to use it.

A **`Stack`** layers its children **on top of one another**, like sheets of paper,
instead of placing them side by side. Children are drawn in order (later ones on top),
and you can position them precisely with `Positioned` or `Align`. Use it when you need
**overlapping UI** — for example, text or a badge on top of an image, a floating button
over content, or a gradient overlay on a photo.

---

### 6. Explain the difference between ListView and ListView.builder.

A plain **`ListView`** takes a fixed `children` list and builds **all** items at once,
which is fine for short, known lists. **`ListView.builder`** builds items **lazily and
on demand** using an `itemBuilder` callback, creating only the items currently visible
(plus a small buffer). This makes it far more **efficient for long or dynamic lists**,
since off-screen items aren't built until they're scrolled into view.

---

### 7. Explain the navigation stack with push and pop.

Flutter manages screens as a **stack** (like a stack of cards). **`Navigator.push`**
adds a new screen on top of the stack, making it the visible screen, while the previous
one stays underneath. **`Navigator.pop`** removes the top screen, revealing the one
below it — which is exactly what the automatic **back button** does. This
**last-in-first-out** model is how mobile apps move forward and back through screens.

---

### 8. Explain how to pass data between screens.

To send data **forward** to a new screen, you pass it through that screen's
**constructor** when you push it, e.g.
`Navigator.push(context, MaterialPageRoute(builder: (context) => DetailsScreen(name: item)))`,
and the receiving screen stores it in a `final` field. To send data **back** to the
previous screen, you pass a value to `Navigator.pop(context, result)`, and the original
screen receives it by awaiting the `push` call.

---

### 9. Explain named routes and their advantages.

**Named routes** let you register screens with string names (e.g. `'/students'`) in
`MaterialApp`'s `routes` map, then navigate with
`Navigator.pushNamed(context, '/students')` instead of constructing a
`MaterialPageRoute` each time. Their advantages are **centralized, organized
navigation** (all routes defined in one place), **less repeated code**, and easier
maintenance as the app grows. (For passing complex data, direct `push` with a
constructor is often still clearer.)

---

### 10. Explain how today's concepts relate to web development (Flexbox, the box model, the DOM).

Flutter's layout ideas map closely onto the web. **`Row`/`Column` with their main and
cross axes work like CSS Flexbox** (`flex-direction: row/column`), and `Expanded`/
`Flexible` behave like the `flex-grow`/`flex` properties. **`Padding`, `Container`
margins, and `EdgeInsets` mirror the CSS box model** (content, padding, border,
margin). And the **widget tree is like the DOM** — a nested tree of elements that
describes and renders the UI. So the structural thinking transfers directly between
Flutter and the web.
