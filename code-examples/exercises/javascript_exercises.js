/**
 * JAVASCRIPT EXERCISES WITH SOLUTIONS
 * Practice these exercises to master JavaScript basics
 */

console.log("=".repeat(60));
console.log("JAVASCRIPT PRACTICE EXERCISES");
console.log("=".repeat(60));

// ============================================
// EXERCISE 1: Find Largest Number
// ============================================
console.log("\n" + "-".repeat(60));
console.log("EXERCISE 1: Find Largest Number");
console.log("-".repeat(60));
console.log("Task: Create a function that finds the largest number in an array");

function findLargest(numbers) {
    /**
     * Find the largest number in an array
     * @param {number[]} numbers - Array of numbers
     * @returns {number} - Largest number
     */
    
    // Solution 1: Using Math.max with spread operator
    return Math.max(...numbers);
    
    // Solution 2: Using reduce
    // return numbers.reduce((max, num) => num > max ? num : max, numbers[0]);
    
    // Solution 3: Using loop
    // let max = numbers[0];
    // for (let num of numbers) {
    //     if (num > max) max = num;
    // }
    // return max;
}

// Test the function
const testArray = [3, 67, 15, 42, 8, 91, 24];
const largest = findLargest(testArray);
console.log(`Array: [${testArray}]`);
console.log(`Largest: ${largest}`);
console.log(`Expected: 91, Got: ${largest} ${largest === 91 ? '✓' : '✗'}`);

// ============================================
// EXERCISE 2: Reverse String
// ============================================
console.log("\n" + "-".repeat(60));
console.log("EXERCISE 2: Reverse String");
console.log("-".repeat(60));
console.log("Task: Write a function that reverses a string");

function reverseString(str) {
    /**
     * Reverse a string
     * @param {string} str - String to reverse
     * @returns {string} - Reversed string
     */
    
    // Solution 1: Using built-in methods
    return str.split('').reverse().join('');
    
    // Solution 2: Using loop
    // let reversed = '';
    // for (let i = str.length - 1; i >= 0; i--) {
    //     reversed += str[i];
    // }
    // return reversed;
    
    // Solution 3: Using reduce
    // return str.split('').reduce((reversed, char) => char + reversed, '');
}

// Test the function
const testStrings = ["hello", "JavaScript", "12345"];
console.log("String reversals:");
testStrings.forEach(str => {
    const reversed = reverseString(str);
    console.log(`  "${str}" → "${reversed}"`);
});

// ============================================
// EXERCISE 3: Book Object
// ============================================
console.log("\n" + "-".repeat(60));
console.log("EXERCISE 3: Book Object");
console.log("-".repeat(60));
console.log("Task: Create a book object with properties and methods");

class Book {
    /**
     * A class representing a book
     */
    
    constructor(title, author, year, pages) {
        this.title = title;
        this.author = author;
        this.year = year;
        this.pages = pages;
        this.isRead = false;
    }
    
    getSummary() {
        return `"${this.title}" by ${this.author}, published in ${this.year}`;
    }
    
    markAsRead() {
        this.isRead = true;
        return `You've marked "${this.title}" as read!`;
    }
    
    getAge() {
        const currentYear = new Date().getFullYear();
        return currentYear - this.year;
    }
}

// Test the Book class
const book1 = new Book("1984", "George Orwell", 1949, 328);
const book2 = new Book("The Hobbit", "J.R.R. Tolkien", 1937, 310);

console.log(book1.getSummary());
console.log(`Age: ${book1.getAge()} years old`);
console.log(book1.markAsRead());
console.log(`Read status: ${book1.isRead ? 'Read ✓' : 'Not read'}`);

// ============================================
// EXERCISE 4: Array to Uppercase
// ============================================
console.log("\n" + "-".repeat(60));
console.log("EXERCISE 4: Array to Uppercase");
console.log("-".repeat(60));
console.log("Task: Use map() to convert array of names to uppercase");

function namesToUppercase(names) {
    /**
     * Convert all names in array to uppercase
     * @param {string[]} names - Array of names
     * @returns {string[]} - Array of uppercase names
     */
    return names.map(name => name.toUpperCase());
}

// Test the function
const names = ["alice", "bob", "charlie", "diana"];
const upperNames = namesToUppercase(names);
console.log("Original:", names);
console.log("Uppercase:", upperNames);

// ============================================
// EXERCISE 5: Car Class
// ============================================
console.log("\n" + "-".repeat(60));
console.log("EXERCISE 5: Car Class");
console.log("-".repeat(60));
console.log("Task: Create a Car class with start() and stop() methods");

class Car {
    /**
     * A class representing a car
     */
    
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
        this.speed = 0;
    }
    
    start() {
        if (!this.isRunning) {
            this.isRunning = true;
            return `${this.year} ${this.make} ${this.model} is now running!`;
        }
        return "Car is already running!";
    }
    
    stop() {
        if (this.isRunning) {
            this.isRunning = false;
            this.speed = 0;
            return `${this.year} ${this.make} ${this.model} has stopped!`;
        }
        return "Car is already stopped!";
    }
    
    accelerate(amount) {
        if (this.isRunning) {
            this.speed += amount;
            return `Accelerating to ${this.speed} mph`;
        }
        return "Start the car first!";
    }
    
    getInfo() {
        const status = this.isRunning ? `running at ${this.speed} mph` : "stopped";
        return `${this.year} ${this.make} ${this.model} - Status: ${status}`;
    }
}

