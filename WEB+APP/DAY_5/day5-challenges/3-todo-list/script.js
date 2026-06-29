// Challenge 3: To-Do List
const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");

// Add a task as a new <li> element
function addTask() {
    const text = taskInput.value.trim();
    if (text === "") return;   // ignore empty input

    const li = document.createElement("li");
    li.textContent = text;
    taskList.appendChild(li);

    taskInput.value = "";
    taskInput.focus();
}

addBtn.addEventListener("click", addTask);

// Allow pressing Enter to add a task
taskInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") addTask();
});

// Event delegation: one listener on the list removes any clicked task
taskList.addEventListener("click", (event) => {
    if (event.target.tagName === "LI") {
        event.target.remove();
    }
});
