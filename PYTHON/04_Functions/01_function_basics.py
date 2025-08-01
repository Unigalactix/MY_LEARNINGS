"""
04_FUNCTIONS - FUNCTION BASICS
===============================

This module covers Python functions fundamentals:
- Function definition and syntax
- Parameters and arguments
- Return statements
- Local vs global scope
- Documentation strings (docstrings)
- Function best practices

Learning Objectives:
- Master function creation and usage
- Understand function parameters and arguments
- Learn about scope and variable lifetime
- Practice writing clean, reusable functions
"""

# ============================================================================
# BASIC FUNCTION DEFINITION
# ============================================================================

print("=== Basic Function Definition ===")

# Simple function with no parameters
def greet():
    """A simple greeting function."""
    print("Hello, World!")

# Call the function
greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def greet_person_with_title(title, name):
    """Greet a person with their title."""
    print(f"Hello, {title} {name}!")

greet_person_with_title("Dr.", "Smith")
greet_person_with_title("Ms.", "Johnson")

# ============================================================================
# RETURN STATEMENTS
# ============================================================================

print("\n=== Return Statements ===")

# Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result

# Using the returned value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Function with multiple return statements
def classify_number(num):
    """Classify a number as positive, negative, or zero."""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

print(f"15 is {classify_number(15)}")
print(f"-7 is {classify_number(-7)}")
print(f"0 is {classify_number(0)}")

# Function returning multiple values (tuple unpacking)
def get_circle_properties(radius):
    """Calculate circle area and circumference."""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = get_circle_properties(5)
print(f"Circle with radius 5: Area = {area:.2f}, Circumference = {circumference:.2f}")

# Function that returns early
def check_password(password):
    """Validate password and return result."""
    if len(password) < 8:
        return False, "Password too short"
    
    if not any(c.isupper() for c in password):
        return False, "Password needs uppercase letter"
    
    if not any(c.isdigit() for c in password):
        return False, "Password needs a digit"
    
    return True, "Password is valid"

is_valid, message = check_password("MyPass123")
print(f"Password validation: {is_valid}, {message}")

# ============================================================================
# FUNCTION PARAMETERS AND ARGUMENTS
# ============================================================================

print("\n=== Function Parameters and Arguments ===")

# Positional parameters
def create_profile(name, age, city):
    """Create a user profile."""
    return f"Name: {name}, Age: {age}, City: {city}"

profile1 = create_profile("Alice", 25, "New York")
print(profile1)

# Keyword arguments
profile2 = create_profile(city="London", name="Bob", age=30)
print(profile2)

# Default parameter values
def create_user(name, age=18, active=True):
    """Create a user with default values."""
    status = "active" if active else "inactive"
    return f"User: {name}, Age: {age}, Status: {status}"

print(create_user("Charlie"))  # Uses defaults
print(create_user("Diana", 25))  # Overrides age
print(create_user("Eve", 30, False))  # Overrides both

# Mixing positional and keyword arguments
print(create_user("Frank", active=False))  # Positional + keyword

# ============================================================================
# VARIABLE-LENGTH ARGUMENTS
# ============================================================================

print("\n=== Variable-Length Arguments ===")

# *args - Variable number of positional arguments
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for number in numbers:
        total += number
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum of no arguments: {sum_all()}")

# **kwargs - Variable number of keyword arguments
def create_config(**settings):
    """Create configuration from keyword arguments."""
    config = {}
    for key, value in settings.items():
        config[key] = value
    return config

config = create_config(debug=True, timeout=30, retries=3)
print(f"Configuration: {config}")