// Test the Car class
const car1 = new Car("Toyota", "Camry", 2022);
const car2 = new Car("Tesla", "Model 3", 2023);

console.log(car1.getInfo());
console.log(car1.start());
console.log(car1.accelerate(50));
console.log(car1.getInfo());
console.log(car1.stop());
console.log();
console.log(car2.getInfo());
console.log(car2.accelerate(30)); // Should fail
console.log(car2.start());
console.log(car2.accelerate(30)); // Should work

// ============================================
// BONUS EXERCISES
// ============================================
console.log("\n" + "=".repeat(60));
console.log("BONUS EXERCISES");
console.log("=".repeat(60));

// BONUS 1: FizzBuzz
console.log("\nBonus 1: FizzBuzz");
console.log("Print numbers 1-20, but for multiples of 3 print 'Fizz',");
console.log("for multiples of 5 print 'Buzz', for multiples of both print 'FizzBuzz'");

function fizzBuzz(n) {
    const results = [];
    for (let i = 1; i <= n; i++) {
        if (i % 15 === 0) results.push('FizzBuzz');
        else if (i % 3 === 0) results.push('Fizz');
        else if (i % 5 === 0) results.push('Buzz');
        else results.push(i);
    }
    return results;
}

console.log(fizzBuzz(20).join(', '));

// BONUS 2: Remove Duplicates
console.log("\nBonus 2: Remove Duplicates from Array");

function removeDuplicates(arr) {
    // Solution 1: Using Set
    return [...new Set(arr)];
    
    // Solution 2: Using filter
    // return arr.filter((item, index) => arr.indexOf(item) === index);
}

const duplicates = [1, 2, 2, 3, 4, 4, 5, 1, 6];
console.log("Original:", duplicates);
console.log("Unique:", removeDuplicates(duplicates));

// BONUS 3: Sum of Range
console.log("\nBonus 3: Sum of Range");

function sumRange(start, end) {
    /**
     * Calculate sum of all numbers in a range
     */
    let sum = 0;
    for (let i = start; i <= end; i++) {
        sum += i;
    }
    return sum;
}

console.log(`Sum of 1 to 100: ${sumRange(1, 100)}`);

// BONUS 4: Count Vowels
console.log("\nBonus 4: Count Vowels in String");

function countVowels(str) {
    const vowels = 'aeiouAEIOU';
    let count = 0;
    
    for (let char of str) {
        if (vowels.includes(char)) {
            count++;
        }
    }
    
    return count;
    
    // Alternative: Using regex
    // return (str.match(/[aeiou]/gi) || []).length;
}

const testSentence = "Hello World, JavaScript is awesome!";
console.log(`Sentence: "${testSentence}"`);
console.log(`Vowel count: ${countVowels(testSentence)}`);

// BONUS 5: Todo List Manager
console.log("\nBonus 5: Todo List Manager");

class TodoList {
    constructor() {
        this.todos = [];
        this.nextId = 1;
    }
    
    addTodo(text) {
        const todo = {
            id: this.nextId++,
            text: text,
            completed: false,
            createdAt: new Date()
        };
        this.todos.push(todo);
        return `Added: "${text}"`;
    }
    
    completeTodo(id) {
        const todo = this.todos.find(t => t.id === id);
        if (todo) {
            todo.completed = true;
            return `Completed: "${todo.text}"`;
        }
        return "Todo not found";
    }
    
    removeTodo(id) {
        const index = this.todos.findIndex(t => t.id === id);
        if (index !== -1) {
            const removed = this.todos.splice(index, 1)[0];
            return `Removed: "${removed.text}"`;
        }
        return "Todo not found";
    }
    
    getActiveTodos() {
        return this.todos.filter(todo => !todo.completed);
    }
    
    getCompletedTodos() {
        return this.todos.filter(todo => todo.completed);
    }
    
    displayTodos() {
        console.log("\nTodo List:");
        if (this.todos.length === 0) {
            console.log("  No todos yet!");
        } else {
            this.todos.forEach(todo => {
                const status = todo.completed ? '✓' : ' ';
                console.log(`  [${status}] ${todo.id}. ${todo.text}`);
            });
        }
        console.log(`Total: ${this.todos.length}, Active: ${this.getActiveTodos().length}`);
    }
}

// Test the TodoList
const myTodos = new TodoList();
console.log(myTodos.addTodo("Learn JavaScript"));
console.log(myTodos.addTodo("Build a project"));
console.log(myTodos.addTodo("Deploy to production"));
myTodos.displayTodos();
console.log(myTodos.completeTodo(1));
myTodos.displayTodos();

// BONUS 6: Fetch Simulation
console.log("\nBonus 6: Async Data Fetching (Simulated)");

async function fetchUserData(userId) {
    try {
        console.log(`Fetching user ${userId}...`);
        
        // Simulate API call with delay
        const user = await new Promise((resolve) => {
            setTimeout(() => {
                resolve({
                    id: userId,
                    name: `User ${userId}`,
                    email: `user${userId}@example.com`,
                    joinedAt: new Date()
                });
            }, 1000);
        });
        
        console.log("User data received:", user);
        return user;
    } catch (error) {
        console.error("Error fetching user:", error);
    }
}

// Run async function
fetchUserData(123);

console.log("\n" + "=".repeat(60));
console.log("EXCELLENT WORK! You've completed all JavaScript exercises! 🎉");
console.log("=".repeat(60));

