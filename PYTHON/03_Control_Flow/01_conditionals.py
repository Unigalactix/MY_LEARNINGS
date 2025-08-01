"""
03_CONTROL_FLOW - CONDITIONAL STATEMENTS
=========================================

This module covers conditional statements in Python:
- if, elif, else statements
- Comparison and logical operators in conditions
- Nested conditionals
- Conditional expressions (ternary operator)
- Best practices for writing clean conditionals

Learning Objectives:
- Master conditional logic in Python
- Learn to write clean, readable if statements
- Understand operator precedence in conditions
- Practice with real-world decision-making scenarios
"""

# ============================================================================
# BASIC IF STATEMENTS
# ============================================================================

print("=== Basic If Statements ===")

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult!")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")

# Multiple conditions with elif
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# ============================================================================
# COMPARISON OPERATORS IN CONDITIONS
# ============================================================================

print("\n=== Comparison Operators in Conditions ===")

# Numeric comparisons
number = 42
print(f"Number: {number}")

if number == 42:
    print("The answer to life, universe, and everything!")

if number != 0:
    print("Number is not zero")

if 0 < number < 100:  # Chained comparison (Pythonic!)
    print("Number is between 0 and 100")

# String comparisons
name = "Alice"
print(f"Name: {name}")

if name == "Alice":
    print("Hello, Alice!")

if name.lower() == "alice":  # Case-insensitive comparison
    print("Hello there (case-insensitive)!")

# Checking string properties
password = "MySecure123"
if len(password) >= 8:
    print("Password length is acceptable")

if "123" in password:
    print("Password contains numbers")

# ============================================================================
# LOGICAL OPERATORS IN CONDITIONS
# ============================================================================

print("\n=== Logical Operators in Conditions ===")

# AND operator - both conditions must be True
username = "admin"
password = "secret123"
is_active = True

if username == "admin" and password == "secret123" and is_active:
    print("Login successful!")
else:
    print("Login failed!")

# OR operator - at least one condition must be True
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# NOT operator - reverses the boolean value
is_raining = False
if not is_raining:
    print("Good day for a walk!")

# Complex logical expressions
age = 25
has_license = True
has_car = False

if age >= 18 and has_license and (has_car or age >= 21):
    print("Can rent a car")
else:
    print("Cannot rent a car")

# ============================================================================
# NESTED CONDITIONALS
# ============================================================================

print("\n=== Nested Conditionals ===")

# Weather decision system
weather = "sunny"
temperature = 22
has_umbrella = True

print(f"Weather: {weather}, Temperature: {temperature}°C")

if weather == "sunny":
    if temperature > 25:
        print("Perfect for swimming!")
    elif temperature > 15:
        print("Great for a picnic!")
    else:
        print("A bit cool, but sunny!")
elif weather == "rainy":
    if has_umbrella:
        print("You can go out with an umbrella")
    else:
        print("Better stay inside")
else:
    print("Check the weather forecast")

# Academic performance evaluation
exam_score = 88
assignment_score = 92
attendance = 95

print(f"Exam: {exam_score}, Assignment: {assignment_score}, Attendance: {attendance}%")

if exam_score >= 80:
    if assignment_score >= 85:
        if attendance >= 90:
            final_grade = "A"
            scholarship = True
        else:
            final_grade = "B+"
            scholarship = False
    else:
        final_grade = "B"
        scholarship = False
else:
    if assignment_score >= 90 and attendance >= 95:
        final_grade = "B-"
        scholarship = False
    else:
        final_grade = "C"
        scholarship = False

print(f"Final grade: {final_grade}")
print(f"Scholarship eligible: {scholarship}")

# ============================================================================
# CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# ============================================================================

print("\n=== Conditional Expressions (Ternary Operator) ===")

# Syntax: value_if_true if condition else value_if_false

# Simple example
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age: {age}, Status: {status}")

# Numeric example
a = 10
b = 5
max_value = a if a > b else b
print(f"Maximum of {a} and {b} is {max_value}")

# String example
weather = "rainy"
clothing = "raincoat" if weather == "rainy" else "t-shirt"
print(f"Weather is {weather}, wear a {clothing}")

# Nested conditional expressions (use sparingly for readability)
score = 75
letter_grade = ("A" if score >= 90 else 
                "B" if score >= 80 else 
                "C" if score >= 70 else 
                "D" if score >= 60 else "F")
print(f"Score: {score}, Grade: {letter_grade}")

# Using in function calls
numbers = [1, 5, 3, 9, 2]
print(f"Numbers: {numbers}")
print(f"List is {'empty' if len(numbers) == 0 else 'not empty'}")

# ============================================================================
# TRUTHY AND FALSY VALUES
# ============================================================================

print("\n=== Truthy and Falsy Values ===")