# Combining all types of parameters
def complex_function(required, default_param="default", *args, **kwargs):
    """Demonstrate all parameter types."""
    print(f"Required: {required}")
    print(f"Default: {default_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print("Complex function call:")
complex_function("value1", "value2", "extra1", "extra2", option1=True, option2=42)

# ============================================================================
# SCOPE AND LIFETIME
# ============================================================================

print("\n=== Scope and Lifetime ===")

# Global variable
global_var = "I'm global"

def demonstrate_scope():
    """Demonstrate variable scope."""
    # Local variable
    local_var = "I'm local"
    
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

demonstrate_scope()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error - local_var not accessible

# Modifying global variables
counter = 0

def increment_counter():
    """Increment global counter."""
    global counter
    counter += 1
    print(f"Counter incremented to: {counter}")

increment_counter()
increment_counter()
print(f"Final counter value: {counter}")

# Local vs global with same name
name = "Global Alice"

def local_name_demo():
    """Demonstrate local variable shadowing global."""
    name = "Local Bob"  # This creates a new local variable
    print(f"Inside function: {name}")

local_name_demo()
print(f"Outside function: {name}")  # Global variable unchanged

# ============================================================================
# DOCSTRINGS AND DOCUMENTATION
# ============================================================================

print("\n=== Function Documentation ===")

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters
    
    Returns:
    float: BMI value
    str: BMI category
    
    Example:
    >>> bmi, category = calculate_bmi(70, 1.75)
    >>> print(f"BMI: {bmi:.1f}, Category: {category}")
    BMI: 22.9, Category: Normal weight
    """
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

# Using the documented function
bmi_value, bmi_category = calculate_bmi(70, 1.75)
print(f"BMI: {bmi_value:.1f}, Category: {bmi_category}")

# Access function documentation
print(f"Function docstring: {calculate_bmi.__doc__}")

# ============================================================================
# FUNCTION AS FIRST-CLASS OBJECTS
# ============================================================================

print("\n=== Functions as First-Class Objects ===")

def square(x):
    """Return the square of x."""
    return x ** 2

def cube(x):
    """Return the cube of x."""
    return x ** 3

# Functions can be assigned to variables
operation = square
print(f"Square of 5: {operation(5)}")

operation = cube
print(f"Cube of 5: {operation(5)}")

# Functions can be stored in data structures
operations = {
    "square": square,
    "cube": cube
}

print(f"Using function from dict - square of 4: {operations['square'](4)}")

# Functions can be passed as arguments
def apply_operation(func, value):
    """Apply a function to a value."""
    return func(value)

result = apply_operation(square, 6)
print(f"Applied square to 6: {result}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convert_temperature(temp, from_unit, to_unit):
    """Convert temperature between units."""
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        return celsius_to_fahrenheit(temp)
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        return fahrenheit_to_celsius(temp)
    else:
        return temp  # Same unit or unsupported conversion

print("Temperature conversions:")
print(f"25°C = {convert_temperature(25, 'celsius', 'fahrenheit'):.1f}°F")
print(f"77°F = {convert_temperature(77, 'fahrenheit', 'celsius'):.1f}°C")

# Example 2: Grade calculator
def calculate_letter_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 97:
        return "A+"
    elif score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 65:
        return "D"
    else:
        return "F"

def calculate_gpa(grades):
    """Calculate GPA from list of letter grades."""
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "F": 0.0
    }
    
    if not grades:
        return 0.0
    
    total_points = sum(grade_points.get(grade, 0.0) for grade in grades)
    return total_points / len(grades)

scores = [95, 87, 92, 78, 88]
letter_grades = [calculate_letter_grade(score) for score in scores]
gpa = calculate_gpa(letter_grades)

print(f"\nGrade calculation:")
for score, letter in zip(scores, letter_grades):
    print(f"Score {score}: Grade {letter}")
print(f"GPA: {gpa:.2f}")

# Example 3: Text analysis
def count_words(text):
    """Count words in text."""
    words = text.split()
    return len(words)

def count_sentences(text):
    """Count sentences in text (approximate)."""
    sentence_endings = text.count('.') + text.count('!') + text.count('?')
    return max(1, sentence_endings)  # At least 1 sentence

def calculate_reading_time(text, words_per_minute=200):
    """Calculate estimated reading time."""
    word_count = count_words(text)
    minutes = word_count / words_per_minute
    return max(1, round(minutes))  # At least 1 minute

def analyze_text(text):
    """Comprehensive text analysis."""
    analysis = {
        "characters": len(text),
        "words": count_words(text),
        "sentences": count_sentences(text),
        "reading_time": calculate_reading_time(text)
    }
    
    if analysis["words"] > 0:
        analysis["avg_word_length"] = sum(len(word.strip('.,!?')) 
                                        for word in text.split()) / analysis["words"]
        analysis["avg_sentence_length"] = analysis["words"] / analysis["sentences"]
    
    return analysis

sample_text = """
Python is a powerful programming language. It is easy to learn and versatile.
Many companies use Python for web development, data science, and automation.
This makes Python a great choice for beginners and experts alike!
"""

analysis = analyze_text(sample_text)
print(f"\nText analysis:")
for key, value in analysis.items():
    if isinstance(value, float):
        print(f"{key.replace('_', ' ').title()}: {value:.1f}")
    else:
        print(f"{key.replace('_', ' ').title()}: {value}")

# ============================================================================
# FUNCTION DESIGN BEST PRACTICES
# ============================================================================

print("\n=== Function Design Best Practices ===")

# Good function: Single responsibility
def validate_email(email):
    """Check if email format is valid."""
    return "@" in email and "." in email

# Good function: Clear parameters and return
def calculate_discount(price, discount_percent):
    """Calculate discounted price."""
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

# Good function: Proper error handling
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

# Example usage
print(f"Email valid: {validate_email('user@example.com')}")
print(f"Discounted price: ${calculate_discount(100, 20):.2f}")
print(f"Safe division: {safe_divide(10, 2)}")
print(f"Safe division by zero: {safe_divide(10, 0)}")

# Function with input validation
def create_rectangle(width, height):
    """Create rectangle with validation."""
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive")
    
    return {
        "width": width,
        "height": height,
        "area": width * height,
        "perimeter": 2 * (width + height)
    }

try:
    rectangle = create_rectangle(5, 3)
    print(f"Rectangle: {rectangle}")
except ValueError as e:
    print(f"Error creating rectangle: {e}")

# ============================================================================
# RECURSION BASICS
# ============================================================================

print("\n=== Recursion Basics ===")

def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. Function Definition:
   - Use 'def' keyword followed by function name and parameters
   - Include docstring for documentation
   - Use meaningful function names (verbs)

2. Parameters and Arguments:
   - Positional parameters: def func(a, b)
   - Default parameters: def func(a, b=10)
   - *args for variable positional arguments
   - **kwargs for variable keyword arguments

3. Return Values:
   - Functions return None by default
   - Use 'return' to send values back
   - Can return multiple values (tuple)
   - Early returns for validation/error cases

4. Scope:
   - Local variables exist only within function
   - Global variables accessible from anywhere
   - Use 'global' keyword to modify global variables
   - Avoid global variables when possible

5. Best Practices:
   - Single Responsibility Principle
   - Clear, descriptive names
   - Proper documentation with docstrings
   - Input validation
   - Error handling
   - Consistent return types

Function Design Guidelines:
- Keep functions short and focused
- Use parameters instead of global variables
- Return meaningful values
- Handle edge cases
- Write testable functions
- Use type hints when helpful

Common Patterns:
- Validation functions
- Calculation functions
- Data transformation functions
- Helper/utility functions
- Factory functions (create objects)
"""

print("\n" + "="*50)
print("END OF MODULE 04 - FUNCTION BASICS")
print("="*50)
