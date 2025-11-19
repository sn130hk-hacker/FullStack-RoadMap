"""
PHASE 1: Python Basics - Complete Beginner Guide
Learn by reading code and running examples
"""

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================

print("=" * 50)
print("1. VARIABLES AND DATA TYPES")
print("=" * 50)

# Integers (whole numbers)
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Floats (decimal numbers)
price = 19.99
print(f"Price: {price}, Type: {type(price)}")

# Strings (text)
name = "John"
greeting = 'Hello World'
print(f"Name: {name}, Type: {type(name)}")

# Booleans (True/False)
is_student = True
has_license = False
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Lists (ordered collection)
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
print(f"Fruits: {fruits}, Type: {type(fruits)}")

# Dictionaries (key-value pairs)
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}, Type: {type(person)}")

# ============================================
# 2. BASIC OPERATORS
# ============================================

print("\n" + "=" * 50)
print("2. BASIC OPERATORS")
print("=" * 50)

# Arithmetic operators
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# Comparison operators
print(f"\n{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# ============================================
# 3. CONTROL STRUCTURES - IF/ELSE
# ============================================

print("\n" + "=" * 50)
print("3. IF/ELSE STATEMENTS")
print("=" * 50)

# Simple if statement
temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's nice outside!")
else:
    print("It's cold outside!")

# Multiple conditions
age = 18
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")
else:
    print("Sorry, you cannot enter")

# ============================================
# 4. LOOPS
# ============================================

print("\n" + "=" * 50)
print("4. LOOPS")
print("=" * 50)

# For loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# For loop with list
print("\nFruits list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"- {fruit}")

# While loop
print("\nCountdown:")
count = 5
while count > 0:
    print(f"{count}...")
    count -= 1
print("Blast off!")

# ============================================
# 5. FUNCTIONS
# ============================================

print("\n" + "=" * 50)
print("5. FUNCTIONS")
print("=" * 50)

# Simple function
def greet(name):
    """Function to greet someone"""
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers and return result"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameter
def introduce(name, age=18):
    """Introduce a person"""
    return f"My name is {name} and I am {age} years old"

print(introduce("Bob"))
print(introduce("Charlie", 25))

# ============================================
# 6. LISTS AND LIST OPERATIONS
# ============================================

print("\n" + "=" * 50)
print("6. LIST OPERATIONS")
print("=" * 50)

# Creating and accessing lists
numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")
print(f"First item: {numbers[0]}")
print(f"Last item: {numbers[-1]}")
print(f"Slice (2nd to 4th): {numbers[1:4]}")

# List methods
numbers.append(6)
print(f"After append(6): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

numbers.remove(3)
print(f"After remove(3): {numbers}")

# List comprehension (advanced but useful)
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# ============================================
# 7. DICTIONARIES
# ============================================

print("\n" + "=" * 50)
print("7. DICTIONARIES")
print("=" * 50)

# Creating and accessing dictionaries
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science"],
    "gpa": 3.8
}

print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")

# Adding/modifying values
student["email"] = "john@email.com"
student["age"] = 21

print(f"Updated student: {student}")

# Dictionary methods
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")

# Looping through dictionary
print("\nStudent information:")
for key, value in student.items():
    print(f"  {key}: {value}")

# ============================================
# 8. ERROR HANDLING
# ============================================

print("\n" + "=" * 50)
print("8. ERROR HANDLING")
print("=" * 50)

# Try-except block
def divide_numbers(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only!"

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))

# ============================================
# 9. FILE OPERATIONS
# ============================================

print("\n" + "=" * 50)
print("9. FILE OPERATIONS")
print("=" * 50)

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python file operations are easy!\n")
print("File written successfully!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# ============================================
# 10. CLASSES AND OBJECTS (OOP Basics)
# ============================================

print("\n" + "=" * 50)
print("10. CLASSES AND OBJECTS")
print("=" * 50)

class Dog:
    """A simple Dog class"""
    
    def __init__(self, name, age):
        """Initialize dog with name and age"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Get dog information"""
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog1.get_info())
print(dog2.bark())
print(dog2.get_info())

# ============================================
# PRACTICE EXERCISES
# ============================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

"""
Try these exercises:

1. Create a function that takes a list of numbers and returns the sum

2. Write a program that prints all even numbers from 1 to 20

3. Create a dictionary of 3 books with title, author, and year

4. Write a function that checks if a number is prime

5. Create a class 'Car' with attributes make, model, year and method drive()

See solutions in exercises folder!
"""

print("\nGreat job! You've learned Python basics!")
print("Next: Try the practice exercises in the exercises folder")

