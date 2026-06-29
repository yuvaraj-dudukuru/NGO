/* ============================================
   JAVASCRIPT PRACTICAL LAB - script.js
   Day 4: JavaScript Basics
   ============================================ */

// ----- Step 2: Display Messages -----
console.log("Hello, this is my JavaScript file!");
console.log("Today is Day 4 of the course.");

// ----- Step 3: Create Variables and Data Types -----
const name = "Priya";        // string
let age = 20;                // number
let isStudent = true;        // boolean

console.log("Name:", name);
console.log("Age:", age);
console.log("Is student:", isStudent);
console.log("Type of age:", typeof age);

// ----- Step 4: Accept Input -----
// prompt returns a string
let userName = prompt("What is your name?");
console.log("Welcome, " + userName);
// Use a template literal too
console.log(`Hello, ${userName}! Nice to meet you.`);

// ----- Step 5: Perform Calculations -----
// Get two numbers (convert from string to number!)
let num1 = Number(prompt("Enter the first number:"));
let num2 = Number(prompt("Enter the second number:"));

let sum = num1 + num2;
let product = num1 * num2;

console.log(`Sum: ${sum}`);
console.log(`Product: ${product}`);

// ----- Step 6: Work With an Array -----
let skills = ["HTML", "CSS", "JavaScript"];
console.log("My skills:", skills);
console.log("First skill:", skills[0]);
console.log("Number of skills:", skills.length);

skills.push("Git");              // add to the end
console.log("After adding Git:", skills);

// ----- Step 7: Display Results to the User -----
let marks = Number(prompt("Enter your marks (0-100):"));
if (isNaN(marks)) {
    alert("That is not a valid number.");
} else if (marks >= 40) {
    alert(`You scored ${marks}. Result: Pass`);
} else {
    alert(`You scored ${marks}. Result: Fail`);
}
