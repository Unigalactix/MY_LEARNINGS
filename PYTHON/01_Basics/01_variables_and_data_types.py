"""
01_BASICS - VARIABLES AND DATA TYPES
=====================================

This module covers the fundamental building blocks of Python:
- Variables and naming conventions
- Basic data types (int, float, str, bool)
- Type conversion
- Basic operations

Learning Objectives:
- Understand how to create and use variables
- Learn about different data types in Python
- Practice type conversion between data types
- Perform basic arithmetic and string operations
"""

# ============================================================================
# VARIABLES IN PYTHON
# ============================================================================

# Variables are containers for storing data values
# Python has no command for declaring a variable
# A variable is created the moment you first assign a value to it

# Variable naming rules:
# 1. Must start with a letter or underscore
# 2. Cannot start with a number
# 3. Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
# 4. Are case-sensitive (age, Age and AGE are three different variables)

# Good variable names (following Python conventions)
first_name = "John"          # Use snake_case for variable names
last_name = "Doe"
age = 25
is_student = True

# Avoid these naming patterns (but they're technically valid)
firstName = "John"           # camelCase (not preferred in Python)
Age = 25                     # Starting with capital letter (usually for classes)

print("=== Variable Examples ===")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Is student: {is_student}")

# ============================================================================
# DATA TYPES
# ============================================================================

print("\n=== Python Data Types ===")

# 1. INTEGER (int) - Whole numbers
my_int = 42
negative_int = -17
large_int = 999999999999999999999999999  # Python handles arbitrarily large integers

print(f"Integer: {my_int}, Type: {type(my_int)}")
print(f"Negative integer: {negative_int}")
print(f"Large integer: {large_int}")

# 2. FLOAT (float) - Decimal numbers
my_float = 3.14159
scientific_notation = 2.5e10  # 2.5 * 10^10
negative_float = -0.001

print(f"Float: {my_float}, Type: {type(my_float)}")
print(f"Scientific notation: {scientific_notation}")
print(f"Negative float: {negative_float}")

# 3. STRING (str) - Text data
my_string = "Hello, World!"
single_quotes = 'Python is awesome'
multiline_string = """This is a
multiline string that
spans multiple lines"""

print(f"String: {my_string}, Type: {type(my_string)}")
print(f"Single quotes: {single_quotes}")
print(f"Multiline string: {multiline_string}")

# 4. BOOLEAN (bool) - True or False
is_python_fun = True
is_learning_hard = False

print(f"Boolean True: {is_python_fun}, Type: {type(is_python_fun)}")
print(f"Boolean False: {is_learning_hard}")

# ============================================================================
# TYPE CONVERSION (CASTING)
# ============================================================================

print("\n=== Type Conversion Examples ===")

# Converting between data types
original_number = "123"          # This is a string
converted_int = int(original_number)     # Convert string to integer
converted_float = float(original_number) # Convert string to float

print(f"Original (string): '{original_number}', Type: {type(original_number)}")
print(f"Converted to int: {converted_int}, Type: {type(converted_int)}")
print(f"Converted to float: {converted_float}, Type: {type(converted_float)}")

# Converting numbers to strings
number = 456
number_as_string = str(number)
print(f"Number to string: '{number_as_string}', Type: {type(number_as_string)}")

# Boolean conversions
print(f"int(True): {int(True)}")     # True becomes 1
print(f"int(False): {int(False)}")   # False becomes 0
print(f"bool(1): {bool(1)}")         # Non-zero numbers become True
print(f"bool(0): {bool(0)}")         # Zero becomes False
print(f"bool('hello'): {bool('hello')}")  # Non-empty strings become True
print(f"bool(''): {bool('')}")       # Empty strings become False

# ============================================================================
# BASIC OPERATIONS
# ============================================================================

print("\n=== Basic Operations ===")

# Arithmetic operations
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: a + b = {a + b}")
print(f"Subtraction: a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division: a / b = {a / b}")           # Returns float
print(f"Floor Division: a // b = {a // b}")   # Returns integer (rounds down)
print(f"Modulus: a % b = {a % b}")            # Remainder after division
print(f"Exponentiation: a ** b = {a ** b}")   # a to the power of b

# String operations
greeting = "Hello"
name = "Python"

print(f"\nString concatenation: '{greeting}' + ' ' + '{name}' = '{greeting + ' ' + name}'")
print(f"String repetition: '{greeting}' * 3 = '{greeting * 3}'")

# ============================================================================
# PRACTICAL EXERCISES
# ============================================================================

print("\n=== Practical Exercises ===")

# Exercise 1: Calculate area of a rectangle
length = 15.5
width = 8.2
area = length * width
print(f"Rectangle area: {length} * {width} = {area}")

# Exercise 2: Convert temperature from Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature conversion: {celsius}°C = {fahrenheit}°F")

# Exercise 3: Calculate compound interest
principal = 1000        # Initial amount
rate = 0.05            # 5% interest rate
time = 3               # 3 years
compound_interest = principal * (1 + rate) ** time
print(f"Compound Interest: ${principal} at {rate*100}% for {time} years = ${compound_interest:.2f}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. Variables in Python are dynamically typed (no need to declare type)
2. Use descriptive variable names following snake_case convention
3. Python has four main built-in data types: int, float, str, bool
4. Type conversion is explicit in Python using int(), float(), str(), bool()
5. Python supports all standard arithmetic operations
6. Use the type() function to check the data type of any variable

Common Mistakes to Avoid:
- Don't use reserved keywords as variable names (e.g., print, if, for)
- Be careful with type conversion - not all conversions are possible
- Remember that division (/) always returns a float, use (//) for integer division
"""

print("\n" + "="*50)
print("END OF MODULE 01 - VARIABLES AND DATA TYPES")
print("="*50)
