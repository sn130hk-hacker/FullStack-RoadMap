/**
 * PHASE 1: JavaScript Basics - Complete Beginner Guide
 * Learn by reading code and running examples in browser console or Node.js
 */

// ============================================
// 1. VARIABLES AND DATA TYPES
// ============================================

console.log("=" .repeat(50));
console.log("1. VARIABLES AND DATA TYPES");
console.log("=" .repeat(50));

// Variables (let, const, var)
let age = 25;                    // Can be reassigned
const PI = 3.14159;              // Cannot be reassigned
var oldWay = "avoid this";       // Old way, use let/const instead

console.log("Age:", age, "Type:", typeof age);

// Numbers
const integer = 42;
const decimal = 19.99;
console.log("Integer:", integer, "Decimal:", decimal);

// Strings
const name = "John";
const greeting = 'Hello World';
const template = `My name is ${name}`;  // Template literal
console.log("Name:", name);
console.log("Template:", template);

// Booleans
const isStudent = true;
const hasLicense = false;
console.log("Is Student:", isStudent, "Type:", typeof isStudent);

// Arrays (ordered collection)
const fruits = ["apple", "banana", "orange"];
const numbers = [1, 2, 3, 4, 5];
console.log("Fruits:", fruits);

// Objects (key-value pairs)
const person = {
    name: "Alice",
    age: 30,
    city: "New York"
};
console.log("Person:", person);

// Null and Undefined
let notDefined;
let empty = null;
console.log("Undefined:", notDefined, "Null:", empty);

// ============================================
// 2. BASIC OPERATORS
// ============================================

console.log("\n" + "=".repeat(50));
console.log("2. BASIC OPERATORS");
console.log("=".repeat(50));

// Arithmetic operators
const a = 10;
const b = 3;

console.log(`Addition: ${a} + ${b} = ${a + b}`);
console.log(`Subtraction: ${a} - ${b} = ${a - b}`);
console.log(`Multiplication: ${a} * ${b} = ${a * b}`);
console.log(`Division: ${a} / ${b} = ${a / b}`);
console.log(`Modulus: ${a} % ${b} = ${a % b}`);
console.log(`Power: ${a} ** ${b} = ${a ** b}`);

// Comparison operators
console.log(`\n${a} > ${b}: ${a > b}`);
console.log(`${a} < ${b}: ${a < b}`);
console.log(`${a} === ${b}: ${a === b}`);  // Strict equality
console.log(`${a} !== ${b}: ${a !== b}`);

// Logical operators
console.log(`true && false: ${true && false}`);
console.log(`true || false: ${true || false}`);
console.log(`!true: ${!true}`);

// ============================================
// 3. CONTROL STRUCTURES - IF/ELSE
// ============================================

console.log("\n" + "=".repeat(50));
console.log("3. IF/ELSE STATEMENTS");
console.log("=".repeat(50));

// Simple if statement
const temperature = 25;

if (temperature > 30) {
    console.log("It's hot outside!");
} else if (temperature > 20) {
    console.log("It's nice outside!");
} else {
    console.log("It's cold outside!");
}

// Ternary operator (shorthand)
const status = age >= 18 ? "Adult" : "Minor";
console.log("Status:", status);

// Switch statement
const day = "Monday";
switch (day) {
    case "Monday":
        console.log("Start of work week");
        break;
    case "Friday":
        console.log("Almost weekend!");
        break;
    case "Saturday":
    case "Sunday":
        console.log("Weekend!");
        break;
    default:
        console.log("Regular day");
}

// ============================================
// 4. LOOPS
// ============================================

console.log("\n" + "=".repeat(50));
console.log("4. LOOPS");
console.log("=".repeat(50));

// For loop
console.log("Counting from 1 to 5:");
for (let i = 1; i <= 5; i++) {
    console.log(`Number: ${i}`);
}

// For...of loop (arrays)
console.log("\nFruits list:");
for (const fruit of fruits) {
    console.log(`- ${fruit}`);
}

// For...in loop (objects)
console.log("\nPerson info:");
for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}

// While loop
console.log("\nCountdown:");
let count = 5;
while (count > 0) {
    console.log(`${count}...`);
    count--;
}
console.log("Blast off!");

// ============================================
// 5. FUNCTIONS
// ============================================

console.log("\n" + "=".repeat(50));
console.log("5. FUNCTIONS");
console.log("=".repeat(50));

// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Alice"));

// Function with multiple parameters
function addNumbers(a, b) {
    return a + b;
}

const result = addNumbers(5, 3);
console.log(`5 + 3 = ${result}`);

// Function with default parameter
function introduce(name, age = 18) {
    return `My name is ${name} and I am ${age} years old`;
}

console.log(introduce("Bob"));
console.log(introduce("Charlie", 25));

// Arrow functions (modern syntax)
const multiply = (a, b) => a * b;
const square = x => x ** 2;

console.log("5 * 3 =", multiply(5, 3));
console.log("5² =", square(5));

// ============================================
// 6. ARRAYS AND ARRAY METHODS
// ============================================

console.log("\n" + "=".repeat(50));
console.log("6. ARRAY METHODS");
console.log("=".repeat(50));

// Array methods
let numArray = [1, 2, 3, 4, 5];
console.log("Original array:", numArray);

