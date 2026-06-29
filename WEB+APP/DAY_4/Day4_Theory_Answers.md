# Day 4 — JavaScript Basics: Theory Answers

## 1. What is JavaScript, and how does it differ from HTML and CSS?
JavaScript is a programming language that adds **behavior and interactivity** to web pages — it can make decisions, perform calculations, respond to clicks, and change page content while it runs. HTML provides the **structure/content** (headings, paragraphs, buttons), and CSS provides the **styling/presentation** (colors, layout, fonts). In short: HTML is *what's there*, CSS is *how it looks*, and JavaScript is *what it does*.

## 2. Difference between `var`, `let`, and `const` (scope and reassignment)
- **`var`** is *function-scoped* and is hoisted; it can be reassigned and redeclared. It's older and avoided in modern code because its scoping is error-prone.
- **`let`** is *block-scoped* (limited to the `{ }` it's declared in) and **can be reassigned** but not redeclared in the same scope.
- **`const`** is also *block-scoped* but **cannot be reassigned** after its initial value (though the contents of a `const` object or array can still be changed).
Use `const` by default, `let` when you need to reassign, and avoid `var`.

## 3. The seven primitive data types (with examples)
1. **String** — `"Priya"`
2. **Number** — `20` (also `3.14`)
3. **Boolean** — `true` / `false`
4. **Undefined** — `let x;` (declared but no value)
5. **Null** — `let y = null;` (intentional "no value")
6. **BigInt** — `9007199254740993n` (very large integers)
7. **Symbol** — `Symbol("id")` (a unique identifier)

## 4. Difference between `null` and `undefined`
**`undefined`** means a variable has been declared but no value has been assigned yet — it's the default "empty" state the JavaScript engine gives. **`null`** is an *intentional* assignment by the programmer to say "this has no value on purpose." So `undefined` usually happens automatically, while `null` is set deliberately.

## 5. Difference between `==` and `===` (and which to use)
**`==`** is the *loose* equality operator — it compares values **after converting types**, so `5 == "5"` is `true`. **`===`** is the *strict* equality operator — it compares **both value and type** with no conversion, so `5 === "5"` is `false`. Always prefer **`===`** because it avoids surprising type-coercion bugs.

## 6. What does `prompt()` return, and why convert it?
`prompt()` **always returns a string** (or `null` if the user cancels). So even if the user types `6`, you get the text `"6"`, not the number `6`. You must convert it (e.g. with `Number()`) before doing math — otherwise `"6" + "4"` gives `"64"` (string concatenation) instead of `10`.

## 7. Difference between implicit and explicit type conversion
**Implicit conversion (coercion)** is done *automatically* by JavaScript, e.g. `"5" * 2` becomes `10` because the string is silently turned into a number. **Explicit conversion** is done *deliberately* by the programmer using functions like `Number()`, `String()`, or `Boolean()`, e.g. `Number("5")`. Explicit conversion is safer because the intent is clear and predictable.

## 8. What are template literals, and why preferred over concatenation?
Template literals are strings written with **backticks** (`` ` ``) that allow embedded expressions using `${ }`, e.g. `` `Hello, ${name}!` ``. They're preferred over concatenation (`"Hello, " + name + "!"`) because they're **easier to read**, avoid messy `+` signs and spacing mistakes, and support **multi-line strings** directly.

## 9. Difference between an object and an array (and when to use each)
An **array** is an *ordered list* of values accessed by numeric index (`skills[0]`); use it for collections of similar items where order matters, like a list of names. An **object** is a collection of **key–value pairs** accessed by named properties (`student.name`); use it to model a single thing with named attributes, like a student's name, age, and grade.

## 10. The three types of errors and how to debug each
1. **Syntax errors** — broken code structure (missing quote, bracket, or semicolon). The code won't run at all; read the console's error message and line number to find and fix it.
2. **Runtime errors** — the code runs but crashes during execution (e.g. calling a function that doesn't exist). Read the console error/stack trace to locate the failing line.
3. **Logic errors** — the code runs without crashing but produces the *wrong result*. These are hardest; debug by using `console.log()` to inspect values step by step, or set breakpoints to trace the logic.
