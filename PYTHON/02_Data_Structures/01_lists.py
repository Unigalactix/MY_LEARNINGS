"""
02_DATA_STRUCTURES - LISTS
===========================

This module covers Python lists in detail:
- Creating and accessing lists
- List methods and operations
- List comprehensions
- Nested lists
- Common list patterns

Learning Objectives:
- Master list creation and manipulation
- Understand mutable vs immutable characteristics
- Learn efficient list operations
- Practice with real-world examples
"""

# ============================================================================
# CREATING LISTS
# ============================================================================

print("=== Creating Lists ===")

# Empty list
empty_list = []
also_empty = list()
print(f"Empty list: {empty_list}")
print(f"Also empty: {also_empty}")

# List with initial values
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, 3.14, True, None]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed_list}")

# Creating lists with range()
range_list = list(range(10))          # [0, 1, 2, ..., 9]
range_custom = list(range(5, 15, 2))  # [5, 7, 9, 11, 13]
print(f"Range list: {range_list}")
print(f"Custom range: {range_custom}")

# Creating lists with repetition
zeros = [0] * 5           # [0, 0, 0, 0, 0]
pattern = ["a", "b"] * 3  # ["a", "b", "a", "b", "a", "b"]
print(f"Zeros: {zeros}")
print(f"Pattern: {pattern}")

# ============================================================================
# ACCESSING LIST ELEMENTS
# ============================================================================

print("\n=== Accessing List Elements ===")

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")

# Positive indexing (0-based)
print(f"First color: {colors[0]}")
print(f"Second color: {colors[1]}")
print(f"Last color: {colors[4]}")

# Negative indexing (from the end)
print(f"Last color: {colors[-1]}")
print(f"Second to last: {colors[-2]}")

# List slicing [start:end:step]
print(f"First three colors: {colors[0:3]}")
print(f"First three colors (shorthand): {colors[:3]}")
print(f"Last two colors: {colors[3:]}")
print(f"All colors: {colors[:]}")
print(f"Every second color: {colors[::2]}")
print(f"Reverse order: {colors[::-1]}")

# Advanced slicing
print(f"Middle colors: {colors[1:4]}")
print(f"Skip first and last: {colors[1:-1]}")

# ============================================================================
# LIST METHODS AND OPERATIONS
# ============================================================================

print("\n=== List Methods and Operations ===")

# Working with a sample list
shopping_list = ["milk", "bread", "eggs"]
print(f"Initial shopping list: {shopping_list}")

# Adding elements
shopping_list.append("butter")           # Add one item to the end
print(f"After append: {shopping_list}")

shopping_list.insert(1, "cheese")       # Insert at specific position
print(f"After insert: {shopping_list}")

shopping_list.extend(["apples", "bananas"])  # Add multiple items
print(f"After extend: {shopping_list}")

# Alternative ways to add items
shopping_list += ["yogurt"]             # Using += operator
print(f"After += : {shopping_list}")

# Removing elements
removed_item = shopping_list.pop()      # Remove and return last item
print(f"Removed item: {removed_item}")
print(f"After pop(): {shopping_list}")

removed_at_index = shopping_list.pop(1) # Remove at specific index
print(f"Removed at index 1: {removed_at_index}")
print(f"After pop(1): {shopping_list}")

shopping_list.remove("eggs")            # Remove first occurrence of value
print(f"After remove('eggs'): {shopping_list}")

# Finding elements
if "milk" in shopping_list:
    milk_index = shopping_list.index("milk")
    print(f"Milk is at index: {milk_index}")

# Count occurrences
test_list = [1, 2, 3, 2, 2, 4]
count_of_twos = test_list.count(2)
print(f"Number of 2s in {test_list}: {count_of_twos}")

# List length
print(f"Shopping list length: {len(shopping_list)}")

# ============================================================================
# LIST SORTING AND REVERSING
# ============================================================================

print("\n=== Sorting and Reversing ===")

# Sample data
numbers = [64, 34, 25, 12, 22, 11, 90]
names = ["Charlie", "Alice", "Bob", "David"]

print(f"Original numbers: {numbers}")
print(f"Original names: {names}")

# Sorting (modifies the original list)
numbers.sort()                    # Sort in ascending order
print(f"Numbers sorted: {numbers}")

names.sort()                      # Sort alphabetically
print(f"Names sorted: {names}")

numbers.sort(reverse=True)        # Sort in descending order
print(f"Numbers reverse sorted: {numbers}")

