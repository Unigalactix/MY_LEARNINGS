"""
01_BASICS - OPERATORS AND EXPRESSIONS
======================================

This module covers all types of operators in Python:
- Arithmetic operators
- Comparison operators  
- Logical operators
- Assignment operators
- Bitwise operators
- Membership operators
- Identity operators

Learning Objectives:
- Understand different types of operators
- Learn operator precedence
- Practice building complex expressions
- Master boolean logic
"""

# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================

print("=== Arithmetic Operators ===")

# Basic arithmetic operators
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition: a + b = {a + b}")                    # 19
print(f"Subtraction: a - b = {a - b}")                 # 11
print(f"Multiplication: a * b = {a * b}")              # 60
print(f"Division: a / b = {a / b}")                    # 3.75 (always returns float)
print(f"Floor Division: a // b = {a // b}")            # 3 (rounds down to nearest integer)
print(f"Modulus: a % b = {a % b}")                     # 3 (remainder after division)
print(f"Exponentiation: a ** b = {a ** b}")            # 50625 (15 to the power of 4)

# Practical examples of modulus operator
print("\n--- Modulus Operator Examples ---")
print(f"10 % 3 = {10 % 3}")  # 1 (remainder when 10 is divided by 3)
print(f"Is 10 even? {10 % 2 == 0}")  # True (even numbers have remainder 0 when divided by 2)
print(f"Is 11 even? {11 % 2 == 0}")  # False

# Finding last digit of a number
number = 12345
last_digit = number % 10
print(f"Last digit of {number} is {last_digit}")

# ============================================================================
# COMPARISON (RELATIONAL) OPERATORS
# ============================================================================

print("\n=== Comparison Operators ===")

x = 10
y = 20
z = 10

print(f"x = {x}, y = {y}, z = {z}")

# Comparison operators return boolean values (True or False)
print(f"x == z: {x == z}")    # Equal to
print(f"x != y: {x != y}")    # Not equal to
print(f"x < y: {x < y}")      # Less than
print(f"x > y: {x > y}")      # Greater than
print(f"x <= z: {x <= z}")    # Less than or equal to
print(f"y >= x: {y >= x}")    # Greater than or equal to

# String comparisons (lexicographic order)
print("\n--- String Comparisons ---")
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"'{name1}' == '{name3}': {name1 == name3}")
print(f"'{name1}' < '{name2}': {name1 < name2}")  # Alphabetical order
print(f"'{name1}' > '{name2}': {name1 > name2}")

# Comparing different data types (be careful!)
print(f"10 == '10': {10 == '10'}")  # False (different types)
print(f"10 == 10.0: {10 == 10.0}")  # True (Python converts)

# ============================================================================
# LOGICAL OPERATORS
# ============================================================================

print("\n=== Logical Operators ===")

# Logical operators work with boolean values
p = True
q = False

print(f"p = {p}, q = {q}")

# AND operator (both conditions must be True)
print(f"p and q: {p and q}")      # False
print(f"p and True: {p and True}")  # True
print(f"q and True: {q and True}")  # False

# OR operator (at least one condition must be True)
print(f"p or q: {p or q}")        # True
print(f"q or False: {q or False}")  # False

# NOT operator (reverses the boolean value)
print(f"not p: {not p}")          # False
print(f"not q: {not q}")          # True

# Combining logical operators
age = 25
has_license = True
print(f"\nAge: {age}, Has License: {has_license}")
print(f"Can drive? {age >= 18 and has_license}")

# Practical example: User authentication
username = "admin"
password = "secret123"
is_active = True

print(f"\nLogin attempt:")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print(f"Account active: {is_active}")

login_successful = (username == "admin" and 
                   password == "secret123" and 
                   is_active)
print(f"Login successful: {login_successful}")

# ============================================================================
# ASSIGNMENT OPERATORS
# ============================================================================

print("\n=== Assignment Operators ===")

# Basic assignment
score = 100
print(f"Initial score: {score}")

# Compound assignment operators (modify and assign)
score += 10    # Same as: score = score + 10
print(f"After += 10: {score}")

score -= 5     # Same as: score = score - 5
print(f"After -= 5: {score}")

score *= 2     # Same as: score = score * 2
print(f"After *= 2: {score}")

score /= 4     # Same as: score = score / 4
print(f"After /= 4: {score}")

score //= 3    # Same as: score = score // 3
print(f"After //= 3: {score}")

score %= 10    # Same as: score = score % 10
print(f"After %= 10: {score}")

score **= 2    # Same as: score = score ** 2
print(f"After **= 2: {score}")

# Multiple assignment
print("\n--- Multiple Assignment ---")
a = b = c = 10  # All variables get the same value
print(f"a = {a}, b = {b}, c = {c}")

# Tuple unpacking (parallel assignment)
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Swapping variables
print(f"Before swap: x = {x}, y = {y}")
x, y = y, x  # Elegant way to swap in Python
print(f"After swap: x = {x}, y = {y}")

# ============================================================================
# MEMBERSHIP OPERATORS
# ============================================================================

print("\n=== Membership Operators ===")

# 'in' and 'not in' operators test membership in sequences
text = "Python Programming"
numbers = [1, 2, 3, 4, 5]
vowels = "aeiou"

print(f"Text: '{text}'")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'java' in text: {'java' in text}")  # Case sensitive

print(f"\nNumbers: {numbers}")
print(f"3 in numbers: {3 in numbers}")
print(f"10 in numbers: {10 in numbers}")
print(f"6 not in numbers: {6 not in numbers}")

# Checking for vowels
letter = 'a'
print(f"\nIs '{letter}' a vowel? {letter.lower() in vowels}")

# ============================================================================
# IDENTITY OPERATORS
# ============================================================================

