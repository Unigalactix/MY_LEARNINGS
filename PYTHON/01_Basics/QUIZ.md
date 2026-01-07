# Python Basics Quiz 📝

**Topic**: Variables and Data Types  
**Difficulty**: ⭐ Beginner  
**Time**: ~20 minutes

**Instructions**: 
- Try to answer all questions before checking the answers
- Use the explanations to understand concepts you missed
- Retake the quiz after reviewing materials if needed

---

## Section 1: Multiple Choice Questions

### Question 1 (⭐ Beginner)
**Which of the following is the correct way to create a variable in Python?**

A) `var x = 10`  
B) `int x = 10`  
C) `x = 10`  
D) `let x = 10`

<details>
<summary>Click to reveal answer</summary>

**Answer: C**

**Explanation**: 
Python uses dynamic typing, meaning you don't need to declare the type of a variable. You simply assign a value to a variable name using the `=` operator. Options A and D are JavaScript syntax, and option B is similar to statically-typed languages like C or Java, which is not required in Python.

**Example**:
```python
x = 10          # Integer
name = "John"   # String
is_valid = True # Boolean
```

</details>

---

### Question 2 (⭐ Beginner)
**What is the output of `type(3.14)`?**

A) `<class 'int'>`  
B) `<class 'float'>`  
C) `<class 'double'>`  
D) `<class 'decimal'>`

<details>
<summary>Click to reveal answer</summary>

**Answer: B**

**Explanation**: 
In Python, any number with a decimal point is automatically treated as a `float` (floating-point number). Python doesn't have a `double` type like some other languages - it uses `float` for all decimal numbers. The `decimal` type exists in Python but requires importing from the `decimal` module.

**Example**:
```python
print(type(3.14))    # <class 'float'>
print(type(3))       # <class 'int'>
print(type("3.14"))  # <class 'str'>
```

</details>

---

### Question 3 (⭐⭐ Intermediate)
**What will be the output of the following code?**

```python
x = "5"
y = 3
result = x * y
print(result)
```

A) `15`  
B) `"15"`  
C) `"555"`  
D) `Error`

<details>
<summary>Click to reveal answer</summary>

**Answer: C**

**Explanation**: 
When you multiply a string by an integer in Python, the string is repeated that many times. This is called string repetition. The string `"5"` is repeated 3 times, resulting in `"555"`.

**Example**:
```python
print("Hello" * 3)    # "HelloHelloHello"
print("*" * 5)        # "*****"
print("5" * 3)        # "555"

# To get numeric multiplication, convert the string to int:
x = int("5")
y = 3
print(x * y)          # 15
```

</details>

---

### Question 4 (⭐⭐ Intermediate)
**Which of the following variable names is NOT valid in Python?**

A) `_private_var`  
B) `user_2024`  
C) `2nd_user`  
D) `user_name`

<details>
<summary>Click to reveal answer</summary>

**Answer: C**

**Explanation**: 
Python variable names cannot start with a number. They must begin with a letter (a-z, A-Z) or an underscore (_). After the first character, they can contain letters, numbers, and underscores.

**Valid naming rules**:
- ✅ Can start with letter or underscore
- ✅ Can contain letters, numbers, and underscores
- ✅ Case-sensitive (`name` and `Name` are different)
- ❌ Cannot start with a number
- ❌ Cannot contain spaces or special characters (except _)
- ❌ Cannot be a Python keyword (if, for, while, etc.)

**Examples**:
```python
# Valid
user_name = "John"
_private = 42
user2024 = "data"
UserName = "Jane"

# Invalid
2nd_user = "data"    # SyntaxError
user-name = "John"   # SyntaxError (hyphen not allowed)
user name = "Jane"   # SyntaxError (space not allowed)
```

</details>

---

## Section 2: True/False Questions

### Question 5 (⭐ Beginner)
**True or False**: In Python, you must declare the data type of a variable before using it.

- [ ] True
- [ ] False

<details>
<summary>Click to reveal answer</summary>

**Answer: False**

**Explanation**: 
Python is a dynamically-typed language, meaning the type is determined automatically at runtime based on the value assigned. You don't need to declare types explicitly. However, Python 3.5+ does support optional type hints for documentation and static analysis purposes, but they're not enforced at runtime.

**Examples**:
```python
# No type declaration needed
x = 10          # x is automatically an int
x = "hello"     # x is now automatically a str
x = 3.14        # x is now automatically a float

# Optional type hints (Python 3.5+)
name: str = "John"
age: int = 25
# These hints are not enforced, just suggestions for developers and tools
```

</details>

---

### Question 6 (⭐⭐ Intermediate)
**True or False**: `bool(0)` returns `True` in Python.

