// Select DOM elements
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');

// Arrow function to handle adding a new task
const addTask = () => {
    // ES6: const instead of var
    const taskText = taskInput.value.trim(); 

    if (taskText === '') return alert('Please enter a task!');

    // Create a new list item (DOM manipulation)
    const li = document.createElement('li');

    // ES6: Template literals (backticks) for cleaner string interpolation
    li.innerHTML = `
        <span>${taskText}</span>
        <div class="actions">
            <button class="btn-complete">✓</button>
            <button class="btn-delete">🗑️</button>
        </div>
    `;

    // DOM Manipulation: Event Listener for completing task
    const completeBtn = li.querySelector('.btn-complete');
    completeBtn.addEventListener('click', () => {
        li.classList.toggle('completed');
    });

    // DOM Manipulation: Event Listener for deleting task
    const deleteBtn = li.querySelector('.btn-delete');
    deleteBtn.addEventListener('click', () => {
        // Removing the element from the DOM
        li.remove();
    });

    // Append the newly created task to the list
    taskList.appendChild(li);

    // Clear the input field
    taskInput.value = '';
    taskInput.focus();
};

// Event listener for adding task via button click
addTaskBtn.addEventListener('click', addTask);

// Event listener for adding task via 'Enter' key
taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addTask();
    }
});
