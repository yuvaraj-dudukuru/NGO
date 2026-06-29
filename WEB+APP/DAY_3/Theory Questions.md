# Answers to the Day 3 theory questions.

---

## 1. Full form of CSS and what "cascading" means

**CSS** stands for **Cascading Style Sheets**. It is the language used to control the
presentation (colors, layout, spacing, fonts) of HTML documents.

**"Cascading"** refers to the algorithm the browser uses to decide which style wins when
multiple rules target the same element. Styles "cascade" down and are resolved based on
three factors — **origin/importance**, **specificity**, and **source order** (the last
matching rule of equal weight wins). This cascade lets styles inherit and override each
other predictably.

---

## 2. The three ways to add CSS and why external is preferred

1. **Inline CSS** — a `style` attribute directly on an element:
   `<p style="color: red;">`. Highest priority, but not reusable.
2. **Internal (embedded) CSS** — a `<style>` block inside the `<head>` of the page.
   Affects only that one page.
3. **External CSS** — styles in a separate `.css` file linked with
   `<link rel="stylesheet" href="styles.css">`.

**External CSS is preferred** because it separates content (HTML) from presentation (CSS),
can be reused across many pages, is cached by the browser (faster loads), and is far easier
to maintain — one change updates the whole site.

---

## 3. Parts of the rule `h1 { color: blue; font-size: 2rem; }`

```
h1   {  color: blue ;  font-size: 2rem ;  }
└┬┘     └─┬─┘ └─┬─┘
 │        │     └──── value
 │        └────────── property
 └─ selector
   └──────────────── the two property:value pairs together are the declarations,
                      and everything inside { } is the declaration block.
```

- **Selector** (`h1`) — targets which element(s) the rule applies to.
- **Declaration block** (`{ ... }`) — the curly braces holding the declarations.
- **Declaration** (`color: blue;`) — a single property/value pair ending in a semicolon.
- **Property** (`color`, `font-size`) — the aspect being styled.
- **Value** (`blue`, `2rem`) — what the property is set to.

---

## 4. The CSS box model and default total size

Every element is a rectangular box made of four layers, from inside out:

1. **Content** — the text/image (width × height).
2. **Padding** — space between content and the border.
3. **Border** — the line around the padding.
4. **Margin** — space outside the border, separating it from other elements.

By **default** (`box-sizing: content-box`), the `width`/`height` you set apply to the
**content only**. The browser calculates the element's total rendered size as:

```
total width  = width  + left padding + right padding + left border + right border
total height = height + top padding + bottom padding + top border + bottom border
(margin adds external space but is not part of the box's own size)
```

So a box with `width: 200px; padding: 20px; border: 5px` actually occupies **250px** wide.

---

## 5. What `box-sizing: border-box` changes and why pros use it

`box-sizing: border-box` makes the `width`/`height` include the **content + padding +
border**, instead of content only. The browser shrinks the content area to fit, so the box
stays the size you declared.

With `width: 200px; padding: 20px; border: 5px`, the element is exactly **200px** wide.
Professionals use it (often globally via `* { box-sizing: border-box; }`) because sizing
becomes predictable — adding padding or borders no longer breaks layouts.

---

## 6. Margin vs padding, and margin collapsing

- **Padding** is the space **inside** the element, between its content and its border.
  It is part of the clickable/background area.
- **Margin** is the space **outside** the element, between its border and neighboring
  elements. It is always transparent.

**Margin collapsing**: when two **vertical** margins meet (e.g., the bottom margin of one
block and the top margin of the next), they don't add up — they **collapse** into a single
margin equal to the **larger** of the two. This only happens with vertical margins of
block elements, not horizontal margins and not padding.

---

## 7. `block` vs `inline` vs `inline-block`

| Display | Starts new line? | Respects width/height? | Respects vertical margin/padding? |
|---|---|---|---|
| **block** | Yes (takes full width) | Yes | Yes |
| **inline** | No (flows in text) | No | No (vertical spacing ignored) |
| **inline-block** | No (flows in text) | Yes | Yes |

- **block** — e.g. `<div>`, `<p>`, `<section>`; stacks vertically.
- **inline** — e.g. `<span>`, `<a>`; sits in the text line, sized by its content.
- **inline-block** — flows inline like text **but** accepts width, height, and full
  margins/padding — ideal for buttons or nav items side by side.

---

## 8. The five `position` values with a real-world use

1. **static** (default) — element follows normal document flow; `top/left` etc. have no
   effect. *Use:* ordinary body text and most page content.
2. **relative** — positioned relative to where it would normally sit; offsets nudge it
   without removing it from flow. *Use:* shifting an element slightly, or creating a
   positioning context for an absolutely-positioned child.
3. **absolute** — removed from flow and positioned relative to its nearest *positioned*
   ancestor. *Use:* a dropdown menu, tooltip, or a badge pinned to a card corner.
4. **fixed** — removed from flow and positioned relative to the **viewport**; stays put
   while scrolling. *Use:* a sticky navbar or a "back to top" button.
5. **sticky** — acts relative until a scroll threshold, then "sticks" like fixed.
   *Use:* a section heading or table header that stays visible while scrolling its section.

---

## 9. CSS specificity and the priority order

**Specificity** is the weight the browser assigns to a selector to decide which rule wins
when several target the same element. More specific selectors override less specific ones,
regardless of source order.

Priority order, **lowest to highest**:

1. **Universal selector** (`*`) and inherited styles — lowest.
2. **Element / type selectors** and pseudo-elements (`p`, `h1`, `::before`).
3. **Class, attribute, and pseudo-class selectors** (`.card`, `[type="text"]`, `:hover`).
4. **ID selectors** (`#header`).
5. **Inline styles** (`style="..."`).
6. **`!important`** — overrides everything above (use sparingly).

When specificity is **equal**, the **last** rule in source order wins.

---

## 10. Responsive design; mobile-first vs desktop-first

**Responsive design** is building pages that adapt to any screen size — phones, tablets,
desktops — using flexible widths, fluid layouts (flexbox/grid), relative units, and
**media queries**, so content stays readable and usable everywhere.

- **Mobile-first** — write the base styles for **small screens first**, then use
  `min-width` media queries to **add** complexity for larger screens. Preferred today;
  it produces leaner CSS and prioritizes performance on phones.
- **Desktop-first** — write base styles for **large screens first**, then use `max-width`
  media queries to **scale down** for smaller screens. Easier when designing primarily for
  desktop but tends toward heavier overrides.