- [ ] True
- [ ] False

<details>
<summary>Click to reveal answer</summary>

**Answer: False**

**Explanation**: 
In Python, `0` is considered a "falsy" value. When converted to a boolean, it returns `False`. Other falsy values include: `None`, `False`, `""` (empty string), `[]` (empty list), `{}` (empty dict), and `0.0`.

**Falsy vs Truthy**:
```python
# Falsy values (evaluate to False)
bool(0)        # False
bool(0.0)      # False
bool("")       # False
bool([])       # False
bool({})       # False
bool(None)     # False
bool(False)    # False

# Truthy values (evaluate to True)
bool(1)        # True
bool(-1)       # True
bool("hello")  # True
bool([1])      # True
bool({"a": 1}) # True
bool(True)     # True
```

**Practical use**:
```python
user_input = input("Enter something: ")
if user_input:  # Automatically checks if not empty
    print("You entered:", user_input)
else:
    print("You didn't enter anything")
```

</details>

---

## Section 3: Fill in the Blank

### Question 7 (⭐ Beginner)
**Complete the code to convert the string "123" to an integer:**

```python
text = "123"
number = ________(text)
print(number + 5)  # Should output: 128
```

<details>
<summary>Click to reveal answer</summary>

**Answer**: 
```python
text = "123"
number = int(text)
print(number + 5)  # Output: 128
```

**Explanation**: 
The `int()` function converts a string to an integer. This is called type casting or type conversion.

**Common type conversions**:
```python
# String to number
int("123")      # 123 (integer)
float("3.14")   # 3.14 (float)

# Number to string
str(123)        # "123"
str(3.14)       # "3.14"

# To boolean
bool(1)         # True
bool(0)         # False

# Float to int (truncates decimal)
int(3.7)        # 3
int(3.2)        # 3
```

**Watch out for**:
```python
int("hello")    # ValueError: invalid literal
int("3.14")     # ValueError: invalid literal (use float() first)
```

</details>

---

### Question 8 (⭐⭐ Intermediate)
**Complete the f-string to display "Hello, John! You are 25 years old.":**

```python
name = "John"
age = 25
message = ________
print(message)
```

<details>
<summary>Click to reveal answer</summary>

**Answer**: 
```python
name = "John"
age = 25
message = f"Hello, {name}! You are {age} years old."
print(message)
```

**Explanation**: 
F-strings (formatted string literals) are the modern way to format strings in Python (3.6+). You prefix the string with `f` and use curly braces `{}` to embed expressions.

**F-string features**:
```python
name = "Alice"
age = 30
price = 29.99

# Basic usage
print(f"Hello, {name}")

# Expressions inside braces
print(f"{name} will be {age + 1} next year")

# Formatting numbers
print(f"Price: ${price:.2f}")  # Price: $29.99

# Calling functions
print(f"Uppercase: {name.upper()}")  # Uppercase: ALICE

# Multiple variables
print(f"{name} is {age} years old")
```

**Other formatting methods** (older, still valid):
```python
# %-formatting (old style)
print("Hello, %s" % name)

# .format() method
print("Hello, {}".format(name))

# But f-strings are preferred for readability
```

</details>

---

## Section 4: Code Output Prediction

### Question 9 (⭐⭐ Intermediate)
**What will be the output of the following code?**

```python
x = 10
y = 3
print(x / y)
print(x // y)
print(x % y)
```

A) `3.333333333333333`, `3`, `1`  
B) `3`, `3`, `1`  
C) `3.33`, `3.0`, `1.0`  
D) Error

<details>
<summary>Click to reveal answer</summary>

**Answer: A**

**Explanation**: 
- `/` is regular division and always returns a float
- `//` is floor division (rounds down to nearest integer)
- `%` is modulus (remainder after division)

**Detailed breakdown**:
```python
x = 10
y = 3

# Regular division (always returns float)
print(x / y)   # 3.333333333333333
print(10 / 2)  # 5.0 (still a float!)

# Floor division (rounds down)
print(x // y)  # 3
print(10 // 3) # 3
print(-10 // 3)# -4 (rounds toward negative infinity)

# Modulus (remainder)
print(x % y)   # 1 (because 10 = 3*3 + 1)
print(10 % 3)  # 1
print(11 % 3)  # 2
print(12 % 3)  # 0
```

**Practical uses**:
```python
# Check if even/odd
number = 17
if number % 2 == 0:
    print("Even")
else:
    print("Odd")  # This will print

# Get last digit
number = 12345
last_digit = number % 10  # 5

# Convert minutes to hours and minutes
total_minutes = 150
hours = total_minutes // 60    # 2
minutes = total_minutes % 60   # 30
print(f"{hours}h {minutes}m")  # 2h 30m
```

