// ===== Step 2: Select Elements =====
const title = document.getElementById("title");
const message = document.getElementById("message");
const userInput = document.getElementById("userInput");
const updateBtn = document.getElementById("updateBtn");
const addBtn = document.getElementById("addBtn");
const itemList = document.getElementById("itemList");

console.log("Title element:", title);   // confirm it found the element

// ===== Step 3: Modify Content =====
title.textContent = "DOM Lab (Updated)";
title.classList.add("highlight");

// ===== Step 4: Handle a Click Event to Update Content =====
updateBtn.addEventListener("click", () => {
    const text = userInput.value.trim();
    if (text === "") {
        message.textContent = "Please type something first.";
    } else {
        message.textContent = `You said: ${text}`;
    }
});

// ===== Step 5: Create Elements Dynamically =====
addBtn.addEventListener("click", () => {
    const text = userInput.value.trim();
    if (text === "") return;   // do nothing if empty

    // Create a new list item
    const li = document.createElement("li");
    li.textContent = text;

    // Add it to the list
    itemList.appendChild(li);

    // Clear the input
    userInput.value = "";
});

// ===== Step 6: Handle Events on Dynamic Elements (Delete on Click) =====
// Event delegation: one listener handles clicks on any list item
itemList.addEventListener("click", (event) => {
    if (event.target.tagName === "LI") {
        event.target.remove();   // remove the clicked item
    }
});
