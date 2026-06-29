# Day 5 — Theory Questions & Answers

## 1. What is ES6 and why was it introduced?

ES6 (ECMAScript 2015) is the sixth major version of the ECMAScript standard, the
specification that JavaScript implements. It was introduced to modernize the language
and fix long-standing pain points: it added block-scoped variables (`let`/`const`),
arrow functions, template literals, destructuring, default/rest/spread parameters,
classes, modules, promises, and more. The goal was to make JavaScript cleaner, more
readable, and better suited to building large, complex applications rather than just
small scripts.

## 2. Difference between `let`, `const`, and `var` (and the Temporal Dead Zone)

- **`var`** is function-scoped, can be redeclared and reassigned, and is *hoisted* and
  initialized to `undefined`, so using it before its declaration returns `undefined`
  instead of an error.
- **`let`** is block-scoped (`{ }`), can be reassigned but not redeclared in the same scope.
- **`const`** is block-scoped and cannot be reassigned after its initial value (though the
  contents of a `const` object or array can still be mutated).

The **Temporal Dead Zone (TDZ)** is the period between entering a scope and the actual
declaration line of a `let`/`const` variable. They are hoisted but *not* initialized, so
accessing them before the declaration throws a `ReferenceError` — unlike `var`, which
would just give `undefined`. This helps catch bugs early.

## 3. Arrow functions and how `this` differs from regular functions

Arrow functions are a shorter syntax for writing functions: `const add = (a, b) => a + b;`.
With a single expression body the result is returned implicitly. The key difference is how
they handle **`this`**: a regular function gets its own `this`, determined by *how it is
called* (the calling object, the global object, or `undefined` in strict mode). An arrow
function does **not** have its own `this` — it *lexically inherits* `this` from the
surrounding scope where it was defined. This makes arrow functions ideal for callbacks
(e.g. inside event handlers or `forEach`) where you want to keep the outer `this`.

## 4. Rest parameters vs. the spread operator

Both use the `...` syntax but do opposite things:

- **Rest parameters** *collect* multiple arguments into a single array, used in a function
  definition: `function sum(...numbers) { ... }` — `numbers` becomes an array of all passed values.
- **Spread operator** *expands* an array or object into individual elements, used when
  calling functions or building new arrays/objects:
  `const combined = [...arr1, ...arr2];` or `Math.max(...numbers);`.

In short: rest **gathers many into one**, spread **expands one into many**.

## 5. Array destructuring and object destructuring (with examples)

Destructuring extracts values from arrays or objects into individual variables.

**Array destructuring** (by position):
```js
const colors = ["red", "green", "blue"];
const [first, second] = colors;
// first = "red", second = "green"
```

**Object destructuring** (by property name):
```js
const student = { name: "Asha", course: "Math" };
const { name, course } = student;
// name = "Asha", course = "Math"
```

## 6. What is the DOM and how does the browser create it?

The **DOM (Document Object Model)** is a live, in-memory representation of a web page,
structured as a tree of objects (nodes). When the browser loads an HTML document, it
*parses* the HTML text top to bottom and builds this tree — each element, attribute, and
piece of text becomes a node connected in a parent/child hierarchy. JavaScript can then
read and change this tree (add, remove, or modify nodes), and the browser instantly
re-renders the page to reflect those changes. The DOM is what lets pages be dynamic and
interactive rather than static.

## 7. `textContent` vs. `innerText` vs. `innerHTML` (and the security concern)

- **`textContent`** gets/sets the raw text of an element, including hidden elements and
  ignoring CSS styling. It is fast and safe — anything set is treated as plain text.
- **`innerText`** gets/sets the *visible* text only; it respects CSS (e.g. won't return
  `display:none` text) and is aware of rendering, which makes it slower.
- **`innerHTML`** gets/sets the full HTML markup inside an element, parsing any tags into
  real DOM elements.

The **security concern** is with `innerHTML`: inserting untrusted user input through it can
execute malicious HTML/scripts, a vulnerability called **XSS (Cross-Site Scripting)**.
For plain text, prefer `textContent`; only use `innerHTML` with content you control or
have sanitized.

## 8. `getElementById` vs. `querySelector`

- **`getElementById("id")`** selects a single element by its `id` attribute only. It is
  very fast and returns the element or `null`.
- **`querySelector("selector")`** accepts any **CSS selector** (id `#`, class `.`, tag,
  attribute, descendant combinations, etc.) and returns the **first** matching element, or
  `null`. It is more flexible but slightly slower.

Use `getElementById` when selecting by id; use `querySelector` for more complex or
class/tag-based selections (and `querySelectorAll` to get *all* matches as a NodeList).

## 9. Why `addEventListener` is preferred over the `onclick` attribute

- **Multiple handlers:** `addEventListener` can attach *many* listeners for the same event
  on one element; an `onclick` property/attribute only holds **one** handler — a second
  assignment overwrites the first.
- **Separation of concerns:** it keeps JavaScript out of the HTML, so behavior and markup
  stay cleanly separated.
- **More control:** it supports options like capturing vs. bubbling phase, `{ once: true }`,
  and easy removal via `removeEventListener`.

For these reasons `addEventListener` is the professional, flexible standard.

## 10. What `event.preventDefault()` does and when you need it

`event.preventDefault()` stops the browser's **default action** for an event from
happening. Many elements have built-in default behaviors — a form *submits and reloads the
page*, a link *navigates to its URL*, a checkbox *toggles*. Calling `preventDefault()`
inside the event handler cancels that default so you can handle the event with JavaScript
instead. The most common case is form submission: you call it to prevent the page reload so
you can validate and process the input yourself (as in the Student Dashboard project).
