// Challenge 5: Form Validator
const form = document.getElementById("signupForm");
const nameField = document.getElementById("nameField");
const emailField = document.getElementById("emailField");
const passwordField = document.getElementById("passwordField");
const formMessage = document.getElementById("formMessage");

form.addEventListener("submit", (event) => {
    event.preventDefault();   // stop the page from reloading

    const name = nameField.value.trim();
    const email = emailField.value.trim();
    const password = passwordField.value.trim();

    // Validate: all fields must be filled
    if (name === "" || email === "" || password === "") {
        formMessage.textContent = "Error: please fill in all fields.";
        formMessage.className = "message error";
        return;
    }

    // Success
    formMessage.textContent = `Success! Welcome, ${name}.`;
    formMessage.className = "message success";
    form.reset();
});
