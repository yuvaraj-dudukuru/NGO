/* ============================================
   DYNAMIC STUDENT DASHBOARD - script.js
   Day 5: ES6 + DOM Manipulation Project
   ============================================ */

// ===== Element selections =====
const form = document.getElementById("studentForm");
const nameInput = document.getElementById("nameInput");
const courseInput = document.getElementById("courseInput");
const studentList = document.getElementById("studentList");
const countSpan = document.getElementById("count");
const formMessage = document.getElementById("formMessage");

// ===== Data =====
let students = [];

// ===== Render the list from the data =====
function renderStudents() {
    studentList.innerHTML = "";

    if (students.length === 0) {
        studentList.innerHTML = "<p>No students yet. Add one above.</p>";
    }

    students.forEach((student, index) => {
        const card = document.createElement("div");
        card.classList.add("student-card");
        card.innerHTML = `
            <div>
                <strong>${student.name}</strong><br>
                <span>${student.course}</span>
            </div>
            <button class="delete-btn" data-index="${index}">Delete</button>
        `;
        studentList.appendChild(card);
    });

    countSpan.textContent = students.length;
}

// ===== Add a student on form submit =====
form.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = nameInput.value.trim();
    const course = courseInput.value.trim();

    if (name === "" || course === "") {
        formMessage.textContent = "Please fill in both fields.";
        return;
    }

    students.push({ name, course });
    formMessage.textContent = "";
    nameInput.value = "";
    courseInput.value = "";
    renderStudents();
});

// ===== Delete a student (event delegation) =====
studentList.addEventListener("click", (event) => {
    if (event.target.classList.contains("delete-btn")) {
        const index = Number(event.target.getAttribute("data-index"));
        students.splice(index, 1);
        renderStudents();
    }
});

// ===== Initial render =====
renderStudents();
