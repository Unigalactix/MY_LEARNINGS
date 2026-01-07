# Python Basics - Coding Challenges 💻

**Topic**: Variables, Data Types, and Operators  
**Total Challenges**: 8  
**Estimated Time**: 2-3 hours

**Instructions**: 
- Try to solve challenges independently before checking solutions
- Test your code with the provided test cases
- Run your code to verify it works correctly

---

## Challenge #1: Temperature Converter ⭐

**Difficulty**: Beginner  
**Time**: 10-15 minutes  
**Concepts**: Variables, arithmetic operations, f-strings

### Problem Statement

Create a program that converts temperature between Celsius and Fahrenheit. The program should:
1. Convert 25°C to Fahrenheit
2. Convert 77°F to Celsius
3. Display results with 2 decimal places

**Formulas**:
- Fahrenheit = (Celsius × 9/5) + 32
- Celsius = (Fahrenheit - 32) × 5/9

### Requirements

- ✅ Define variables for temperatures
- ✅ Perform conversions using formulas
- ✅ Use f-strings for output with 2 decimal places
- ✅ Include unit symbols (°C, °F)

### Test Cases

```python
# Test Case 1
celsius = 25
# Expected output: "25.00°C = 77.00°F"

# Test Case 2
fahrenheit = 77
# Expected output: "77.00°F = 25.00°C"

# Test Case 3
celsius = 0
# Expected output: "0.00°C = 32.00°F"

# Test Case 4
fahrenheit = 32
# Expected output: "32.00°F = 0.00°C"
```

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# Temperature Converter

# Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

# Fahrenheit to Celsius
fahrenheit = 77
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")

# Test with freezing point
celsius = 0
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

# Test with freezing point in Fahrenheit
fahrenheit = 32
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
```

**Output**:
```
25.00°C = 77.00°F
77.00°F = 25.00°C
0.00°C = 32.00°F
32.00°F = 0.00°C
```

**Key Concepts**:
- Arithmetic operations with floats
- F-string formatting with :.2f for 2 decimal places
- Using parentheses for proper order of operations

</details>

---

## Challenge #2: Circle Calculator ⭐

**Difficulty**: Beginner  
**Time**: 15 minutes  
**Concepts**: Constants, variables, arithmetic, formatting

### Problem Statement

Create a program that calculates the area and circumference of a circle given its radius.

**Formulas**:
- Area = π × r²
- Circumference = 2 × π × r

Use `PI = 3.14159` as a constant.

### Requirements

- ✅ Define PI as a constant (uppercase)
- ✅ Calculate area and circumference for multiple radii
- ✅ Format output to 2 decimal places
- ✅ Test with radius = 5, 10, and 7.5

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# Circle Calculator

# Define constant
PI = 3.14159

# Test Case 1: radius = 5
radius = 5
area = PI * radius ** 2
circumference = 2 * PI * radius
print(f"Radius: {radius}")
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")
print()

# Test Case 2: radius = 10
radius = 10
area = PI * radius ** 2
circumference = 2 * PI * radius
print(f"Radius: {radius}")
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")
print()

# Test Case 3: radius = 7.5
radius = 7.5
area = PI * radius ** 2
circumference = 2 * PI * radius
print(f"Radius: {radius}")
print(f"Area: {area:.2f} square units")
print(f"Circumference: {circumference:.2f} units")
```

**Better solution with function** (preview of functions):
```python
PI = 3.14159

def circle_stats(radius):
    """Calculate and display circle statistics"""
    area = PI * radius ** 2
    circumference = 2 * PI * radius
    print(f"Radius: {radius}")
    print(f"Area: {area:.2f} square units")
    print(f"Circumference: {circumference:.2f} units")
    print()

# Test all cases
circle_stats(5)
circle_stats(10)
circle_stats(7.5)
```

</details>

---

## Challenge #3: String Manipulator ⭐⭐

**Difficulty**: Intermediate  
**Time**: 20 minutes  
**Concepts**: String operations, type conversion, string methods

### Problem Statement

