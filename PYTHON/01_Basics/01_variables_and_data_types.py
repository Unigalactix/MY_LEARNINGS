"""
01_PYTHON_BASICS - VARIABLES AND DATA TYPES
===========================================
🎯 Based on roadmap.sh/python recommendations

This module covers the fundamental building blocks of Python:
- Variables and naming conventions (PEP 8 compliant)
- Basic data types with memory management concepts
- Type conversion and type hints
- String formatting (modern f-strings approach)
- Best practices for variable naming and code style

Learning Objectives:
✅ Master variable creation and Python naming conventions
✅ Understand Python's dynamic typing system
✅ Practice type conversion between data types
✅ Learn modern string formatting techniques
✅ Apply PEP 8 style guidelines from day one

Industry Focus:
🏢 Code that follows Python community standards
🏢 Practices used in real-world Python projects
🏢 Foundation for professional Python development
"""

# ============================================================================
# PYTHON VARIABLE NAMING CONVENTIONS (PEP 8 COMPLIANT)
# ============================================================================

# ✅ GOOD: Follow snake_case for variables and functions
first_name = "John"          # Variable: snake_case
last_name = "Doe"
user_age = 25
is_student = True
account_balance = 1500.50

# ✅ GOOD: Descriptive names that explain purpose
current_temperature = 23.5
max_retry_attempts = 3
database_connection_string = "postgresql://localhost:5432/mydb"

# ✅ GOOD: Constants in UPPER_CASE
PI = 3.14159
MAX_FILE_SIZE = 1024 * 1024  # 1MB in bytes
DEFAULT_TIMEOUT = 30

# ❌ AVOID: These work but don't follow Python conventions
firstName = "John"           # camelCase (used in JavaScript, not Python)
Age = 25                     # PascalCase (reserved for classes)
a = 25                       # Non-descriptive single letters
temp = 23.5                  # Abbreviated names (unclear)

print("=== PEP 8 Compliant Variable Examples ===")
print(f"User: {first_name} {last_name}")
print(f"Age: {user_age}, Student: {is_student}")
print(f"Account Balance: ${account_balance}")
print(f"Current Temperature: {current_temperature}°C")

# ============================================================================
# MODERN PYTHON DATA TYPES WITH TYPE HINTS
# ============================================================================

from typing import Optional, Union, List, Dict
from decimal import Decimal
from datetime import datetime

print("\n=== Python Data Types (Modern Approach) ===")

# 1. INTEGER (int) - Whole numbers with unlimited precision
user_id: int = 42
negative_score: int = -17
large_number: int = 999_999_999_999_999_999  # Python allows underscore separators

print(f"User ID: {user_id}, Type: {type(user_id)}")
print(f"Large number: {large_number:,}")  # Format with commas

# 2. FLOAT (float) - IEEE 754 double precision
price: float = 29.99
scientific: float = 2.5e10  # 2.5 * 10^10
precision_demo: float = 0.1 + 0.2  # Floating point precision issue

print(f"Price: ${price:.2f}")
print(f"Scientific notation: {scientific:,.0f}")
print(f"Precision demo: {precision_demo} (not exactly 0.3!)")

# 💡 For financial calculations, use Decimal instead of float
precise_price: Decimal = Decimal('29.99')
tax_rate: Decimal = Decimal('0.08')
total_with_tax: Decimal = precise_price * (1 + tax_rate)
print(f"Precise calculation: ${total_with_tax}")

# 3. STRING (str) - Unicode text with modern formatting
username: str = "python_dev_2025"
api_key: str = 'sk-1234567890abcdef'  # Both quotes work
multiline_query: str = """
    SELECT users.name, users.email
    FROM users
    WHERE users.active = true
    AND users.created_at > '2024-01-01'
"""

# ✅ MODERN: f-string formatting (Python 3.6+)
current_time = datetime.now()
welcome_message = f"Welcome {username}! Today is {current_time:%Y-%m-%d %H:%M}"
print(f"Modern formatting: {welcome_message}")

# ✅ GOOD: Format with precision and padding
pi_formatted = f"π = {PI:.4f}"
padded_number = f"ID: {user_id:05d}"  # Zero-padded to 5 digits
print(f"Formatted π: {pi_formatted}")
print(f"Padded ID: {padded_number}")

# 4. BOOLEAN (bool) - True/False with truthy/falsy concepts
is_authenticated: bool = True
has_premium_subscription: bool = False
is_admin: Optional[bool] = None  # Optional type hint

print(f"Authenticated: {is_authenticated}")
print(f"Premium: {has_premium_subscription}")
print(f"Admin status: {is_admin}")

# 💡 Truthy and Falsy values in Python
truthy_values = [True, 1, "hello", [1, 2, 3], {"key": "value"}]
falsy_values = [False, 0, "", [], {}, None]

print("\n--- Truthy/Falsy Demonstration ---")
for value in truthy_values:
    print(f"bool({value!r}) = {bool(value)}")

for value in falsy_values:
    print(f"bool({value!r}) = {bool(value)}")

# ============================================================================
# TYPE CONVERSION WITH ERROR HANDLING
# ============================================================================

print("\n=== Safe Type Conversion Examples ===")

def safe_int_conversion(value: str) -> Optional[int]:
    """Safely convert string to integer with error handling."""
    try:
        return int(value)
    except ValueError:
        print(f"Warning: Cannot convert '{value}' to integer")
        return None

# Demonstrate safe conversion
test_values = ["123", "45.67", "invalid", "0", "-42"]
for test_val in test_values:
    result = safe_int_conversion(test_val)
    print(f"'{test_val}' -> {result}")

# Advanced type conversion examples
price_string = "29.99"
quantity_string = "5"

try:
    price = float(price_string)
    quantity = int(quantity_string)
    total = price * quantity
    print(f"Order total: ${total:.2f} ({quantity} items at ${price:.2f} each)")
except ValueError as e:
    print(f"Conversion error: {e}")

# Boolean conversion nuances
print(f"\nBoolean conversion examples:")
print(f"bool('False') = {bool('False')}")  # True! (non-empty string)
print(f"bool('') = {bool('')}")             # False (empty string)
print(f"bool(0) = {bool(0)}")               # False
print(f"bool([]) = {bool([])}")             # False (empty list)
print(f"bool([0]) = {bool([0])}")           # True (non-empty list)

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
