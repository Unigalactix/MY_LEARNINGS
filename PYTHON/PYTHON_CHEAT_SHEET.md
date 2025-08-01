# Python Cheat Sheet

## 🐍 Python Quick Reference Guide

### Basic Syntax

#### Variables and Data Types
```python
# Variables (no declaration needed)
name = "John"           # String
age = 25               # Integer
height = 5.9           # Float
is_student = True      # Boolean
items = [1, 2, 3]      # List
person = {"name": "John", "age": 25}  # Dictionary

# Type checking
print(type(name))      # <class 'str'>
print(isinstance(age, int))  # True
```

#### String Operations
```python
# String methods
text = "Hello World"
print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(text.strip())         # Remove whitespace
print(text.replace("World", "Python"))  # Hello Python
print(text.split())         # ['Hello', 'World']
print(len(text))           # 11

# String formatting
name = "Alice"
age = 30
print(f"My name is {name} and I'm {age} years old")  # f-strings (Python 3.6+)
print("My name is {} and I'm {} years old".format(name, age))  # format()
print("My name is %s and I'm %d years old" % (name, age))      # % formatting
```

#### List Operations
```python
# List methods
numbers = [1, 2, 3]
numbers.append(4)          # [1, 2, 3, 4]
numbers.insert(0, 0)       # [0, 1, 2, 3, 4]
numbers.remove(2)          # [0, 1, 3, 4]
popped = numbers.pop()     # 4, list becomes [0, 1, 3]
numbers.extend([5, 6])     # [0, 1, 3, 5, 6]

# List comprehensions
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

#### Dictionary Operations
```python
# Dictionary methods
person = {"name": "John", "age": 25}
person["city"] = "New York"     # Add new key-value pair
print(person.get("name"))       # "John"
print(person.get("salary", 0))  # 0 (default value)
print(person.keys())            # dict_keys(['name', 'age', 'city'])
print(person.values())          # dict_values(['John', 25, 'New York'])
print(person.items())           # dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Control Flow

#### Conditional Statements
```python
# if-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary operator
result = "Pass" if score >= 60 else "Fail"
```

#### Loops
```python
# for loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue    # Skip to next iteration
    if i == 7:
        break      # Exit loop
    print(i)
```

### Functions

#### Basic Functions
```python
# Function definition
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Function calls
print(greet("Alice"))                    # Hello, Alice!
print(greet("Bob", "Hi"))               # Hi, Bob!

# *args and **kwargs
def flexible_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

flexible_function(1, 2, 3, name="John", age=25)
# Args: (1, 2, 3)
# Kwargs: {'name': 'John', 'age': 25}
```

#### Lambda Functions
```python
# Lambda (anonymous) functions
square = lambda x: x**2
print(square(5))  # 25

# Using with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))      # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
```

### Object-Oriented Programming

#### Classes and Objects
```python
class Person:
    # Class variable
    species = "Homo sapiens"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name        # Instance variable
        self.age = age         # Instance variable
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating objects
person1 = Person("Alice", 30)
person2 = Person.from_birth_year("Bob", 1990)

print(person1.introduce())      # Hi, I'm Alice and I'm 30 years old
print(Person.is_adult(16))      # False
```

#### Inheritance
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)     # Call parent constructor
        self.student_id = student_id
    
    def introduce(self):                # Method overriding
        return f"Hi, I'm {self.name}, a student with ID {self.student_id}"

student = Student("Charlie", 20, "S12345")
print(student.introduce())  # Hi, I'm Charlie, a student with ID S12345
```

### File Handling

#### Reading and Writing Files
```python
# Writing to file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is awesome!")

# Reading from file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Working with CSV
import csv

# Writing CSV
data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading CSV
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Exception Handling

```python
# try-except-else-finally
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("This always executes")

# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Common Built-in Functions

```python
# Math functions
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))          # 15
print(max(numbers))          # 5
print(min(numbers))          # 1
print(len(numbers))          # 5
print(abs(-5))              # 5
print(round(3.14159, 2))    # 3.14

# Type conversion
print(int("123"))           # 123
print(float("3.14"))        # 3.14
print(str(123))             # "123"
print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']

# Useful functions
print(enumerate(["a", "b", "c"]))  # [(0, 'a'), (1, 'b'), (2, 'c')]
print(zip([1, 2, 3], ["a", "b", "c"]))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(sorted([3, 1, 4, 1, 5]))    # [1, 1, 3, 4, 5]
print(reversed([1, 2, 3]))         # [3, 2, 1]
```

### Modules and Packages

```python
# Importing modules
import math
from datetime import datetime, date
import numpy as np                    # Alias
from collections import Counter, defaultdict

# Using imported modules
print(math.sqrt(16))                 # 4.0
print(datetime.now())                # Current date and time
print(np.array([1, 2, 3]))          # [1 2 3]

# Creating your own module (save as mymodule.py)
def hello(name):
    return f"Hello, {name}!"

PI = 3.14159

# Using your module (in another file)
# import mymodule
# print(mymodule.hello("World"))
# print(mymodule.PI)
```

### List Comprehensions and Generators

```python
# List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
matrix = [[i*j for j in range(3)] for i in range(3)]

# Dictionary comprehensions
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}

# Set comprehensions
unique_lengths = {len(word) for word in ["hello", "world", "python"]}

# Generator expressions
squares_gen = (x**2 for x in range(10))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# Generator functions
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
```

### Decorators

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints "Hello, Alice!" three times
```

### Common Patterns and Idioms

```python
# Swapping variables
a, b = 5, 10
a, b = b, a  # Now a=10, b=5

# Multiple assignment
x, y, z = 1, 2, 3

# Unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers  # first=1, middle=[2,3,4], last=5

# Dictionary default values
from collections import defaultdict
dd = defaultdict(list)
dd['key'].append('value')

# Counter
from collections import Counter
counts = Counter("hello world")
print(counts)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Any and all
print(any([True, False, False]))   # True
print(all([True, False, False]))   # False

# Checking membership
if 'key' in dictionary:
    print("Key exists")

# Safe dictionary access
value = dictionary.get('key', 'default_value')
```

### Performance Tips

```python
# Use list comprehensions instead of loops when possible
# Fast
squares = [x**2 for x in range(1000)]

# Slower
squares = []
for x in range(1000):
    squares.append(x**2)

# Use sets for membership testing
# Fast
valid_ids = {1, 2, 3, 4, 5}
if user_id in valid_ids:
    pass

# Slower for large collections
valid_ids = [1, 2, 3, 4, 5]
if user_id in valid_ids:
    pass

# Use generators for memory efficiency
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Use join() for string concatenation
# Fast
result = ''.join(string_list)

# Slower
result = ''
for s in string_list:
    result += s
```

## 📚 Common Libraries Quick Reference

### datetime
```python
from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
```

### json
```python
import json

# Python to JSON
data = {"name": "John", "age": 30}
json_string = json.dumps(data)

# JSON to Python
parsed_data = json.loads(json_string)
```

### os and pathlib
```python
import os
from pathlib import Path

# os module
current_dir = os.getcwd()
files = os.listdir('.')
os.makedirs('new_folder', exist_ok=True)

# pathlib (more modern)
path = Path('folder/file.txt')
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text('Hello, World!')
```

### requests (external library)
```python
import requests

response = requests.get('https://api.github.com/users/octocat')
data = response.json()
print(data['name'])
```