Create a program that takes a user's full name and performs various string manipulations:
1. Display the name in uppercase
2. Display the name in lowercase
3. Display the number of characters (including spaces)
4. Display initials (first letter of each name)
5. Display the name in reverse

### Example

```
Input: "John Michael Smith"
Output:
Uppercase: JOHN MICHAEL SMITH
Lowercase: john michael smith
Length: 18 characters
Initials: JMS
Reversed: htimS leahciM nhoJ
```

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# String Manipulator

# Test with a name
full_name = "John Michael Smith"

# 1. Uppercase
uppercase_name = full_name.upper()
print(f"Uppercase: {uppercase_name}")

# 2. Lowercase
lowercase_name = full_name.lower()
print(f"Lowercase: {lowercase_name}")

# 3. Length
name_length = len(full_name)
print(f"Length: {name_length} characters")

# 4. Initials
names = full_name.split()  # Split by spaces
initials = ""
for name in names:
    initials += name[0]  # Take first character of each name
print(f"Initials: {initials}")

# Alternative for initials (more Pythonic)
initials_v2 = "".join([name[0] for name in full_name.split()])
print(f"Initials (v2): {initials_v2}")

# 5. Reversed
reversed_name = full_name[::-1]
print(f"Reversed: {reversed_name}")

# Bonus: Title case
print(f"Title Case: {full_name.title()}")

# Bonus: Count spaces
space_count = full_name.count(" ")
print(f"Number of spaces: {space_count}")
```

**Key Concepts**:
- String methods: `.upper()`, `.lower()`, `.split()`, `.title()`, `.count()`
- String slicing: `[::-1]` for reversal
- String indexing: `name[0]` for first character
- List comprehension (bonus)

</details>

---

## Challenge #4: Type Detective ⭐⭐

**Difficulty**: Intermediate  
**Time**: 15 minutes  
**Concepts**: Type checking, type conversion, conditionals

### Problem Statement

Create a program that analyzes different variables and reports:
1. The type of each variable
2. Whether it's truthy or falsy
3. Its length (if applicable)

Test with these values: `42`, `"hello"`, `""`, `0`, `None`, `[]`, `[1, 2, 3]`, `True`

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# Type Detective

def analyze_variable(var, name="variable"):
    """Analyze a variable and print its properties"""
    print(f"\nAnalyzing: {name}")
    print(f"Value: {repr(var)}")
    print(f"Type: {type(var).__name__}")
    print(f"Truthy: {bool(var)}")
    
    # Check if it has a length
    try:
        length = len(var)
        print(f"Length: {length}")
    except TypeError:
        print("Length: N/A (no length)")
    
    print("-" * 40)

# Test with different values
analyze_variable(42, "number")
analyze_variable("hello", "string")
analyze_variable("", "empty_string")
analyze_variable(0, "zero")
analyze_variable(None, "none_value")
analyze_variable([], "empty_list")
analyze_variable([1, 2, 3], "list")
analyze_variable(True, "boolean")

# Additional tests
analyze_variable(3.14, "float")
analyze_variable({"key": "value"}, "dictionary")
```

**Expected Output** (partial):
```
Analyzing: number
Value: 42
Type: int
Truthy: True
Length: N/A (no length)
----------------------------------------

Analyzing: string
Value: 'hello'
Type: str
Truthy: True
Length: 5
----------------------------------------

Analyzing: empty_string
Value: ''
Type: str
Truthy: False
Length: 0
----------------------------------------
```

</details>

---

## Challenge #5: Math Operations Practice ⭐⭐

**Difficulty**: Intermediate  
**Time**: 20 minutes  
**Concepts**: All arithmetic operators, operator precedence

### Problem Statement

Given two numbers, calculate and display:
1. Sum
2. Difference
3. Product
4. Regular division (float result)
5. Floor division (integer result)
6. Modulus (remainder)
7. Power (first number to the power of second)

Test with: (17, 5) and (100, 7)

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# Math Operations Practice

