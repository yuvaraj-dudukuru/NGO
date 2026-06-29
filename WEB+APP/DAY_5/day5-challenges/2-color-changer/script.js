// Challenge 2: Color Changer
const redBtn = document.getElementById("redBtn");
const greenBtn = document.getElementById("greenBtn");
const blueBtn = document.getElementById("blueBtn");
const resetBtn = document.getElementById("resetBtn");

// Each button sets the body's background color via the style property
redBtn.addEventListener("click", () => {
    document.body.style.backgroundColor = "#fecaca";
});

greenBtn.addEventListener("click", () => {
    document.body.style.backgroundColor = "#bbf7d0";
});

blueBtn.addEventListener("click", () => {
    document.body.style.backgroundColor = "#bfdbfe";
});

resetBtn.addEventListener("click", () => {
    document.body.style.backgroundColor = "";
});
