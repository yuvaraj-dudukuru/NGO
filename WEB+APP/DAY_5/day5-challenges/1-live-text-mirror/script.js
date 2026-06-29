// Challenge 1: Live Text Mirror
const mirrorInput = document.getElementById("mirrorInput");
const mirrorOutput = document.getElementById("mirrorOutput");

// The "input" event fires on every keystroke / change
mirrorInput.addEventListener("input", () => {
    const text = mirrorInput.value;
    // Show typed text live; fall back to a placeholder when empty
    mirrorOutput.textContent = text === "" ? "Your text will appear here." : text;
});
