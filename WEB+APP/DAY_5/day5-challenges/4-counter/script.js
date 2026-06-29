// Challenge 4: Counter
const countDisplay = document.getElementById("count");
const incBtn = document.getElementById("incBtn");
const decBtn = document.getElementById("decBtn");
const resetBtn = document.getElementById("resetBtn");

// "let" because the value changes over time
let count = 0;

function render() {
    countDisplay.textContent = count;
}

incBtn.addEventListener("click", () => {
    count++;
    render();
});

decBtn.addEventListener("click", () => {
    count--;
    render();
});

resetBtn.addEventListener("click", () => {
    count = 0;
    render();
});