# Sorting without modifying original (returns new list)
original = [3, 1, 4, 1, 5, 9]
sorted_copy = sorted(original)
print(f"Original: {original}")
print(f"Sorted copy: {sorted_copy}")

# Reversing
numbers.reverse()                 # Reverse the list in place
print(f"Numbers reversed: {numbers}")

reversed_copy = list(reversed(original))  # Create reversed copy
print(f"Reversed copy: {reversed_copy}")

# Custom sorting with key function
students = ["Alice", "bob", "Charlie", "dave"]
students.sort(key=str.lower)      # Case-insensitive sort
print(f"Case-insensitive sort: {students}")

# Sorting by length
words = ["python", "java", "c", "javascript", "go"]
words.sort(key=len)
print(f"Sorted by length: {words}")

# ============================================================================
# LIST COMPREHENSIONS
# ============================================================================

print("\n=== List Comprehensions ===")

# Basic list comprehension syntax: [expression for item in iterable]

# Traditional way
squares_traditional = []
for x in range(10):
    squares_traditional.append(x ** 2)
print(f"Traditional squares: {squares_traditional}")

# List comprehension way (more Pythonic)
squares_comprehension = [x ** 2 for x in range(10)]
print(f"Comprehension squares: {squares_comprehension}")

# With conditional (filter)
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# String processing
words = ["hello", "world", "python", "programming"]
upper_words = [word.upper() for word in words]
print(f"Uppercase words: {upper_words}")

# More complex expressions
temperatures_celsius = [0, 20, 30, 40, 100]
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]
print(f"Celsius: {temperatures_celsius}")
print(f"Fahrenheit: {temperatures_fahrenheit}")

# Conditional expressions in comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Even/Odd classification: {even_odd}")

# Nested comprehensions (be careful with readability)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Original matrix: {matrix}")
print(f"Flattened: {flattened}")

# ============================================================================
# NESTED LISTS (2D LISTS)
# ============================================================================

print("\n=== Nested Lists (2D Lists) ===")

# Creating 2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Accessing elements in 2D list
print(f"Element at row 1, column 2: {matrix[1][2]}")  # 6
print(f"First row: {matrix[0]}")
print(f"First column: [matrix[i][0] for i in range(len(matrix))]")

first_column = [matrix[i][0] for i in range(len(matrix))]
print(f"First column: {first_column}")

# Creating 2D list with comprehension
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table:")
for row in multiplication_table:
    print(row)

# Practical example: Student grades
students_grades = [
    ["Alice", 85, 92, 78],
    ["Bob", 90, 87, 93],
    ["Charlie", 78, 85, 82]
]

print("\nStudent Grades:")
for student in students_grades:
    name = student[0]
    grades = student[1:]
    average = sum(grades) / len(grades)
    print(f"{name}: {grades} -> Average: {average:.1f}")

# ============================================================================
# COMMON LIST PATTERNS AND ALGORITHMS
# ============================================================================

print("\n=== Common List Patterns ===")

# Finding maximum and minimum
numbers = [23, 45, 12, 67, 34, 89, 15]
print(f"Numbers: {numbers}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# Finding index of max/min
max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))
print(f"Max value {max(numbers)} is at index {max_index}")
print(f"Min value {min(numbers)} is at index {min_index}")

# Filtering lists
positive_numbers = [x for x in [-5, -2, 0, 3, 7, -1, 9] if x > 0]
print(f"Positive numbers: {positive_numbers}")

# Removing duplicates (preserving order)
numbers_with_duplicates = [1, 2, 3, 2, 4, 3, 5, 1]
unique_numbers = []
for num in numbers_with_duplicates:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"Original with duplicates: {numbers_with_duplicates}")
print(f"Unique (preserved order): {unique_numbers}")

# Alternative using dict.fromkeys() (Python 3.7+)
unique_ordered = list(dict.fromkeys(numbers_with_duplicates))
print(f"Unique (dict method): {unique_ordered}")

# Checking if list is sorted
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

test1 = [1, 2, 3, 4, 5]
test2 = [1, 3, 2, 4, 5]
print(f"{test1} is sorted: {is_sorted(test1)}")
print(f"{test2} is sorted: {is_sorted(test2)}")

# ============================================================================
# LIST COPYING AND REFERENCES
# ============================================================================

print("\n=== List Copying and References ===")

# Understanding list references
original = [1, 2, 3, 4]
reference = original          # This creates a reference, not a copy!
shallow_copy = original.copy()  # or original[:]
import copy
deep_copy = copy.deepcopy(original)

