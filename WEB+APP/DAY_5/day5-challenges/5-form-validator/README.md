# Challenge 5 — Form Validator

A sign-up form that validates its fields on submit and shows a success or error
message — without reloading the page.

## Files
- `index.html` — name, email, and password fields plus a submit button and a message area.
- `styles.css` — styling, including `.message.error` and `.message.success` states.
- `script.js` — the `submit` handler that validates and reports.

## How it works
On submit the handler calls `event.preventDefault()` to stop the default page
reload, trims all three fields, and checks that none are empty. If any field is
blank it shows a red error message; otherwise it shows a green success message
and resets the form.

## How to run
Open `index.html` in a browser (double-click or **Live Server**). Submit with
blank fields to see the error, then fill them in to see the success message.

## How to stop
Close the browser tab.

## Concept
`event.preventDefault()`, form validation, and swapping CSS classes to style
feedback messages.
