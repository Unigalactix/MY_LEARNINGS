"""
01_BASICS - INPUT AND OUTPUT
=============================

This module covers how to interact with users through input and output:
- Using print() function for output
- Using input() function for user input
- String formatting techniques
- Basic user interaction patterns

Learning Objectives:
- Master the print() function and its parameters
- Learn how to get user input with input()
- Understand different string formatting methods
- Create interactive programs
"""

# ============================================================================
# OUTPUT WITH PRINT() FUNCTION
# ============================================================================

print("=== Python Print Function ===")

# Basic print usage
print("Hello, World!")
print("Welcome to Python programming!")

# Print multiple items
name = "Alice"
age = 28
print("Name:", name, "Age:", age)

# Print with different separators
print("Apple", "Banana", "Cherry", sep=", ")
print("Python", "is", "awesome", sep="-")
print("A", "B", "C", sep="")  # No separator

# Print with different endings (default is newline \n)
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Complete!")

print()  # Empty line for spacing

# Print to different outputs (usually stdout, but can redirect)
import sys
print("This goes to standard output", file=sys.stdout)
print("This could go to a file", file=sys.stdout)  # We'll cover files later

# ============================================================================
# STRING FORMATTING METHODS
# ============================================================================

print("\n=== String Formatting Methods ===")

# Method 1: Concatenation (basic but not recommended for complex formatting)
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print("Concatenation: " + full_name)

# Method 2: format() method
age = 30
height = 5.9
print("My name is {} and I am {} years old".format(full_name, age))
print("Name: {}, Age: {}, Height: {} feet".format(full_name, age, height))

# format() with positional arguments
print("Name: {0}, Age: {1}, in 10 years will be {2}".format(full_name, age, age + 10))

# format() with named arguments
print("Name: {name}, Age: {age}, Height: {height}".format(
    name=full_name, age=age, height=height))

# Method 3: f-strings (formatted string literals) - RECOMMENDED
# Available in Python 3.6+
print(f"My name is {full_name} and I am {age} years old")
print(f"In 5 years, {full_name} will be {age + 5} years old")

# f-strings with expressions
numbers = [1, 2, 3, 4, 5]
print(f"The sum of {numbers} is {sum(numbers)}")
print(f"The average is {sum(numbers) / len(numbers):.2f}")

# f-strings with formatting
pi = 3.14159265359
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi to 4 decimal places: {pi:.4f}")

price = 29.99
print(f"Price: ${price:.2f}")  # Always show 2 decimal places for money

# Method 4: % formatting (older style, still sometimes used)
print("Name: %s, Age: %d, Height: %.1f" % (full_name, age, height))

# ============================================================================
# INPUT FROM USERS
# ============================================================================

print("\n=== Getting User Input ===")

# Basic input (always returns a string)
print("Let's get some information about you...")

# Note: In a real program, you would uncomment these lines
# For demonstration, we'll use predefined values

# user_name = input("What's your name? ")
# user_age = input("What's your age? ")

# Simulating user input for demonstration
user_name = "Demo User"
user_age = "25"

print(f"You entered: Name = '{user_name}', Age = '{user_age}'")
print(f"Note: input() always returns a string. Age type is: {type(user_age)}")

# Converting input to numbers
age_as_number = int(user_age)
print(f"Age as number: {age_as_number}, Type: {type(age_as_number)}")

# ============================================================================
# PRACTICAL INPUT/OUTPUT EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: Simple calculator
print("--- Simple Calculator Demo ---")
# In real usage, uncomment these:
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# For demo:
num1, num2 = 10.5, 3.2
print(f"Demo values: num1 = {num1}, num2 = {num2}")

result_add = num1 + num2
result_multiply = num1 * num2

print(f"{num1} + {num2} = {result_add}")
print(f"{num1} × {num2} = {result_multiply:.2f}")

# Example 2: Personal information form
print("\n--- Personal Info Form Demo ---")

# Simulated inputs:
first_name = "Jane"
last_name = "Doe"
birth_year = "1995"
favorite_color = "Blue"

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Birth Year: {birth_year}")
print(f"Favorite Color: {favorite_color}")

# Calculate current age (simplified)
current_year = 2024
age = current_year - int(birth_year)