# Falsy values in Python (evaluate to False in boolean context):
# False, None, 0, 0.0, '', [], {}, set()

print("Testing falsy values:")
falsy_values = [False, None, 0, 0.0, '', [], {}, set()]
for value in falsy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{repr(value)} is falsy")

# Truthy values (everything else)
print("\nTesting truthy values:")
truthy_values = [True, 1, -1, 0.1, 'hello', [1], {'a': 1}, {1}]
for value in truthy_values:
    if value:
        print(f"{repr(value)} is truthy")
    else:
        print(f"{repr(value)} is falsy")

# Practical applications
name = ""
if name:  # Empty string is falsy
    print(f"Hello, {name}!")
else:
    print("Please enter your name")

items = []
if items:  # Empty list is falsy
    print(f"You have {len(items)} items")
else:
    print("Your list is empty")

# Using truthy/falsy for default values
user_input = ""  # Simulating empty input
display_name = user_input or "Anonymous"  # Use "Anonymous" if input is empty
print(f"Display name: {display_name}")

# ============================================================================
# MEMBERSHIP AND IDENTITY TESTING
# ============================================================================

print("\n=== Membership and Identity Testing ===")

# Membership testing with 'in' and 'not in'
fruits = ["apple", "banana", "orange", "grape"]
fruit = "apple"

if fruit in fruits:
    print(f"{fruit} is available")

if "mango" not in fruits:
    print("Mango is not available")

# String membership
email = "user@example.com"
if "@" in email and "." in email:
    print("Email format looks valid")

# Dictionary membership (checks keys by default)
user_permissions = {"read": True, "write": False, "delete": False}
if "admin" in user_permissions:
    print("User has admin permission")
else:
    print("User does not have admin permission")

# Identity testing with 'is' and 'is not'
value = None
if value is None:  # Preferred way to check for None
    print("Value is None")

result = True
if result is True:  # Usually just use 'if result:'
    print("Result is True")

# Checking for specific types
data = [1, 2, 3]
if type(data) is list:
    print("Data is a list")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: User authentication system
def authenticate_user():
    print("--- User Authentication ---")
    username = "admin"
    password = "secure123"
    account_locked = False
    failed_attempts = 0
    
    # Simulated login attempt
    input_username = "admin"
    input_password = "secure123"
    
    if account_locked:
        print("Account is locked. Please contact administrator.")
    elif failed_attempts >= 3:
        print("Too many failed attempts. Account temporarily locked.")
    elif username == input_username and password == input_password:
        print("Login successful!")
        print("Welcome to the system!")
    else:
        print("Invalid username or password.")
        failed_attempts += 1
        print(f"Failed attempts: {failed_attempts}")

authenticate_user()

# Example 2: Grade calculator with detailed feedback
def calculate_grade():
    print("\n--- Grade Calculator ---")
    exam_score = 85
    homework_avg = 90
    participation = 95
    attendance = 88
    
    print(f"Exam: {exam_score}%")
    print(f"Homework: {homework_avg}%")
    print(f"Participation: {participation}%")
    print(f"Attendance: {attendance}%")
    
    # Calculate weighted average
    final_score = (exam_score * 0.4 + 
                   homework_avg * 0.3 + 
                   participation * 0.2 + 
                   attendance * 0.1)
    
    print(f"Final Score: {final_score:.1f}%")
    
    # Determine letter grade
    if final_score >= 97:
        letter_grade = "A+"
    elif final_score >= 93:
        letter_grade = "A"
    elif final_score >= 90:
        letter_grade = "A-"
    elif final_score >= 87:
        letter_grade = "B+"
    elif final_score >= 83:
        letter_grade = "B"
    elif final_score >= 80:
        letter_grade = "B-"
    elif final_score >= 77:
        letter_grade = "C+"
    elif final_score >= 73:
        letter_grade = "C"
    elif final_score >= 70:
        letter_grade = "C-"
    elif final_score >= 67:
        letter_grade = "D+"
    elif final_score >= 65:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    print(f"Letter Grade: {letter_grade}")
    
    # Additional feedback
    if final_score >= 90:
        print("Excellent work!")
    elif final_score >= 80:
        print("Good job!")
    elif final_score >= 70:
        print("Satisfactory performance.")
    else:
        print("Needs improvement.")
    
    # Specific recommendations
    if exam_score < 80:
        print("Recommendation: Focus more on exam preparation.")
    if homework_avg < 85:
        print("Recommendation: Complete all homework assignments.")
    if attendance < 90:
        print("Recommendation: Improve class attendance.")

calculate_grade()

