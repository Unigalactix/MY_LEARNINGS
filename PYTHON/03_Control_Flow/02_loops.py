"""
03_CONTROL_FLOW - LOOPS
========================

This module covers loop structures in Python:
- for loops and range()
- while loops
- Loop control statements (break, continue, pass)
- Nested loops
- Loop patterns and best practices
- Iteration over different data structures

Learning Objectives:
- Master for and while loops
- Understand when to use each type of loop
- Learn loop control mechanisms
- Practice with real-world iteration scenarios
"""

# ============================================================================
# FOR LOOPS
# ============================================================================

print("=== For Loops ===")

# Basic for loop with range()
print("Counting from 0 to 4:")
for i in range(5):
    print(f"Count: {i}")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

print("\nCounting by 2s from 0 to 10:")
for i in range(0, 11, 2):
    print(f"Even number: {i}")

print("\nCountdown from 10 to 1:")
for i in range(10, 0, -1):
    print(f"Countdown: {i}")

# Looping through lists
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# Looping with index using enumerate()
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Starting enumerate from a different number
print("\nFruits with custom numbering:")
for index, fruit in enumerate(fruits, start=1):
    print(f"Item {index}: {fruit}")

# ============================================================================
# LOOPING THROUGH DIFFERENT DATA STRUCTURES
# ============================================================================

print("\n=== Looping Through Data Structures ===")

# Looping through strings
message = "Python"
print(f"Letters in '{message}':")
for char in message:
    print(f"- {char}")

# Looping through dictionaries
student_grades = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 88
}

print("\nStudent grades (keys only):")
for student in student_grades:
    print(f"- {student}")

print("\nStudent grades (key-value pairs):")
for student, grade in student_grades.items():
    print(f"{student}: {grade}%")

print("\nJust the grades (values only):")
for grade in student_grades.values():
    print(f"Grade: {grade}%")

# Looping through tuples
coordinates = [(0, 0), (1, 2), (3, 4), (5, 6)]
print("\nCoordinates:")
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# Looping through sets
unique_numbers = {1, 3, 5, 7, 9, 3, 1}  # Duplicates will be removed
print(f"\nUnique numbers: {unique_numbers}")
for number in unique_numbers:
    print(f"Number: {number}")

# ============================================================================
# WHILE LOOPS
# ============================================================================

print("\n=== While Loops ===")

# Basic while loop
count = 0
print("Counting with while loop:")
while count < 5:
    print(f"Count: {count}")
    count += 1  # Important: update the condition variable!

# While loop with user input simulation
print("\nGuessing game simulation:")
secret_number = 7
guess = 0
attempts = 0

while guess != secret_number and attempts < 3:
    attempts += 1
    # Simulating user guesses
    if attempts == 1:
        guess = 5
    elif attempts == 2:
        guess = 8
    else:
        guess = 7
    
    print(f"Attempt {attempts}: Guess is {guess}")
    
    if guess == secret_number:
        print("Congratulations! You guessed it!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

if guess != secret_number:
    print(f"Sorry! The number was {secret_number}")

# While loop for processing until condition
print("\nProcessing items until empty:")
items = ["task1", "task2", "task3", "task4"]
while items:  # Continue while list is not empty
    current_item = items.pop(0)  # Remove first item
    print(f"Processing: {current_item}")
    print(f"Remaining items: {len(items)}")

# ============================================================================
# LOOP CONTROL STATEMENTS
# ============================================================================

print("\n=== Loop Control Statements ===")

# BREAK statement - exits the loop completely
print("Using break to find first even number:")
numbers = [1, 3, 7, 8, 9, 12, 15]
for number in numbers:
    print(f"Checking: {number}")
    if number % 2 == 0:
        print(f"Found first even number: {number}")
        break
else:
    print("No even number found")  # This runs if loop completes without break

# CONTINUE statement - skips rest of current iteration
print("\nUsing continue to skip odd numbers:")
for number in range(1, 11):
    if number % 2 == 1:  # If odd
        continue  # Skip the rest of this iteration
    print(f"Even number: {number}")

# PASS statement - does nothing (placeholder)
print("\nUsing pass as placeholder:")
for i in range(5):
    if i < 3:
        pass  # TODO: implement later
    else:
        print(f"Processing: {i}")

# Practical example with break and continue
print("\nProcessing grades (skip invalid, stop at F):")
grades = [85, "invalid", 92, 78, "F", 88, 76]
for grade in grades:
    if isinstance(grade, str):
        if grade == "F":
            print("Found failing grade, stopping processing")
            break
        else:
            print(f"Skipping invalid grade: {grade}")
            continue
    
    # Process valid numeric grade
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    else:
        letter = "D"
    
    print(f"Grade {grade}: {letter}")

# ============================================================================
# NESTED LOOPS
# ============================================================================

print("\n=== Nested Loops ===")

# Multiplication table
print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{product:2}", end=" ")  # Format with 2 spaces, no newline
    print()  # New line after each row

# Matrix processing
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatrix elements:")
for row_index, row in enumerate(matrix):
    for col_index, element in enumerate(row):
        print(f"matrix[{row_index}][{col_index}] = {element}")

# Finding patterns in nested data
students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [88, 76, 94]},
    {"name": "Charlie", "grades": [91, 89, 87]}
]

