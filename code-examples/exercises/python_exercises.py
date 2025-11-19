"""
PYTHON EXERCISES WITH SOLUTIONS
Practice these exercises to master Python basics
"""

print("=" * 60)
print("PYTHON PRACTICE EXERCISES")
print("=" * 60)

# ============================================
# EXERCISE 1: Sum of List
# ============================================
print("\n" + "-" * 60)
print("EXERCISE 1: Sum of List")
print("-" * 60)
print("Task: Create a function that takes a list and returns the sum")

def sum_list(numbers):
    """
    Calculate sum of all numbers in a list
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int/float: Sum of all numbers
    """
    # Solution 1: Using built-in sum()
    return sum(numbers)
    
    # Solution 2: Using loop
    # total = 0
    # for num in numbers:
    #     total += num
    # return total

# Test the function
test_list = [1, 2, 3, 4, 5]
result = sum_list(test_list)
print(f"Sum of {test_list} = {result}")
print(f"Expected: 15, Got: {result}, ✓" if result == 15 else "✗")

# ============================================
# EXERCISE 2: Even Numbers
# ============================================
print("\n" + "-" * 60)
print("EXERCISE 2: Print Even Numbers")
print("-" * 60)
print("Task: Print all even numbers from 1 to 20")

def print_even_numbers(start, end):
    """
    Print all even numbers in a range
    
    Args:
        start (int): Start of range
        end (int): End of range
    """
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    
    print(f"Even numbers from {start} to {end}:")
    print(even_numbers)
    
    # Alternative: List comprehension
    # even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]

print_even_numbers(1, 20)

# ============================================
# EXERCISE 3: Book Dictionary
# ============================================
print("\n" + "-" * 60)
print("EXERCISE 3: Book Dictionary")
print("-" * 60)
print("Task: Create a dictionary of 3 books with title, author, year")

books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Fiction"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Classic"
    }
]

print("Book Collection:")
for i, book in enumerate(books, 1):
    print(f"\nBook {i}:")
    for key, value in book.items():
        print(f"  {key.capitalize()}: {value}")

# ============================================
# EXERCISE 4: Prime Number Checker
# ============================================
print("\n" + "-" * 60)
print("EXERCISE 4: Prime Number Checker")
print("-" * 60)
print("Task: Write a function that checks if a number is prime")

def is_prime(n):
    """
    Check if a number is prime
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if prime, False otherwise
    """
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check if divisible by any number from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Test the function
test_numbers = [2, 3, 4, 5, 10, 17, 20, 29]
print("Prime number tests:")
for num in test_numbers:
    result = is_prime(num)
    print(f"{num}: {'Prime ✓' if result else 'Not Prime ✗'}")

# ============================================
# EXERCISE 5: Car Class
# ============================================
print("\n" + "-" * 60)
print("EXERCISE 5: Car Class")
print("-" * 60)
print("Task: Create a Car class with make, model, year and drive() method")

class Car:
    """
    A class representing a car
    """
    
    def __init__(self, make, model, year):
        """
        Initialize car with make, model, and year
        
        Args:
            make (str): Car manufacturer
            model (str): Car model
            year (int): Manufacturing year
        """
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        """Start the car"""
        if not self.is_running:
            self.is_running = True
            return f"{self.year} {self.make} {self.model} is now running!"
        return "Car is already running!"
    
    def stop(self):
        """Stop the car"""
        if self.is_running:
            self.is_running = False
            return f"{self.year} {self.make} {self.model} has stopped!"
        return "Car is already stopped!"
    
    def drive(self, distance):
        """
        Drive the car
        
        Args:
            distance (int): Distance to drive in miles
        """
        if self.is_running:
            return f"Driving {self.year} {self.make} {self.model} for {distance} miles!"
        return "Start the car first!"
    
    def get_info(self):
        """Get car information"""
        status = "running" if self.is_running else "stopped"
        return f"{self.year} {self.make} {self.model} - Status: {status}"

# Test the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model 3", 2023)

print(car1.get_info())
print(car1.start())
print(car1.drive(50))
print(car1.get_info())
print(car1.stop())
print()
print(car2.get_info())
print(car2.drive(30))  # Should fail - car not started
print(car2.start())
print(car2.drive(30))  # Should work

# ============================================
# BONUS EXERCISES
# ============================================
print("\n" + "=" * 60)
print("BONUS EXERCISES")
print("=" * 60)

# BONUS 1: Fibonacci Sequence
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print("\nBonus 1: Fibonacci Sequence (first 10 terms)")
print(fibonacci(10))

# BONUS 2: Palindrome Checker
def is_palindrome(text):
    """Check if a string is a palindrome"""
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    return text == text[::-1]

print("\nBonus 2: Palindrome Checker")
test_words = ["racecar", "hello", "A man a plan a canal Panama", "python"]
for word in test_words:
    result = is_palindrome(word)
    print(f"'{word}': {'Palindrome ✓' if result else 'Not Palindrome ✗'}")

# BONUS 3: Word Counter
def word_frequency(text):
    """Count frequency of each word in text"""
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # Remove punctuation
        word = word.strip('.,!?;:')
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

print("\nBonus 3: Word Frequency Counter")
sample_text = "Python is awesome. Python is easy to learn. Learn Python today!"
freq = word_frequency(sample_text)
print("Text:", sample_text)
print("Word frequencies:")
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# BONUS 4: Temperature Converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

print("\nBonus 4: Temperature Converter")
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

# BONUS 5: Shopping Cart
class ShoppingCart:
    """A simple shopping cart"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart"""
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        print(f"Added {quantity}x {name} to cart")
    
    def remove_item(self, name):
        """Remove item from cart"""
        self.items = [item for item in self.items if item["name"] != name]
        print(f"Removed {name} from cart")
    
    def get_total(self):
        """Calculate total price"""
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def show_cart(self):
        """Display cart contents"""
        print("\nShopping Cart:")
        if not self.items:
            print("  Cart is empty")
        else:
            for item in self.items:
                total = item["price"] * item["quantity"]
                print(f"  {item['name']}: ${item['price']:.2f} x {item['quantity']} = ${total:.2f}")
            print(f"  Total: ${self.get_total():.2f}")

print("\nBonus 5: Shopping Cart")
cart = ShoppingCart()
cart.add_item("Apple", 0.99, 5)
cart.add_item("Banana", 0.59, 3)
cart.add_item("Milk", 3.49, 1)
cart.show_cart()
cart.remove_item("Banana")
cart.show_cart()

print("\n" + "=" * 60)
print("EXCELLENT WORK! You've completed all Python exercises! 🎉")
print("=" * 60)