# Example 3: Shopping discount calculator
def calculate_discount():
    print("\n--- Shopping Discount Calculator ---")
    subtotal = 150.00
    is_member = True
    coupon_code = "SAVE20"
    item_count = 8
    
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Member: {is_member}")
    print(f"Coupon: {coupon_code}")
    print(f"Items: {item_count}")
    
    discount = 0
    discount_description = []
    
    # Member discount
    if is_member:
        discount += 0.10  # 10% member discount
        discount_description.append("10% member discount")
    
    # Bulk purchase discount
    if item_count >= 5:
        discount += 0.05  # 5% bulk discount
        discount_description.append("5% bulk purchase discount")
    
    # High value discount
    if subtotal >= 100:
        discount += 0.05  # 5% high value discount
        discount_description.append("5% high value discount")
    
    # Coupon discount
    if coupon_code == "SAVE20":
        discount += 0.20  # 20% coupon discount
        discount_description.append("20% coupon discount")
    elif coupon_code == "SAVE10":
        discount += 0.10  # 10% coupon discount
        discount_description.append("10% coupon discount")
    
    # Cap maximum discount
    if discount > 0.50:  # Maximum 50% discount
        discount = 0.50
        discount_description.append("(capped at 50%)")
    
    discount_amount = subtotal * discount
    final_total = subtotal - discount_amount
    
    print(f"\nApplied discounts: {', '.join(discount_description)}")
    print(f"Total discount: {discount * 100:.0f}% (${discount_amount:.2f})")
    print(f"Final total: ${final_total:.2f}")
    
    # Savings message
    if discount_amount > 20:
        print("Great savings!")
    elif discount_amount > 10:
        print("Good savings!")
    else:
        print("Thanks for shopping with us!")

calculate_discount()

# ============================================================================
# COMMON PATTERNS AND BEST PRACTICES
# ============================================================================

print("\n=== Common Patterns and Best Practices ===")

# Pattern 1: Input validation
def validate_input():
    age_input = "25"  # Simulated user input
    
    # Validate numeric input
    if age_input.isdigit():
        age = int(age_input)
        if 0 <= age <= 150:
            print(f"Valid age: {age}")
        else:
            print("Age must be between 0 and 150")
    else:
        print("Please enter a valid number")

validate_input()

# Pattern 2: Early returns to reduce nesting
def process_order(items, payment_method, customer_type):
    """Example of using early returns to reduce nesting"""
    
    # Early validation
    if not items:
        return "Error: No items in order"
    
    if payment_method not in ["credit", "debit", "cash"]:
        return "Error: Invalid payment method"
    
    # Calculate total
    total = sum(item.get("price", 0) for item in items)
    
    # Apply discounts based on customer type
    if customer_type == "premium":
        total *= 0.9  # 10% discount
    elif customer_type == "employee":
        total *= 0.8  # 20% discount
    
    return f"Order processed: ${total:.2f}"

# Test the function
sample_items = [{"price": 10}, {"price": 15}, {"price": 20}]
result = process_order(sample_items, "credit", "premium")
print(f"Order result: {result}")

# Pattern 3: Using dictionaries for complex conditionals
def get_tax_rate(state):
    """Using dictionary instead of multiple if-elif statements"""
    tax_rates = {
        "CA": 0.0825,
        "NY": 0.08,
        "TX": 0.0625,
        "FL": 0.06,
        "WA": 0.065
    }
    return tax_rates.get(state, 0.05)  # Default 5% for unknown states

state = "CA"
tax_rate = get_tax_rate(state)
print(f"Tax rate for {state}: {tax_rate * 100}%")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. Basic Conditional Structure:
   - if condition:
   - elif condition:
   - else:
   - Indentation is crucial in Python

2. Comparison Operators:
   - ==, !=, <, >, <=, >=
   - Can chain comparisons: a < b < c
   - String comparisons are lexicographic

3. Logical Operators:
   - and: both conditions must be True
   - or: at least one condition must be True
   - not: reverses boolean value
   - Short-circuit evaluation

4. Conditional Expressions (Ternary):
   - value_if_true if condition else value_if_false
   - Use for simple conditions only

5. Truthy and Falsy Values:
   - Falsy: False, None, 0, 0.0, '', [], {}, set()
   - Everything else is truthy
   - Useful for checking empty collections

6. Membership and Identity:
   - 'in' and 'not in' for membership testing
   - 'is' and 'is not' for identity testing
   - Use 'is' with None, True, False

Best Practices:
- Keep conditions simple and readable
- Use parentheses to clarify complex expressions
- Prefer early returns to reduce nesting
- Use dictionaries for multiple discrete choices
- Consider using helper functions for complex logic
- Write conditions that read like English when possible
- Use meaningful variable names in conditions

Common Patterns:
- Input validation
- Authentication/authorization
- Business rule implementation
- Configuration-based behavior
- Error handling and user feedback
"""

print("\n" + "="*50)
print("END OF MODULE 03 - CONDITIONAL STATEMENTS")
print("="*50)
