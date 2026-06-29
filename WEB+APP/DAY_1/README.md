# index.html — My First Web Page

This is a beginner HTML5 web page created on Day 1 of Web and Mobile App Development.

## What it does

When opened in a browser, the page displays:

- A main heading: **Hello World**
- Two paragraphs of introductory text about learning web development

## File structure

| Part | Purpose |
|------|---------|
| `<!DOCTYPE html>` | Declares the document as modern HTML5 |
| `<html lang="en">` | Root element; `lang="en"` sets the language to English |
| `<head>` | Contains information *about* the page (not shown in the page body) |
| `<meta charset="UTF-8">` | Sets character encoding so text displays correctly |
| `<title>` | Sets the text shown in the browser tab ("My First Web Page") |
| `<body>` | Holds everything the user actually sees |
| `<h1>` | The largest heading on the page |
| `<p>` | A paragraph of text |

## Full code

```html
<!DOCTYPE html>
<!-- Declares this as a modern HTML5 document -->
<html lang="en">
<head>
<!-- Information about the page (not visible in the page body) -->
<meta charset="UTF-8">
<title>My First Web Page</title>
</head>
<body>
<!-- Everything the user sees goes inside the body -->
<h1>Hello World</h1>
<p>This is my very first web page.</p>
<p>I am learning Web and Mobile App Development.</p>
</body>
</html>
```

## How to run it

1. Locate `index.html` in this folder.
2. Double-click the file, or right-click → **Open with** → your web browser.
3. The page opens with no internet connection required — it runs entirely on your computer.

## Key takeaways

- HTML uses **tags** (like `<h1>` and `<p>`) to structure content.
- Most tags come in pairs: an opening tag `<p>` and a closing tag `</p>`.
- Comments (`<!-- ... -->`) are notes for developers and are not shown on the page.
- The `<head>` holds page settings; the `<body>` holds visible content.