print("\n--- Generated Profile ---")
print(f"Full Name: {first_name} {last_name}")
print(f"Age: {age} years old")
print(f"Favorite Color: {favorite_color}")

# Example 3: Interactive greeting
print("\n--- Interactive Greeting Demo ---")

# Real code would be:
# user_name = input("Enter your name: ")
# user_location = input("Where are you from? ")

# Demo values:
user_name = "Alex"
user_location = "New York"

print(f"Hello, {user_name}!")
print(f"It's nice to meet someone from {user_location}!")
print(f"Welcome to Python programming, {user_name}!")

# ============================================================================
# ADVANCED FORMATTING EXAMPLES
# ============================================================================

print("\n=== Advanced Formatting Examples ===")

# Number formatting
large_number = 1234567.89
print(f"Large number with commas: {large_number:,}")
print(f"Large number with commas and 2 decimals: {large_number:,.2f}")

# Percentage formatting
ratio = 0.756
print(f"Ratio as percentage: {ratio:.1%}")

# Padding and alignment
products = [
    ("Apple", 1.25),
    ("Banana", 0.75),
    ("Cherry", 3.50)
]

print("\n--- Product Price List ---")
print(f"{'Product':<10} {'Price':>8}")
print("-" * 20)
for product, price in products:
    print(f"{product:<10} ${price:>7.2f}")

# Date formatting (we'll cover datetime module later)
from datetime import datetime
now = datetime.now()
print(f"\nCurrent date and time: {now:%Y-%m-%d %H:%M:%S}")

# ============================================================================
# BEST PRACTICES AND TIPS
# ============================================================================

print("\n=== Best Practices ===")

# 1. Always validate user input in real applications
def safe_int_input(prompt):
    """A safer way to get integer input (for reference)"""
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("Please enter a valid integer.")

# 2. Use f-strings for modern Python (3.6+)
name = "Python"
version = 3.9
print(f"Using {name} version {version}")  # Preferred

# 3. Be consistent with formatting
score = 85.7
print(f"Your score: {score:.1f}%")  # Consistent decimal places

# 4. Use meaningful prompts
# Good: "Enter your age in years: "
# Bad: "Age: "

# ============================================================================
# INTERACTIVE PROGRAM TEMPLATE
# ============================================================================

print("\n=== Template for Interactive Programs ===")

def interactive_program_demo():
    """
    Template for creating interactive programs
    """
    print("=" * 40)
    print("  WELCOME TO PYTHON INTERACTIVE DEMO")
    print("=" * 40)
    
    # For demo purposes, we'll use predefined values
    # In real programs, replace these with actual input() calls
    
    print("\nGathering information...")
    
    # Simulated user inputs:
    name = "Student"
    age = "20"
    hobby = "Programming"
    
    print(f"Name entered: {name}")
    print(f"Age entered: {age}")
    print(f"Hobby entered: {hobby}")
    
    # Process the data
    age_num = int(age)
    
    # Generate output
    print(f"\n--- SUMMARY ---")
    print(f"Hello, {name}!")
    print(f"You are {age_num} years old.")
    print(f"Your hobby is {hobby}.")
    
    if age_num >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    
    print(f"\nIn 10 years, you'll be {age_num + 10} years old!")
    print("\nThank you for using our program!")

# Run the demo
interactive_program_demo()

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. print() function:
   - Can print multiple items separated by commas
   - Use sep parameter to change separator
   - Use end parameter to change ending character
   
2. input() function:
   - Always returns a string
   - Convert to numbers using int() or float() when needed
   - Always validate user input in production code

3. String formatting (in order of preference):
   - f-strings: f"Hello {name}" (Python 3.6+, recommended)
   - .format(): "Hello {}".format(name)
   - % formatting: "Hello %s" % name (older style)
   - Concatenation: "Hello " + name (avoid for complex formatting)

4. Formatting options:
   - {:.2f} for 2 decimal places
   - {:,} for thousands separator
   - {:.1%} for percentage
   - {:<10} for left alignment with width 10
   - {:>10} for right alignment with width 10

Best Practices:
- Use f-strings for modern, readable code
- Always validate user input
- Provide clear prompts for user input
- Format numbers appropriately for their context
- Use meaningful variable names
"""

print("\n" + "="*50)
print("END OF MODULE 01 - INPUT AND OUTPUT")
print("="*50)
