# ================================
# SOLUTIONS: Python Intermediate Exercises
# ================================

import math
from collections import Counter

# Exercise 7: Functions
print("=== Exercise 7: Functions ===")

# 1. Calculate area of rectangle
def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

print(f"Rectangle area (5x3): {rectangle_area(5, 3)}")

# 2. Calculate average of a list
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

test_numbers = [10, 20, 30, 40, 50]
print(f"Average of {test_numbers}: {calculate_average(test_numbers)}")

# 3. Check if string is palindrome
def is_palindrome(text):
    """Check if a string is a palindrome."""
    # Remove spaces and convert to lowercase
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

test_word = "racecar"
print(f"'{test_word}' is palindrome: {is_palindrome(test_word)}")

# 4. Generate Fibonacci sequence
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

fib_sequence = fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_sequence}")

print()

# Exercise 8: List Comprehensions
print("=== Exercise 8: List Comprehensions ===")

# 1. Squares of numbers 1-10
squares = [x**2 for x in range(1, 11)]
print(f"Squares 1-10: {squares}")

# 2. Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# 3. Length of words in sentence
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in sentence.split()]
print(f"Word lengths: {word_lengths}")

# 4. Combinations of two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combinations = [(x, y) for x in list1 for y in list2]
print(f"Combinations: {combinations}")

print()

# Exercise 9: File Handling
print("=== Exercise 9: File Handling ===")

# 1. Create and write quotes to file
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens to you while you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]

def write_quotes_to_file(filename, quotes_list):
    """Write quotes to a file."""
    try:
        with open(filename, 'w') as file:
            for quote in quotes_list:
                file.write(quote + '\n')
        print(f"Quotes written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# 2. Read file and count lines
def count_lines_in_file(filename):
    """Count the number of lines in a file."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return 0

# 3. Append new quotes
def append_quotes_to_file(filename, new_quotes):
    """Append new quotes to existing file."""
    try:
        with open(filename, 'a') as file:
            for quote in new_quotes:
                file.write(quote + '\n')
        print(f"New quotes appended to {filename}")
    except IOError as e:
        print(f"Error appending to file: {e}")

# Simulate file operations (commented out to avoid actual file creation)
# write_quotes_to_file('quotes.txt', quotes)
# line_count = count_lines_in_file('quotes.txt')
# print(f"Number of lines: {line_count}")

print()

# Exercise 10: Exception Handling
print("=== Exercise 10: Exception Handling ===")

# 1. Calculator with division by zero handling
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# 2. Number input validation
def get_valid_number(prompt="Enter a number: "):
    """Get a valid number from user input with error handling."""
    while True:
        try:
            # In real program, use input(prompt)
            user_input = "42"  # Simulating user input
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            # In real program, this would continue the loop

number = get_valid_number()
print(f"You entered: {number}")

# 3. Custom exception for email validation
class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses."""
    pass

def validate_email(email):
    """Validate email address format."""
    if '@' not in email:
        raise InvalidEmailError("Email must contain @ symbol")
    if '.' not in email.split('@')[1]:
        raise InvalidEmailError("Email domain must contain a dot")
    if len(email) < 5:
        raise InvalidEmailError("Email too short")
    return True

# Test email validation
test_emails = ["user@example.com", "invalid-email", "user@domain"]
for email in test_emails:
    try:
        validate_email(email)
        print(f"'{email}' is valid")
    except InvalidEmailError as e:
        print(f"'{email}' is invalid: {e}")

print()

# Exercise 11: Classes and Objects
print("=== Exercise 11: Classes and Objects ===")

# 1. Student class
class Student:
    """A class to represent a student."""
    
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades else []
    
    def add_grade(self, grade):
        """Add a grade to the student's record."""
        self.grades.append(grade)
    
    def calculate_average(self):
        """Calculate the average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def is_passing(self, passing_grade=60):
        """Check if student is passing."""
        return self.calculate_average() >= passing_grade
    
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Average: {self.calculate_average():.2f}"

# Test Student class
student1 = Student("Alice", 20, [85, 90, 78, 92])
print(student1)
print(f"Is passing: {student1.is_passing()}")

# 2. BankAccount class
class BankAccount:
    """A class to represent a bank account."""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money to the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            return True
        return False
    
    def get_balance(self):
        """Get current balance."""
        return self.balance
    
    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"

# Test BankAccount class
account = BankAccount("John Doe", 1000)
print(account)
account.deposit(500)
account.withdraw(200)
print(f"Final balance: ${account.get_balance():.2f}")

print("\n=== All Intermediate Exercises Complete! ===")