print("\nStudent grade analysis:")
for student in students:
    name = student["name"]
    grades = student["grades"]
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    print(f"{name}: Average = {average:.1f}")

# Breaking out of nested loops
print("\nFinding first negative number in matrix:")
test_matrix = [
    [1, 2, 3],
    [4, -5, 6],
    [7, 8, 9]
]

found = False
for i, row in enumerate(test_matrix):
    for j, element in enumerate(row):
        if element < 0:
            print(f"Found negative number {element} at position ({i}, {j})")
            found = True
            break
    if found:  # Break outer loop too
        break

# ============================================================================
# LOOP PATTERNS AND TECHNIQUES
# ============================================================================

print("\n=== Loop Patterns and Techniques ===")

# Pattern 1: Accumulation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for number in numbers:
    total += number
print(f"Sum of {numbers}: {total}")

# Pattern 2: Filtering
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(f"Even numbers: {even_numbers}")

# Pattern 3: Transformation
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)
print(f"Squared numbers: {squared_numbers}")

# Pattern 4: Finding maximum/minimum
numbers = [34, 67, 23, 89, 12, 56]
max_value = numbers[0]  # Start with first element
max_index = 0

for index, number in enumerate(numbers):
    if number > max_value:
        max_value = number
        max_index = index

print(f"Maximum value {max_value} found at index {max_index}")

# Pattern 5: Counting occurrences
text = "hello world hello python"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"Word count: {word_count}")

# Pattern 6: Parallel iteration with zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("\nPeople information:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# ============================================================================
# LOOP OPTIMIZATION AND BEST PRACTICES
# ============================================================================

print("\n=== Loop Optimization and Best Practices ===")

# Use built-in functions when possible
numbers = [1, 2, 3, 4, 5]

# Instead of manual accumulation
manual_sum = 0
for num in numbers:
    manual_sum += num

# Use built-in sum()
builtin_sum = sum(numbers)

print(f"Manual sum: {manual_sum}")
print(f"Built-in sum: {builtin_sum}")

# Use list comprehensions for simple transformations
# Instead of this:
squares = []
for x in range(10):
    squares.append(x ** 2)

# Use this:
squares_comp = [x ** 2 for x in range(10)]

print(f"Squares (loop): {squares}")
print(f"Squares (comprehension): {squares_comp}")

# Use enumerate() instead of manual indexing
items = ["apple", "banana", "cherry"]