// Push and pop
numArray.push(6);
console.log("After push(6):", numArray);

const last = numArray.pop();
console.log("Popped:", last, "Array:", numArray);

// Map (transform each element)
const doubled = numArray.map(num => num * 2);
console.log("Doubled:", doubled);

// Filter (keep elements that match condition)
const evens = numArray.filter(num => num % 2 === 0);
console.log("Even numbers:", evens);

// Reduce (combine all elements into one value)
const sum = numArray.reduce((acc, num) => acc + num, 0);
console.log("Sum:", sum);

// Find
const found = numArray.find(num => num > 3);
console.log("First number > 3:", found);

// Some and Every
const hasEven = numArray.some(num => num % 2 === 0);
const allPositive = numArray.every(num => num > 0);
console.log("Has even:", hasEven, "All positive:", allPositive);

// ============================================
// 7. OBJECTS
// ============================================

console.log("\n" + "=".repeat(50));
console.log("7. OBJECTS");
console.log("=".repeat(50));

// Creating and accessing objects
const student = {
    name: "John",
    age: 20,
    courses: ["Math", "Science"],
    gpa: 3.8,
    
    // Object method
    study: function() {
        return `${this.name} is studying`;
    }
};

console.log("Student name:", student.name);
console.log("Student age:", student["age"]);
console.log(student.study());

// Adding/modifying properties
student.email = "john@email.com";
student.age = 21;
console.log("Updated student:", student);

// Object destructuring
const { name: studentName, age: studentAge } = student;
console.log("Destructured:", studentName, studentAge);

// Object methods
console.log("Keys:", Object.keys(student));
console.log("Values:", Object.values(student));

// ============================================
// 8. ERROR HANDLING
// ============================================

console.log("\n" + "=".repeat(50));
console.log("8. ERROR HANDLING");
console.log("=".repeat(50));

// Try-catch block
function divideNumbers(a, b) {
    try {
        if (b === 0) {
            throw new Error("Cannot divide by zero!");
        }
        return `${a} / ${b} = ${a / b}`;
    } catch (error) {
        return `Error: ${error.message}`;
    }
}

console.log(divideNumbers(10, 2));
console.log(divideNumbers(10, 0));

// ============================================
// 9. ASYNC JAVASCRIPT - BASICS
// ============================================

console.log("\n" + "=".repeat(50));
console.log("9. ASYNC JAVASCRIPT");
console.log("=".repeat(50));

// setTimeout
console.log("Start");
setTimeout(() => {
    console.log("This runs after 2 seconds");
}, 2000);
console.log("End");

// Promises
const myPromise = new Promise((resolve, reject) => {
    const success = true;
    
    setTimeout(() => {
        if (success) {
            resolve("Promise resolved!");
        } else {
            reject("Promise rejected!");
        }
    }, 1000);
});

myPromise
    .then(result => console.log(result))
    .catch(error => console.error(error));

// Async/Await (modern approach)
async function fetchData() {
    try {
        console.log("Fetching data...");
        // Simulating API call
        const data = await new Promise(resolve => {
            setTimeout(() => resolve({ id: 1, name: "Data" }), 1000);
        });
        console.log("Data received:", data);
    } catch (error) {
        console.error("Error:", error);
    }
}

fetchData();

// ============================================
// 10. CLASSES (ES6)
// ============================================

console.log("\n" + "=".repeat(50));
console.log("10. CLASSES");
console.log("=".repeat(50));

class Dog {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    bark() {
        return `${this.name} says Woof!`;
    }
    
    getInfo() {
        return `${this.name} is ${this.age} years old`;
    }
}

// Creating objects
const dog1 = new Dog("Buddy", 3);
const dog2 = new Dog("Max", 5);

console.log(dog1.bark());
console.log(dog1.getInfo());
console.log(dog2.bark());

// ============================================
// 11. MODERN JAVASCRIPT (ES6+)
// ============================================

console.log("\n" + "=".repeat(50));
console.log("11. MODERN JAVASCRIPT");
console.log("=".repeat(50));

// Spread operator
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log("Combined arrays:", combined);

// Rest parameters
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}

console.log("Sum of 1,2,3,4,5:", sum(1, 2, 3, 4, 5));

// Destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log("First:", first, "Second:", second, "Rest:", rest);

// Optional chaining
const user = {
    name: "Alice",
    address: {
        city: "New York"
    }
};

console.log("City:", user?.address?.city);
console.log("ZIP:", user?.address?.zip); // undefined, but no error

// ============================================
// PRACTICE EXERCISES
// ============================================

console.log("\n" + "=".repeat(50));
console.log("PRACTICE EXERCISES");
console.log("=".repeat(50));

/**
 * Try these exercises:
 * 
 * 1. Create a function that takes an array and returns the largest number
 * 
 * 2. Write a function that reverses a string
 * 
 * 3. Create an object representing a book with properties and methods
 * 
 * 4. Use map() to convert an array of names to uppercase
 * 
 * 5. Create a class 'Car' with methods start() and stop()
 * 
 * See solutions in exercises folder!
 */

console.log("\nGreat job! You've learned JavaScript basics!");
console.log("Next: Try the practice exercises in the exercises folder");