def math_operations(a, b):
    """Perform all basic math operations on two numbers"""
    print(f"\nMath Operations: {a} and {b}")
    print("=" * 40)
    
    # Sum
    print(f"{a} + {b} = {a + b}")
    
    # Difference
    print(f"{a} - {b} = {a - b}")
    
    # Product
    print(f"{a} × {b} = {a * b}")
    
    # Regular division
    print(f"{a} ÷ {b} = {a / b:.4f}")
    
    # Floor division
    print(f"{a} // {b} = {a // b}")
    
    # Modulus
    print(f"{a} % {b} = {a % b}")
    
    # Power
    print(f"{a} ** {b} = {a ** b}")
    
    # Bonus: Show relationship between //, % and regular division
    quotient = a // b
    remainder = a % b
    check = quotient * b + remainder
    print(f"\nVerification: {quotient} × {b} + {remainder} = {check}")
    print("=" * 40)

# Test cases
math_operations(17, 5)
math_operations(100, 7)

# Additional interesting cases
math_operations(10, 3)
math_operations(50, 6)
```

**Key Learning**:
- Floor division rounds DOWN to nearest integer
- Modulus gives remainder
- Relationship: `a = (a // b) * b + (a % b)`

</details>

---

## Challenge #6: Variable Naming Convention Checker ⭐⭐⭐

**Difficulty**: Advanced  
**Time**: 30 minutes  
**Concepts**: Strings, conditionals, string methods, validation

### Problem Statement

Create a program that checks if a variable name follows Python naming conventions:
- Starts with letter or underscore
- Contains only letters, numbers, and underscores
- Is not a Python keyword

Test with: `"user_name"`, `"2nd_user"`, `"_private"`, `"if"`, `"userName"`, `"user-name"`

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# Variable Naming Convention Checker

import keyword  # Built-in Python module - no installation needed!

def check_variable_name(name):
    """
    Check if a string is a valid Python variable name.
    Returns True if valid, False otherwise, with reason.
    """
    print(f"\nChecking: '{name}'")
    
    # Check if empty
    if not name:
        print("❌ Invalid: Empty name")
        return False
    
    # Check if starts with digit
    if name[0].isdigit():
        print("❌ Invalid: Cannot start with a digit")
        return False
    
    # Check if Python keyword
    if keyword.iskeyword(name):
        print("❌ Invalid: Python keyword")
        return False
    
    # Check for valid characters
    valid_chars = True
    for char in name:
        if not (char.isalnum() or char == '_'):
            print(f"❌ Invalid: Contains invalid character '{char}'")
            return False
    
    # If we got here, it's valid
    print("✅ Valid Python variable name")
    
    # Check naming convention recommendations
    if name.isupper():
        print("   💡 Suggestion: Looks like a CONSTANT (all uppercase)")
    elif name[0].isupper():
        print("   💡 Suggestion: Looks like a ClassName (PascalCase)")
    elif '_' not in name and any(c.isupper() for c in name):
        print("   💡 Suggestion: camelCase detected. Python prefers snake_case")
    elif name.startswith('_'):
        if name.startswith('__'):
            print("   💡 Info: Double underscore prefix (name mangling)")
        else:
            print("   💡 Info: Single underscore prefix (internal/private)")
    else:
        print("   ✨ Follows PEP 8 snake_case convention")
    
    return True

# Test cases
test_names = [
    "user_name",      # Valid, snake_case
    "2nd_user",       # Invalid, starts with digit
    "_private",       # Valid, private convention
    "if",             # Invalid, keyword
    "userName",       # Valid but camelCase
    "user-name",      # Invalid, contains hyphen
    "MAX_SIZE",       # Valid, constant convention
    "UserClass",      # Valid, class convention
    "__init__",       # Valid, special method
    "my_var_2",       # Valid
    "for",            # Invalid, keyword
    "print",          # Valid (shadowing built-in, but allowed)
]

print("Python Variable Name Checker")
print("=" * 50)

for name in test_names:
    check_variable_name(name)

# List all Python keywords
print("\n" + "=" * 50)
print("Python Keywords:")
print(", ".join(keyword.kwlist))
```

**Key Concepts**:
- String validation methods: `.isdigit()`, `.isalnum()`, `.isupper()`
- Python `keyword` module
- PEP 8 naming conventions
- Input validation

</details>

---

## Challenge #7: Number System Converter ⭐⭐⭐

**Difficulty**: Advanced  
**Time**: 30 minutes  
**Concepts**: Type conversion, string formatting, number bases

### Problem Statement

Create a program that converts a decimal number to binary, octal, and hexadecimal, and displays:
1. The number in each base
2. The number of digits in each representation
3. Each representation with proper prefix (0b, 0o, 0x)

Test with: 255, 42, 1000

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# Number System Converter

def number_system_converter(decimal_num):
    """
    Convert a decimal number to binary, octal, and hexadecimal.
    Display with formatting and analysis.
    """
    print(f"\n{'='*60}")
    print(f"Converting: {decimal_num} (Decimal)")
    print('='*60)
    
    # Binary conversion
    binary = bin(decimal_num)
    binary_no_prefix = binary[2:]  # Remove '0b' prefix
    print(f"Binary:      {binary:>20}  ({len(binary_no_prefix)} digits)")
    
    # Octal conversion
    octal = oct(decimal_num)
    octal_no_prefix = octal[2:]  # Remove '0o' prefix
    print(f"Octal:       {octal:>20}  ({len(octal_no_prefix)} digits)")
    
    # Hexadecimal conversion (lowercase)
    hexadecimal = hex(decimal_num)
    hex_no_prefix = hexadecimal[2:]  # Remove '0x' prefix
    print(f"Hexadecimal: {hexadecimal:>20}  ({len(hex_no_prefix)} digits)")
    
    # Hexadecimal uppercase
    hex_upper = hexadecimal.upper()
    print(f"Hex (upper): {hex_upper:>20}  ({len(hex_no_prefix)} digits)")
    
    # Without prefixes
    print(f"\nWithout prefixes:")
    print(f"Binary:      {binary_no_prefix:>20}")
    print(f"Octal:       {octal_no_prefix:>20}")
    print(f"Hexadecimal: {hex_no_prefix:>20}")
    
    # Verification: convert back to decimal
    print(f"\nVerification (convert back to decimal):")
    print(f"Binary {binary} → {int(binary, 2)}")
    print(f"Octal {octal} → {int(octal, 8)}")
    print(f"Hex {hexadecimal} → {int(hexadecimal, 16)}")

# Test cases
test_numbers = [255, 42, 1000, 16, 8, 65535]

print("Number System Converter")
print("Decimal → Binary, Octal, Hexadecimal")

for num in test_numbers:
    number_system_converter(num)

# Bonus: Formatted table for multiple numbers
print("\n" + "="*60)
print("Summary Table")
print("="*60)
print(f"{'Decimal':<10} {'Binary':<20} {'Octal':<10} {'Hex':<10}")
print("-"*60)

for num in test_numbers:
    binary = bin(num)
    octal = oct(num)
    hexadecimal = hex(num)
    print(f"{num:<10} {binary:<20} {octal:<10} {hexadecimal:<10}")
```

**Output Example** (partial):
```
============================================================
Converting: 255 (Decimal)
============================================================
Binary:                 0b11111111  (8 digits)
Octal:                       0o377  (3 digits)
Hexadecimal:                  0xff  (2 digits)
Hex (upper):                  0xFF  (2 digits)
```

**Key Concepts**:
- Built-in functions: `bin()`, `oct()`, `hex()`
- String slicing to remove prefixes
- `int()` with base parameter for conversion back
- String formatting and alignment

</details>

---

## Challenge #8: Data Type Playground (Project) 🎯

**Difficulty**: Project Level  
**Time**: 45-60 minutes  
**Concepts**: All basic concepts integrated

### Problem Statement

Create an interactive data type exploration program that:
1. Takes user input
2. Attempts to identify the best data type
3. Performs relevant operations based on type
4. Displays detailed information

### Features to Implement

1. **Input Analysis**: Determine if input looks like a number, boolean, or string
2. **Type Conversion**: Try to convert to appropriate type
3. **Operations**: Perform type-specific operations
4. **Display**: Show comprehensive information

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# Data Type Playground

def analyze_and_process(user_input):
    """
    Analyze user input and process based on detected type.
    """
    print("\n" + "="*60)
    print(f"Analyzing input: '{user_input}'")
    print("="*60)
    
    # Original type
    print(f"Original type: {type(user_input).__name__}")
    print(f"Original value: {repr(user_input)}")
    
    # Try to identify the best type
    print("\n--- Type Detection ---")
    
    # Check if it's a boolean word
    if user_input.lower() in ['true', 'false']:
        print("✓ Detected: Boolean")
        value = user_input.lower() == 'true'
        print(f"Converted to: {value} ({type(value).__name__})")
        print(f"Negation: {not value}")
        
    # Check if it's an integer
    elif user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        print("✓ Detected: Integer")
        value = int(user_input)
        print(f"Converted to: {value} ({type(value).__name__})")
        print(f"Square: {value ** 2}")
        print(f"Even: {value % 2 == 0}")
        print(f"Absolute: {abs(value)}")
        
    # Check if it's a float
    elif '.' in user_input:
        try:
            value = float(user_input)
            print("✓ Detected: Float")
            print(f"Converted to: {value} ({type(value).__name__})")
            print(f"Rounded: {round(value)}")
            print(f"Rounded (2 decimals): {round(value, 2)}")
            print(f"Integer part: {int(value)}")
        except ValueError:
            print("✓ Detected: String (contains . but not a number)")
            value = user_input
            string_operations(value)
    
    # It's a string
    else:
        print("✓ Detected: String")
        value = user_input
        string_operations(value)
    
    # Truthy/Falsy check
    print(f"\nTruthy value: {bool(value)}")

def string_operations(text):
    """Perform string-specific operations"""
    print(f"Length: {len(text)}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Title case: {text.title()}")
    print(f"Reversed: {text[::-1]}")
    print(f"Character count: {len(text)}")
    print(f"Word count: {len(text.split())}")
    print(f"Contains digits: {any(c.isdigit() for c in text)}")
    print(f"Contains letters: {any(c.isalpha() for c in text)}")

# Interactive version (commented out for non-interactive testing)
"""
def main():
    print("Data Type Playground")
    print("="*60)
    print("Enter values to analyze (type 'quit' to exit)")
    print()
    
    while True:
        user_input = input("Enter a value: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not user_input:
            print("Please enter a value!")
            continue
        
        analyze_and_process(user_input)
"""

# Test with predefined inputs
test_inputs = [
    "42",
    "3.14",
    "Hello World",
    "true",
    "False",
    "-17",
    "123.456",
    "Python3.9",
    ""
]

print("Data Type Playground - Testing Mode")
print("="*60)

for test_input in test_inputs:
    if test_input:  # Skip empty string for this demo
        analyze_and_process(test_input)

# To run interactively, uncomment:
# main()
```

**Key Features**:
- Type detection logic
- Dynamic type conversion
- Type-specific operations
- Comprehensive output
- Error handling (for float conversion)

</details>

---

## Progress Tracking

Use this checklist to track your progress:

- [ ] Challenge #1: Temperature Converter
- [ ] Challenge #2: Circle Calculator
- [ ] Challenge #3: String Manipulator
- [ ] Challenge #4: Type Detective
- [ ] Challenge #5: Math Operations Practice
- [ ] Challenge #6: Variable Naming Checker
- [ ] Challenge #7: Number System Converter
- [ ] Challenge #8: Data Type Playground

---

## Next Steps

After completing these challenges:

1. **Review**: Compare your solutions with provided ones
2. **Optimize**: Can you make your solutions cleaner?
3. **Extend**: Add features to the challenges
4. **Move On**: Progress to `02_input_output.py` lessons and challenges
5. **Build**: Create your own small calculator or conversion tool

---

## Tips for Success

💡 **Test incrementally**: Test each piece of code as you write it  
💡 **Use descriptive names**: Make your code self-documenting  
💡 **Format output nicely**: Good formatting makes output readable  
💡 **Handle edge cases**: Test with unusual inputs  
💡 **Comment your logic**: Future you will thank present you

---

**Happy Coding!** 🐍🚀