</details>

---

### Question 10 (⭐⭐⭐ Advanced)
**What will be the output?**

```python
x = 0.1 + 0.2
print(x)
print(x == 0.3)
```

A) `0.3`, `True`  
B) `0.30000000000000004`, `False`  
C) `0.3`, `False`  
D) Error

<details>
<summary>Click to reveal answer</summary>

**Answer: B**

**Explanation**: 
This demonstrates floating-point precision issues. Computers represent decimal numbers in binary, which can't perfectly represent some decimal fractions. This is not a Python bug - it's a fundamental limitation of how computers store floating-point numbers (IEEE 754 standard).

**The floating-point problem**:
```python
print(0.1 + 0.2)           # 0.30000000000000004
print(0.1 + 0.2 == 0.3)    # False

# Why does this happen?
# 0.1 in binary is an infinite repeating fraction
# Computers can only store finite precision

# More examples
print(0.1 + 0.1 + 0.1)     # 0.30000000000000004
print(1.0 - 0.9)            # 0.09999999999999998
```

**Solutions**:

1. **Round for display**:
```python
x = 0.1 + 0.2
print(round(x, 2))  # 0.3
```

2. **Use decimal module for precision**:
```python
from decimal import Decimal

x = Decimal('0.1') + Decimal('0.2')
print(x)                # 0.3
print(x == Decimal('0.3'))  # True
```

3. **Use math.isclose() for comparisons**:
```python
import math

x = 0.1 + 0.2
print(math.isclose(x, 0.3))  # True
```

4. **Use epsilon for comparisons**:
```python
x = 0.1 + 0.2
epsilon = 1e-9
print(abs(x - 0.3) < epsilon)  # True
```

**When to use what**:
- Regular float: Most cases, calculations that don't need perfect precision
- Decimal: Financial calculations, when precision is critical
- isclose(): When comparing float values for equality

</details>

---

## Scoring Guide

**Total Questions**: 10

- **9-10 correct (90-100%)**: Excellent! You've mastered Python basics! 🎉
- **7-8 correct (70-89%)**: Good job! Review the concepts you missed. 👍
- **5-6 correct (50-69%)**: You're getting there! More practice needed. 📚
- **0-4 correct (0-49%)**: Keep learning! Go through the basics again. 💪

---

## What's Next?

### If you scored well (80%+):
- ✅ Move to `02_input_output.py`
- ✅ Try the coding challenges below
- ✅ Experiment with type conversions

### If you need more practice (below 80%):
- 📖 Review `01_variables_and_data_types.py`
- 💻 Run code examples in a Python interpreter
- 🔄 Retake this quiz
- 💬 Practice with interactive Python tutorials

---

## Practice Exercises

### Exercise 1: Variable Swap
Write code to swap the values of two variables without using a third variable.

<details>
<summary>Click for solution</summary>

```python
# Method 1: Using tuple unpacking (Pythonic way)
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5

# Method 2: Using arithmetic
a = 5
b = 10
a = a + b   # a = 15
b = a - b   # b = 5
a = a - b   # a = 10
print(a, b)  # 10 5
```

</details>

### Exercise 2: Type Detective
Write a function that takes a variable and prints its type and value in a formatted way.

<details>
<summary>Click for solution</summary>

```python
def type_detective(var):
    """Print type and value information about a variable"""
    var_type = type(var).__name__
    print(f"Type: {var_type}")
    print(f"Value: {var}")
    print(f"Repr: {repr(var)}")
    
# Test it
type_detective(42)
type_detective("hello")
type_detective(3.14)
type_detective(True)
type_detective([1, 2, 3])
```

</details>

### Exercise 3: Safe Type Converter
Create a function that safely converts a string to an integer, returning a default value if conversion fails.

<details>
<summary>Click for solution</summary>

```python
def safe_int(value, default=0):
    """
    Safely convert value to integer.
    Return default if conversion fails.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Test it
print(safe_int("123"))      # 123
print(safe_int("hello"))    # 0
print(safe_int("45", 10))   # 45
print(safe_int("bad", 10))  # 10
print(safe_int(None))       # 0
```

</details>

---

## Related Materials

- [01_variables_and_data_types.py](./01_variables_and_data_types.py) - Complete lesson
- [02_input_output.py](./02_input_output.py) - Next lesson
- [PYTHON/CHEAT_SHEET.md](../CHEAT_SHEET.md) - Quick reference
- [PYTHON/LEARNING_GUIDE.md](../LEARNING_GUIDE.md) - Study plan

---

**Keep practicing!** 🐍🚀
