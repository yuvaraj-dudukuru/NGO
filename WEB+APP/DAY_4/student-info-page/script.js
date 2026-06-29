/* ============================================
   STUDENT INFORMATION PAGE - script.js
   Day 4: JavaScript Basics Project
   ============================================ */

// ----- Function 1: Enter the student's name ----
function enterName() {
    let name = prompt("Please enter your name:");
    if (name && name.trim() !== "") {
        document.getElementById("studentName").textContent = name.trim();
        alert(`Welcome, ${name.trim()}!`);
    } else {
        alert("You did not enter a valid name.");
    }
}

// ----- Function 2: Calculate average marks ----
function calculateAverage() {
    let mark1 = Number(prompt("Enter marks for subject 1:"));
    let mark2 = Number(prompt("Enter marks for subject 2:"));
    let mark3 = Number(prompt("Enter marks for subject 3:"));

    if (isNaN(mark1) || isNaN(mark2) || isNaN(mark3)) {
        document.getElementById("result").textContent =
            "Please enter valid numbers for all subjects.";
        return;
    }

    let total = mark1 + mark2 + mark3;
    let average = total / 3;
    let status = average >= 40 ? "Pass" : "Fail";

    document.getElementById("result").textContent =
        `Total: ${total}, Average: ${average.toFixed(2)}, Status: ${status}`;
}

// ----- Function 3: Change the page title ----
function changeTitle() {
    let title = document.getElementById("pageTitle");
    if (title.textContent === "Student Information") {
        title.textContent = "Welcome to Day 4!";
    } else {
        title.textContent = "Student Information";
    }
}
