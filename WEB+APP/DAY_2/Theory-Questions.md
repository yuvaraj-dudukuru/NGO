# Theory Questions — Answers

### 1. Explain the full form of HTML and what each word means.
HTML stands for **HyperText Markup Language**. *HyperText* means text that can link
to other documents or resources through hyperlinks. *Markup* means it uses tags to
label and structure content (headings, paragraphs, lists, etc.). *Language* means it
follows a defined set of rules and syntax that browsers understand.

### 2. Why is HTML called a markup language and not a programming language?
HTML only **describes the structure and meaning** of content — it marks up text so the
browser knows what is a heading, a paragraph, or a link. It has no logic: it cannot make
decisions, perform calculations, loop, or store and process data the way a programming
language (such as JavaScript or Python) can. Because it lays out content rather than
computing anything, it is a markup language.

### 3. Describe the difference between the `<head>` and `<body>` sections.
The `<head>` contains **metadata** — information *about* the page that is not shown in the
main window, such as the `<title>`, character set, viewport settings, and links to CSS.
The `<body>` contains the **visible content** the user actually sees and interacts with:
text, images, links, forms, and so on.

### 4. Explain the difference between a tag, an element, and an attribute, with an example.
- **Tag** — the keyword in angle brackets that marks the start or end of something, e.g.
  `<p>` (opening) and `</p>` (closing).
- **Element** — the complete unit: the opening tag, the content, and the closing tag
  together, e.g. `<p>Hello world</p>`.
- **Attribute** — extra information placed inside the opening tag as a name/value pair,
  e.g. the `href` in `<a href="https://example.com">Link</a>`.

### 5. What is the difference between `id` and `class`? When would you use each?
An **`id` is unique** — it should appear only once per page and is used to identify a
single specific element (e.g. `#main-header`, or as an anchor target for navigation). A
**`class` is reusable** — many elements can share the same class so they can be styled or
selected as a group (e.g. `.button`). Use `id` for one-of-a-kind elements; use `class`
when you want to apply the same styling or behaviour to multiple elements.

### 6. Why are the `alt` attribute and the `<label>` element important for accessibility?
The **`alt`** attribute gives a text description of an image, so screen-reader users hear
what the image shows and the text appears if the image fails to load. The **`<label>`**
element ties a description to a form field, so screen readers announce what each input is
for and clicking the label focuses the field (a larger, easier target). Both make the page
usable for people who rely on assistive technology.

### 7. Explain the difference between `<strong>` / `<em>` and `<b>` / `<i>`.
`<strong>` and `<em>` are **semantic** — they convey *meaning*: `<strong>` marks strong
importance and `<em>` marks emphasis that changes how a sentence is read, and screen
readers can announce this. `<b>` and `<i>` are **purely visual** — they make text bold or
italic for style only, carrying no extra importance or meaning. Use `strong`/`em` when the
meaning matters; use `b`/`i` only for appearance.

### 8. What is semantic HTML and why does it matter for SEO and accessibility?
Semantic HTML uses tags that **describe the meaning** of content — like `<header>`,
`<nav>`, `<main>`, `<article>`, and `<footer>` — instead of generic `<div>`s. For
**SEO**, search engines understand the page structure better and can index and rank
content more accurately. For **accessibility**, assistive technologies can navigate the
page by its landmarks and announce content correctly to users.

### 9. Explain the security risk of `target="_blank"` and how to prevent it.
A link with `target="_blank"` opens a new tab, and the new page can gain partial access to
the original page through the `window.opener` reference — it could redirect your original
tab to a malicious site (a "tabnabbing" attack). **Prevent it** by adding
`rel="noopener noreferrer"` to the link, which cuts the `opener` link (and stops the
referrer being sent). Example: `<a href="..." target="_blank" rel="noopener noreferrer">`.

### 10. List four qualities of professional, industry-standard HTML.
1. **Valid and well-formed** — passes the W3C validator, with properly nested and closed tags.
2. **Semantic** — uses meaningful elements rather than `<div>`s for everything.
3. **Accessible** — includes `alt` text, `<label>`s, and proper heading order.
4. **Clean and consistent** — readable, indented, well-commented, and separated from
   styling (CSS) and behaviour (JavaScript).