# Less Pythonic
print("\nLess Pythonic indexing:")
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# More Pythonic
print("\nMore Pythonic with enumerate:")
for i, item in enumerate(items):
    print(f"{i}: {item}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: File processing simulation
def process_log_files():
    print("--- Log File Processing ---")
    log_entries = [
        "INFO: Application started",
        "DEBUG: Loading configuration",
        "ERROR: Database connection failed",
        "WARNING: High memory usage",
        "INFO: User logged in",
        "ERROR: File not found",
        "INFO: Application shutdown"
    ]
    
    error_count = 0
    warning_count = 0
    
    for entry in log_entries:
        if entry.startswith("ERROR"):
            error_count += 1
            print(f"🔴 {entry}")
        elif entry.startswith("WARNING"):
            warning_count += 1
            print(f"🟡 {entry}")
        elif entry.startswith("INFO"):
            print(f"ℹ️ {entry}")
        else:
            print(f"📝 {entry}")
    
    print(f"\nSummary: {error_count} errors, {warning_count} warnings")

process_log_files()

# Example 2: Shopping cart total calculation
def calculate_shopping_total():
    print("\n--- Shopping Cart Calculation ---")
    cart = [
        {"item": "Laptop", "price": 999.99, "quantity": 1},
        {"item": "Mouse", "price": 29.99, "quantity": 2},
        {"item": "Keyboard", "price": 79.99, "quantity": 1},
        {"item": "Monitor", "price": 299.99, "quantity": 1}
    ]
    
    total = 0
    item_count = 0
    
    print("Shopping Cart:")
    for item_info in cart:
        item = item_info["item"]
        price = item_info["price"]
        quantity = item_info["quantity"]
        
        line_total = price * quantity
        total += line_total
        item_count += quantity
        
        print(f"{item}: ${price:.2f} x {quantity} = ${line_total:.2f}")
    
    print(f"\nTotal items: {item_count}")
    print(f"Subtotal: ${total:.2f}")
    
    # Apply discounts
    if total > 500:
        discount = total * 0.1  # 10% discount
        total -= discount
        print(f"Discount (10%): -${discount:.2f}")
    
    tax = total * 0.08  # 8% tax
    total += tax
    print(f"Tax (8%): +${tax:.2f}")
    print(f"Final total: ${total:.2f}")

calculate_shopping_total()

# Example 3: Password strength checker
def check_password_strength():
    print("\n--- Password Strength Checker ---")
    passwords = ["123456", "password", "MySecure123!", "abc", "P@ssw0rd123"]
    
    for password in passwords:
        print(f"\nChecking password: {'*' * len(password)}")
        
        # Initialize criteria
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        
        # Check each character
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_special = True
        
        # Evaluate strength
        criteria_met = 0
        
        if len(password) >= 8:
            criteria_met += 1
        else:
            print("❌ Too short (needs 8+ characters)")
        
        if has_upper:
            criteria_met += 1
        else:
            print("❌ Needs uppercase letter")
        
        if has_lower:
            criteria_met += 1
        else:
            print("❌ Needs lowercase letter")
        
        if has_digit:
            criteria_met += 1
        else:
            print("❌ Needs digit")
        
        if has_special:
            criteria_met += 1
        else:
            print("❌ Needs special character")
        
        # Determine strength
        if criteria_met == 5:
            strength = "Strong"
        elif criteria_met >= 3:
            strength = "Medium"
        else:
            strength = "Weak"
        
        print(f"Strength: {strength} ({criteria_met}/5 criteria)")

check_password_strength()

# Example 4: Finding prime numbers
def find_prime_numbers():
    print("\n--- Prime Number Finder ---")
    limit = 30
    primes = []
    
    for number in range(2, limit + 1):
        is_prime = True
        
        # Check if number has any divisors
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(number)
    
    print(f"Prime numbers up to {limit}: {primes}")
    print(f"Found {len(primes)} prime numbers")

find_prime_numbers()

# ============================================================================
# COMMON PITFALLS AND SOLUTIONS
# ============================================================================

print("\n=== Common Pitfalls and Solutions ===")

# Pitfall 1: Infinite while loop
print("Avoiding infinite loops:")
# Bad: while True without break condition
# Good: always have a way to exit
counter = 0
while counter < 3:
    print(f"Safe loop iteration: {counter}")
    counter += 1  # Don't forget to update!

# Pitfall 2: Modifying list while iterating
print("\nSafe list modification:")
numbers = [1, 2, 3, 4, 5, 6]
print(f"Original: {numbers}")

# Wrong way (can skip elements):
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)

# Right way (iterate over copy):
numbers_copy = numbers.copy()
for num in numbers_copy:
    if num % 2 == 0:
        numbers.remove(num)

print(f"After removing evens: {numbers}")

# Alternative: build new list
original = [1, 2, 3, 4, 5, 6]
odds_only = []
for num in original:
    if num % 2 == 1:
        odds_only.append(num)
print(f"Odds only: {odds_only}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. For Loops:
   - Best for iterating over sequences
   - Use range() for numeric sequences
   - Use enumerate() when you need index
   - Use zip() for parallel iteration

2. While Loops:
   - Best for condition-based iteration
   - Always ensure loop condition will eventually be False
   - Good for user input loops
   - Useful when you don't know iteration count in advance

3. Loop Control:
   - break: exits loop completely
   - continue: skips to next iteration
   - pass: does nothing (placeholder)
   - else clause: runs if loop completes without break

4. Nested Loops:
   - Inner loop completes fully for each outer iteration
   - Use break carefully in nested structures
   - Consider flattening when possible

5. Best Practices:
   - Use built-in functions (sum, max, min) when possible
   - Prefer list comprehensions for simple transformations
   - Use enumerate() instead of manual indexing
   - Don't modify lists while iterating
   - Choose the right loop type for the task

Common Patterns:
- Accumulation (sum, product)
- Filtering (selecting items)
- Transformation (modifying items)
- Searching (finding items)
- Counting (occurrences)
- Validation (checking conditions)

Performance Tips:
- List comprehensions are often faster than explicit loops
- Built-in functions are optimized
- Avoid nested loops when possible
- Use appropriate data structures for lookups
"""

print("\n" + "="*50)
print("END OF MODULE 03 - LOOPS")
print("="*50)