print("\n=== Identity Operators ===")

# 'is' and 'is not' test if two variables refer to the same object
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

print(f"list1 == list2: {list1 == list2}")    # True (same content)
print(f"list1 is list2: {list1 is list2}")    # False (different objects)
print(f"list1 is list3: {list1 is list3}")    # True (same object)

# Special case with small integers and strings (Python optimization)
a = 100
b = 100
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # True (Python caches small integers)

a = 1000
b = 1000
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # May be False (larger integers not always cached)

# Use 'is' with None, True, False
value = None
print(f"value is None: {value is None}")  # Preferred way to check for None

# ============================================================================
# BITWISE OPERATORS (Advanced)
# ============================================================================

print("\n=== Bitwise Operators ===")

# Bitwise operators work on binary representations of numbers
a = 12  # Binary: 1100
b = 7   # Binary: 0111

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

print(f"a & b (AND): {a & b} (binary: {bin(a & b)})")      # 4 (0100)
print(f"a | b (OR): {a | b} (binary: {bin(a | b)})")       # 15 (1111)
print(f"a ^ b (XOR): {a ^ b} (binary: {bin(a ^ b)})")      # 11 (1011)
print(f"~a (NOT): {~a} (binary: {bin(~a)})")               # -13
print(f"a << 2 (Left Shift): {a << 2} (binary: {bin(a << 2)})")  # 48 (110000)
print(f"a >> 2 (Right Shift): {a >> 2} (binary: {bin(a >> 2)})")  # 3 (11)

# ============================================================================
# OPERATOR PRECEDENCE
# ============================================================================

print("\n=== Operator Precedence ===")

# Python follows mathematical order of operations (PEMDAS/BODMAS)
result1 = 2 + 3 * 4      # Multiplication first: 2 + 12 = 14
result2 = (2 + 3) * 4    # Parentheses first: 5 * 4 = 20

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

# Complex expression
result = 10 + 5 * 2 ** 2 - 8 / 4
# Step by step: 10 + 5 * 4 - 2 = 10 + 20 - 2 = 28
print(f"10 + 5 * 2 ** 2 - 8 / 4 = {result}")

# Logical operators precedence
age = 25
income = 50000
has_job = True

# Parentheses make the intention clear
eligible = (age >= 21) and (income > 30000 or has_job)
print(f"Loan eligible: {eligible}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: Grade calculator
score = 85
grade = (
    'A' if score >= 90 else
    'B' if score >= 80 else
    'C' if score >= 70 else
    'D' if score >= 60 else
    'F'
)
print(f"Score: {score}, Grade: {grade}")

# Example 2: Leap year checker
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"Year {year} is leap year: {is_leap}")

# Example 3: Password strength checker
password = "MySecure123!"
length_ok = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)

strength = "Strong" if all([length_ok, has_upper, has_lower, has_digit, has_special]) else "Weak"
print(f"Password: {'*' * len(password)}")
print(f"Strength: {strength}")

# Example 4: BMI calculator with category
weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)
category = (
    "Underweight" if bmi < 18.5 else
    "Normal weight" if bmi < 25 else
    "Overweight" if bmi < 30 else
    "Obese"
)

print(f"BMI: {bmi:.1f}, Category: {category}")

# Example 5: Time conversion
total_seconds = 7385
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")

# ============================================================================
# COMMON MISTAKES AND BEST PRACTICES
# ============================================================================

print("\n=== Common Mistakes to Avoid ===")

# Mistake 1: Using assignment (=) instead of comparison (==)
x = 5
# if x = 10:  # This would cause a SyntaxError
if x == 10:   # Correct comparison
    print("x is 10")
else:
    print("x is not 10")

# Mistake 2: Comparing floating point numbers directly
a = 0.1 + 0.2
b = 0.3
print(f"0.1 + 0.2 = {a}")
print(f"a == 0.3: {a == b}")  # Might be False due to floating point precision

# Better way to compare floats
tolerance = 1e-9
print(f"abs(a - b) < tolerance: {abs(a - b) < tolerance}")

# Mistake 3: Chaining comparisons incorrectly
age = 25
# Wrong: if 18 <= age <= 65:  # This is actually correct in Python!
# But in other languages, you might need: age >= 18 and age <= 65

print(f"Age {age} is working age: {18 <= age <= 65}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. Arithmetic Operators:
   - / always returns float, // returns integer division
   - % (modulus) gives remainder, useful for checking even/odd
   - ** is exponentiation

2. Comparison Operators:
   - Return boolean values (True/False)
   - Can chain comparisons: 18 <= age <= 65
   - String comparisons are lexicographic (alphabetical)

3. Logical Operators:
   - and, or, not
   - Short-circuit evaluation (stops when result is determined)
   - Useful for complex conditions

4. Assignment Operators:
   - Compound operators (+=, -=, etc.) modify and assign
   - Multiple assignment: a = b = c = 10
   - Tuple unpacking: x, y = 1, 2

5. Membership Operators:
   - in and not in test membership in sequences
   - Case sensitive for strings

6. Identity Operators:
   - is and is not test object identity, not equality
   - Use 'is' with None, True, False
   - Use == for value comparison, is for identity

7. Operator Precedence:
   - Follows mathematical order (PEMDAS)
   - Use parentheses to make intentions clear
   - When in doubt, use parentheses

Best Practices:
- Use parentheses to clarify complex expressions
- Be careful with floating point comparisons
- Use 'is' for None checks, '==' for value comparisons
- Use meaningful variable names in expressions
- Break complex expressions into smaller parts
"""

print("\n" + "="*50)
print("END OF MODULE 01 - OPERATORS AND EXPRESSIONS")
print("="*50)
