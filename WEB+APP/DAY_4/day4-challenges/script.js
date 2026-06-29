/* ============================================
   DAY 4 CODING CHALLENGES - script.js
   ============================================ */

// Helper: show a message in the result area
function showResult(message) {
    document.getElementById("result").textContent = message;
}

// ----- Challenge 1: Temperature Converter -----
function temperatureConverter() {
    let celsius = Number(prompt("Enter temperature in Celsius:"));

    if (isNaN(celsius)) {
        showResult("Please enter a valid number.");
        return;
    }

    let fahrenheit = celsius * 9 / 5 + 32;
    showResult(`${celsius}°C = ${fahrenheit}°F`);
}

// ----- Challenge 2: Even or Odd -----
function evenOrOdd() {
    let number = Number(prompt("Enter a number:"));

    if (isNaN(number)) {
        alert("Please enter a valid number.");
        showResult("Invalid input for Even/Odd.");
        return;
    }

    let result = number % 2 === 0 ? "even" : "odd";
    alert(`${number} is ${result}.`);
    showResult(`${number} is ${result}.`);
}

// ----- Challenge 3: Simple Calculator -----
function simpleCalculator() {
    let num1 = Number(prompt("Enter the first number:"));
    let num2 = Number(prompt("Enter the second number:"));
    let operation = prompt("Enter an operation (+, -, *, /):");

    if (isNaN(num1) || isNaN(num2)) {
        showResult("Please enter valid numbers.");
        return;
    }

    let answer;
    switch (operation) {
        case "+":
            answer = num1 + num2;
            break;
        case "-":
            answer = num1 - num2;
            break;
        case "*":
            answer = num1 * num2;
            break;
        case "/":
            if (num2 === 0) {
                showResult("Cannot divide by zero.");
                return;
            }
            answer = num1 / num2;
            break;
        default:
            showResult("Invalid operation. Use +, -, *, or /.");
            return;
    }

    showResult(`${num1} ${operation} ${num2} = ${answer}`);
}

// ----- Challenge 4: Grade Calculator -----
function gradeCalculator() {
    let mark1 = Number(prompt("Enter marks for subject 1:"));
    let mark2 = Number(prompt("Enter marks for subject 2:"));
    let mark3 = Number(prompt("Enter marks for subject 3:"));

    if (isNaN(mark1) || isNaN(mark2) || isNaN(mark3)) {
        showResult("Please enter valid numbers for all subjects.");
        return;
    }

    let average = (mark1 + mark2 + mark3) / 3;

    let grade;
    if (average >= 90) {
        grade = "A";
    } else if (average >= 75) {
        grade = "B";
    } else if (average >= 60) {
        grade = "C";
    } else {
        grade = "F";
    }

    showResult(`Average: ${average.toFixed(2)}, Grade: ${grade}`);
}

// ----- Challenge 5: Random Dice -----
function rollDice() {
    let dice1 = Math.floor(Math.random() * 6) + 1;
    let dice2 = Math.floor(Math.random() * 6) + 1;
    let total = dice1 + dice2;

    showResult(`Dice 1: ${dice1}, Dice 2: ${dice2}, Total: ${total}`);
}