print(f"Original: {original}")
print(f"Reference: {reference}")
print(f"Shallow copy: {shallow_copy}")

# Modifying original affects reference but not copies
original.append(5)
print(f"After modifying original:")
print(f"Original: {original}")
print(f"Reference: {reference}")      # Changed!
print(f"Shallow copy: {shallow_copy}")  # Unchanged

# Demonstration with nested lists
nested_original = [[1, 2], [3, 4]]
nested_shallow = nested_original.copy()
nested_deep = copy.deepcopy(nested_original)

nested_original[0].append(3)  # Modify inner list
print(f"Original nested: {nested_original}")
print(f"Shallow copy: {nested_shallow}")    # Inner list changed!
print(f"Deep copy: {nested_deep}")          # Unchanged

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: Grade calculator
def calculate_grades():
    grades = [85, 92, 78, 96, 88, 73, 89]
    
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    # Letter grade assignment
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    
    print(f"Grades: {grades}")
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Letter grades: {letter_grades}")

calculate_grades()

# Example 2: Inventory management
print("\n--- Inventory Management ---")
inventory = [
    ["Laptop", 50, 999.99],
    ["Mouse", 200, 29.99],
    ["Keyboard", 150, 79.99],
    ["Monitor", 75, 299.99]
]

print("Current Inventory:")
total_value = 0
for item in inventory:
    name, quantity, price = item
    item_value = quantity * price
    total_value += item_value
    print(f"{name}: {quantity} units @ ${price:.2f} = ${item_value:.2f}")

print(f"Total inventory value: ${total_value:.2f}")

# Find items with low stock (< 100)
low_stock = [item for item in inventory if item[1] < 100]
print(f"Low stock items: {[item[0] for item in low_stock]}")

# Example 3: Text processing
print("\n--- Text Processing ---")
text = "The quick brown fox jumps over the lazy dog"
words = text.split()
print(f"Original text: {text}")
print(f"Words: {words}")
print(f"Word count: {len(words)}")
print(f"Average word length: {sum(len(word) for word in words) / len(words):.1f}")

# Find words longer than 4 characters
long_words = [word for word in words if len(word) > 4]
print(f"Words longer than 4 chars: {long_words}")

# ============================================================================
# PERFORMANCE TIPS
# ============================================================================

print("\n=== Performance Tips ===")

import time

# Tip 1: List comprehensions are generally faster than for loops
print("Comparing performance: for loop vs list comprehension")

# For loop method
start_time = time.time()
result1 = []
for i in range(10000):
    result1.append(i ** 2)
loop_time = time.time() - start_time

# List comprehension method
start_time = time.time()
result2 = [i ** 2 for i in range(10000)]
comp_time = time.time() - start_time

print(f"For loop time: {loop_time:.4f} seconds")
print(f"List comprehension time: {comp_time:.4f} seconds")
print(f"List comprehension is {loop_time/comp_time:.1f}x faster")

# Tip 2: Use extend() instead of repeated append() for multiple items
print("\nPrefer extend() over multiple append() calls")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. List Basics:
   - Lists are mutable (can be changed after creation)
   - Use square brackets [] to create lists
   - Elements can be of different types
   - Zero-based indexing (first element is at index 0)

2. Common Operations:
   - append() adds one item to the end
   - extend() adds multiple items to the end
   - insert() adds item at specific position
   - remove() removes first occurrence of value
   - pop() removes and returns item (last by default)
   - index() finds position of value
   - count() counts occurrences

3. List Comprehensions:
   - Syntax: [expression for item in iterable if condition]
   - More Pythonic and often faster than for loops
   - Can include conditional logic

4. Slicing:
   - list[start:end:step]
   - Negative indices count from the end
   - Omitted values use defaults (0, len, 1)

5. Copying:
   - assignment (=) creates a reference, not a copy
   - Use .copy() or [:] for shallow copy
   - Use copy.deepcopy() for nested structures

6. Performance:
   - List comprehensions are generally faster
   - Use extend() for adding multiple items
   - Consider using collections.deque for frequent insertions/deletions at both ends

Best Practices:
- Use meaningful variable names
- Prefer list comprehensions for simple transformations
- Be careful with list references vs copies
- Use built-in functions (sum, max, min) when possible
- Consider memory usage with very large lists
"""

print("\n" + "="*50)
print("END OF MODULE 02 - LISTS")
print("="*50)
