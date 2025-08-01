# Python Cheat Sheet 🐍

## Quick Reference Guide for Python Programming

### 📝 Basic Syntax

```python
# Comments
# This is a single line comment
"""
This is a
multi-line comment
"""

# Print statement
print("Hello, World!")

# Variables (no declaration needed)
name = "Python"
age = 30
is_awesome = True
```

## 🔢 Data Types

### Numeric Types
```python
# Integer
x = 10
y = -5

# Float
pi = 3.14159
temperature = -20.5

# Complex
z = 3 + 4j

# Type conversion
int_val = int(3.14)      # 3
float_val = float(10)    # 10.0
str_val = str(123)       # "123"
```

### String Operations
```python
# String creation
name = "Python"
message = 'Hello World'
multiline = """This is a
multi-line string"""

# String methods
text = "Hello World"
text.upper()           # "HELLO WORLD"
text.lower()           # "hello world"
text.strip()           # Remove whitespace
text.replace("World", "Python")  # "Hello Python"
text.split()           # ["Hello", "World"]
len(text)              # 11

# String formatting
name = "Alice"
age = 25
f"My name is {name} and I'm {age}"  # f-strings (Python 3.6+)
"My name is {} and I'm {}".format(name, age)  # .format()
"My name is %s and I'm %d" % (name, age)      # % formatting
```

## 📊 Data Structures

### Lists (Mutable, Ordered)
```python
# Creation
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Common operations
fruits.append("grape")        # Add to end
fruits.insert(1, "mango")    # Insert at index
fruits.remove("banana")      # Remove by value
fruits.pop()                 # Remove last item
fruits.pop(0)                # Remove at index
len(fruits)                  # Length
fruits[0]                    # Access by index
fruits[-1]                   # Last item
fruits[1:3]                  # Slicing
fruits[::-1]                 # Reverse

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Tuples (Immutable, Ordered)
```python
# Creation
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Operations
coordinates[0]     # Access by index
len(coordinates)   # Length
x, y = coordinates # Unpacking
```

### Dictionaries (Mutable, Key-Value Pairs)
```python
# Creation
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}

# Operations
person["name"]              # Access value
person["email"] = "alice@example.com"  # Add/update
del person["city"]          # Delete key
person.get("age", 0)        # Get with default
person.keys()               # Get all keys
person.values()             # Get all values
person.items()              # Get key-value pairs

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
```

### Sets (Mutable, Unique Elements)
```python
# Creation
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Operations
fruits.add("grape")         # Add element
fruits.remove("banana")     # Remove element
fruits.discard("mango")     # Remove if exists
len(fruits)                 # Size
"apple" in fruits          # Membership test

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1 | set2                # Union: {1, 2, 3, 4, 5}
set1 & set2                # Intersection: {3}
set1 - set2                # Difference: {1, 2}
```

## 🔄 Control Flow

### Conditional Statements
```python
# if/elif/else
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
if age >= 18 and age < 65:
    print("Working age")
```

### Loops
```python
# For loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for fruit in ["apple", "banana"]:
    print(fruit)

for i, fruit in enumerate(["apple", "banana"]):
    print(f"{i}: {fruit}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue    # Skip iteration
    if i == 7:
        break      # Exit loop
    print(i)
```

## 🎯 Functions

### Basic Functions
```python
# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function with default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple parameters
def add(a, b):
    return a + b

# Variable arguments
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda functions
square = lambda x: x**2
add = lambda x, y: x + y
```

## 🏗️ Object-Oriented Programming

### Classes and Objects
```python
class Person:
    # Class variable
    species = "Homo sapiens"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name    # Instance variable
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name}"
    
    # Class method
    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split('-')
        return cls(name, int(age))
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Usage
person = Person("Alice", 30)
print(person.introduce())
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

## 📁 File Handling

```python
# Reading files
with open('file.txt', 'r') as file:
    content = file.read()           # Read entire file
    lines = file.readlines()       # Read all lines
    
# Writing files
with open('file.txt', 'w') as file:
    file.write("Hello, World!")
    
# Appending to files
with open('file.txt', 'a') as file:
    file.write("New line\n")

# Working with CSV
import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## ⚠️ Exception Handling

```python
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    # Some code
    pass
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exceptions occurred")
finally:
    print("This always runs")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

## 📦 Modules and Packages

```python
# Importing modules
import math
from datetime import datetime
import numpy as np              # With alias
from collections import Counter, defaultdict

# Using imported modules
math.sqrt(16)                   # 4.0
datetime.now()                  # Current date/time

# Creating your own module (save as mymodule.py)
def my_function():
    return "Hello from my module!"

# Importing your module
from mymodule import my_function
```

## 🛠️ Built-in Functions

```python
# Common built-in functions
len([1, 2, 3])                  # 3
max([1, 5, 3])                  # 5
min([1, 5, 3])                  # 1
sum([1, 2, 3])                  # 6
abs(-5)                         # 5
round(3.14159, 2)               # 3.14
sorted([3, 1, 4])               # [1, 3, 4]
reversed([1, 2, 3])             # [3, 2, 1]
enumerate(['a', 'b', 'c'])      # [(0, 'a'), (1, 'b'), (2, 'c')]
zip([1, 2], ['a', 'b'])         # [(1, 'a'), (2, 'b')]
range(5)                        # [0, 1, 2, 3, 4]
```

## 📈 List/Dict/Set Comprehensions

```python
# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
words = [word.upper() for word in ['hello', 'world']]

# Dictionary comprehensions
squares_dict = {x: x**2 for x in range(5)}
word_lengths = {word: len(word) for word in ['hello', 'world']}

# Set comprehensions
unique_squares = {x**2 for x in range(-5, 6)}
```

## 🚀 Advanced Features

### Decorators
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

### Generators
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Generator expression
squares = (x**2 for x in range(10))
```

### Context Managers
```python
# Using with statement
with open('file.txt', 'r') as f:
    content = f.read()

# Creating context manager
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
```

## 📚 Popular Libraries

```python
# Data manipulation
import pandas as pd
import numpy as np

# Web requests
import requests
response = requests.get('https://api.example.com')

# Date and time
from datetime import datetime, timedelta
now = datetime.now()

# JSON handling
import json
data = json.loads('{"name": "Alice"}')
json_string = json.dumps({"name": "Alice"})

# Regular expressions
import re
pattern = r'\d+'
matches = re.findall(pattern, "I have 5 cats and 3 dogs")
```

## 💡 Python Best Practices

1. **Follow PEP 8** - Python's official style guide
2. **Use meaningful variable names** - `user_count` not `uc`
3. **Write docstrings** for functions and classes
4. **Handle exceptions** appropriately
5. **Use list comprehensions** when appropriate
6. **Avoid global variables** when possible
7. **Use `with` statements** for file handling
8. **Test your code** regularly
9. **Use virtual environments** for projects
10. **Comment your code** for clarity

---

## 🔗 Quick References

- **String formatting**: `f"{var}"` (f-strings)
- **List slicing**: `list[start:end:step]`
- **Dictionary get**: `dict.get(key, default)`
- **Exception handling**: `try/except/finally`
- **File handling**: `with open() as file:`
- **List comprehension**: `[expr for item in iterable if condition]`

**Happy Python Programming!** 🐍✨
