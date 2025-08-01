"""
02_DATA_STRUCTURES - DICTIONARIES
==================================

This module covers Python dictionaries in detail:
- Creating and accessing dictionaries
- Dictionary methods and operations
- Dictionary comprehensions
- Nested dictionaries
- Common dictionary patterns

Learning Objectives:
- Master dictionary creation and manipulation
- Understand key-value pair concepts
- Learn efficient dictionary operations
- Practice with real-world data structures
"""

# ============================================================================
# CREATING DICTIONARIES
# ============================================================================

print("=== Creating Dictionaries ===")

# Empty dictionary
empty_dict = {}
also_empty = dict()
print(f"Empty dictionary: {empty_dict}")
print(f"Also empty: {also_empty}")

# Dictionary with initial values
student = {
    "name": "Alice Johnson",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "Computer Science"]
}
print(f"Student: {student}")

# Different ways to create dictionaries
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
print(f"Colors: {colors}")

# Using dict() constructor
person = dict(name="Bob", age=25, city="New York")
print(f"Person: {person}")

# Creating from lists of tuples
countries_capitals = [("USA", "Washington"), ("France", "Paris"), ("Japan", "Tokyo")]
capitals = dict(countries_capitals)
print(f"Capitals: {capitals}")

# Using zip to create dictionary
keys = ["apple", "banana", "orange"]
values = [1.2, 0.8, 1.5]
prices = dict(zip(keys, values))
print(f"Fruit prices: {prices}")

# ============================================================================
# ACCESSING DICTIONARY ELEMENTS
# ============================================================================

print("\n=== Accessing Dictionary Elements ===")

# Sample dictionary
book = {
    "title": "Python Programming",
    "author": "John Smith",
    "year": 2023,
    "pages": 450,
    "isbn": "978-1234567890"
}

print(f"Book: {book}")

# Accessing values using keys
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
print(f"Year: {book['year']}")

# Using get() method (safer - doesn't raise error if key doesn't exist)
print(f"Pages: {book.get('pages')}")
print(f"Publisher: {book.get('publisher', 'Unknown')}")  # Default value

# Check if key exists
if "isbn" in book:
    print(f"ISBN: {book['isbn']}")

# Get all keys, values, and items
print(f"Keys: {list(book.keys())}")
print(f"Values: {list(book.values())}")
print(f"Items: {list(book.items())}")

# ============================================================================
# MODIFYING DICTIONARIES
# ============================================================================

print("\n=== Modifying Dictionaries ===")

# Sample inventory
inventory = {
    "laptops": 50,
    "mice": 200,
    "keyboards": 150
}

print(f"Initial inventory: {inventory}")

# Adding new key-value pairs
inventory["monitors"] = 75
inventory["headphones"] = 120
print(f"After adding items: {inventory}")

# Modifying existing values
inventory["laptops"] += 25  # Received new stock
inventory["mice"] -= 10     # Sold some mice
print(f"After stock changes: {inventory}")

# Using update() to add multiple items
new_items = {"tablets": 30, "printers": 15, "webcams": 80}
inventory.update(new_items)
print(f"After bulk update: {inventory}")

# Removing items
removed_item = inventory.pop("webcams")  # Remove and return value
print(f"Removed {removed_item} webcams")
print(f"After removal: {inventory}")

# Remove with default value
removed = inventory.pop("smartphones", 0)  # Returns 0 if key not found
print(f"Removed {removed} smartphones")

# Delete using del keyword
del inventory["printers"]
print(f"After deleting printers: {inventory}")

# Clear all items
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(f"Cleared dictionary: {temp_dict}")

# ============================================================================
# DICTIONARY METHODS
# ============================================================================

print("\n=== Dictionary Methods ===")

# Sample data
scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 88,
    "Eve": 90
}

print(f"Scores: {scores}")

# Get all keys
print(f"Students: {list(scores.keys())}")

# Get all values
print(f"All scores: {list(scores.values())}")

# Get all key-value pairs
print(f"All items: {list(scores.items())}")

# Get value with default
print(f"Frank's score: {scores.get('Frank', 'Not found')}")

# setdefault() - get value or set default if key doesn't exist
scores.setdefault("Frank", 85)  # Adds Frank with score 85
scores.setdefault("Alice", 100)  # Alice already exists, no change
print(f"After setdefault: {scores}")

# popitem() - remove and return last inserted item (Python 3.7+)
last_item = scores.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem: {scores}")

# Copy dictionary
scores_copy = scores.copy()
print(f"Copy: {scores_copy}")

# ============================================================================
# DICTIONARY COMPREHENSIONS
# ============================================================================

print("\n=== Dictionary Comprehensions ===")

# Basic dictionary comprehension
# Syntax: {key_expression: value_expression for item in iterable}

# Create squares dictionary
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# From existing dictionary
celsius = {"morning": 20, "noon": 35, "evening": 25}
fahrenheit = {time: (temp * 9/5) + 32 for time, temp in celsius.items()}
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# With conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# String processing
words = ["hello", "world", "python", "programming"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Conditional values
scores = {"Alice": 95, "Bob": 67, "Charlie": 82, "Diana": 78}
pass_fail = {name: "Pass" if score >= 70 else "Fail" for name, score in scores.items()}
print(f"Pass/Fail: {pass_fail}")

# ============================================================================
# NESTED DICTIONARIES
# ============================================================================

print("\n=== Nested Dictionaries ===")

# Creating nested dictionaries
company = {
    "departments": {
        "engineering": {
            "employees": 50,
            "manager": "Alice Smith",
            "budget": 2000000
        },
        "marketing": {
            "employees": 20,
            "manager": "Bob Johnson",
            "budget": 800000
        },
        "sales": {
            "employees": 30,
            "manager": "Charlie Brown",
            "budget": 1200000
        }
    },
    "total_employees": 100,
    "founded": 2010
}

print("Company structure:")
print(f"Founded: {company['founded']}")
print(f"Total employees: {company['total_employees']}")

# Accessing nested values
print(f"Engineering manager: {company['departments']['engineering']['manager']}")
print(f"Marketing budget: ${company['departments']['marketing']['budget']:,}")

# Iterating through nested dictionary
print("\nDepartment details:")
for dept_name, dept_info in company["departments"].items():
    print(f"{dept_name.title()}:")
    print(f"  Manager: {dept_info['manager']}")
    print(f"  Employees: {dept_info['employees']}")
    print(f"  Budget: ${dept_info['budget']:,}")

# Safely accessing nested values
def safe_get_nested(dictionary, *keys):
    """Safely get nested dictionary value"""
    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return None
    return dictionary

# Usage example
manager = safe_get_nested(company, "departments", "engineering", "manager")
print(f"Engineering manager (safe): {manager}")

invalid = safe_get_nested(company, "departments", "hr", "manager")
print(f"HR manager (safe): {invalid}")

# ============================================================================
# WORKING WITH JSON-LIKE DATA
# ============================================================================

print("\n=== Working with JSON-like Data ===")

# Student database
students_db = {
    "students": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "grades": {"math": 95, "science": 88, "english": 92},
            "activities": ["chess", "debate", "volleyball"]
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "grades": {"math": 87, "science": 91, "english": 85},
            "activities": ["basketball", "coding"]
        },
        {
            "id": 3,
            "name": "Charlie Brown",
            "grades": {"math": 92, "science": 86, "english": 89},
            "activities": ["music", "art", "drama"]
        }
    ]
}

print("Student Database Analysis:")

# Calculate average grades for each student
for student in students_db["students"]:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades.values()) / len(grades)
    print(f"{name}: Average grade = {average:.1f}")

# Find students with math grade above 90
high_math_students = [
    student["name"] for student in students_db["students"]
    if student["grades"]["math"] > 90
]
print(f"Students with Math > 90: {high_math_students}")

# Count total activities
all_activities = []
for student in students_db["students"]:
    all_activities.extend(student["activities"])

activity_count = {}
for activity in all_activities:
    activity_count[activity] = activity_count.get(activity, 0) + 1

print(f"Activity participation: {activity_count}")

# ============================================================================
# COMMON DICTIONARY PATTERNS
# ============================================================================

print("\n=== Common Dictionary Patterns ===")

# Pattern 1: Frequency counting
text = "hello world hello python world"
words = text.split()

# Method 1: Using get()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word count (get method): {word_count}")

# Method 2: Using setdefault()
word_count2 = {}
for word in words:
    word_count2.setdefault(word, 0)
    word_count2[word] += 1
print(f"Word count (setdefault): {word_count2}")

# Method 3: Using collections.defaultdict
from collections import defaultdict
word_count3 = defaultdict(int)
for word in words:
    word_count3[word] += 1
print(f"Word count (defaultdict): {dict(word_count3)}")

# Pattern 2: Grouping data
students_data = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("Diana", "B"),
    ("Eve", "A"),
    ("Frank", "C")
]

# Group students by grade
grade_groups = {}
for name, grade in students_data:
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append(name)

print(f"Students by grade: {grade_groups}")

# Pattern 3: Dictionary inversion
original = {"a": 1, "b": 2, "c": 1, "d": 3}
# Note: This loses data if values are not unique
inverted = {value: key for key, value in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Better inversion for non-unique values
inverted_multi = {}
for key, value in original.items():
    if value not in inverted_multi:
        inverted_multi[value] = []
    inverted_multi[value].append(key)
print(f"Inverted (multi): {inverted_multi}")

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: Shopping cart
def shopping_cart_example():
    cart = {}
    
    # Add items to cart
    def add_item(item, price, quantity=1):
        if item in cart:
            cart[item]["quantity"] += quantity
        else:
            cart[item] = {"price": price, "quantity": quantity}
    
    def remove_item(item, quantity=None):
        if item in cart:
            if quantity is None:
                del cart[item]
            else:
                cart[item]["quantity"] -= quantity
                if cart[item]["quantity"] <= 0:
                    del cart[item]
    
    def calculate_total():
        return sum(item["price"] * item["quantity"] for item in cart.values())
    
    # Simulate shopping
    add_item("Apple", 1.20, 5)
    add_item("Banana", 0.80, 3)
    add_item("Orange", 1.50, 2)
    add_item("Apple", 1.20, 2)  # Add more apples
    
    print("Shopping Cart:")
    for item, details in cart.items():
        total_price = details["price"] * details["quantity"]
        print(f"{item}: {details['quantity']} @ ${details['price']:.2f} = ${total_price:.2f}")
    
    print(f"Total: ${calculate_total():.2f}")

shopping_cart_example()

# Example 2: Contact management
print("\n--- Contact Management ---")
contacts = {
    "Alice Johnson": {
        "phone": "555-0123",
        "email": "alice@email.com",
        "address": "123 Main St",
        "birthday": "1995-03-15"
    },
    "Bob Smith": {
        "phone": "555-0456",
        "email": "bob@email.com",
        "address": "456 Oak Ave",
        "birthday": "1992-07-22"
    }
}

def search_contact(name):
    """Search for a contact by name"""
    name_lower = name.lower()
    for contact_name, details in contacts.items():
        if name_lower in contact_name.lower():
            return contact_name, details
    return None, None

# Search example
name, details = search_contact("alice")
if details:
    print(f"Found: {name}")
    for key, value in details.items():
        print(f"  {key.title()}: {value}")

# Example 3: Configuration management
print("\n--- Configuration Management ---")
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secret123"
    },
    "logging": {
        "level": "INFO",
        "file": "app.log",
        "max_size": "10MB"
    },
    "features": {
        "enable_cache": True,
        "max_users": 1000,
        "debug_mode": False
    }
}

def get_config_value(path):
    """Get configuration value using dot notation"""
    keys = path.split('.')
    value = config
    for key in keys:
        value = value.get(key)
        if value is None:
            return None
    return value

# Usage examples
db_host = get_config_value("database.host")
log_level = get_config_value("logging.level")
cache_enabled = get_config_value("features.enable_cache")

print(f"Database host: {db_host}")
print(f"Log level: {log_level}")
print(f"Cache enabled: {cache_enabled}")

# ============================================================================
# PERFORMANCE AND MEMORY CONSIDERATIONS
# ============================================================================

print("\n=== Performance Tips ===")

# Tip 1: Use get() instead of checking key existence + accessing
sample_dict = {"a": 1, "b": 2, "c": 3}

# Slower
# if "d" in sample_dict:
#     value = sample_dict["d"]
# else:
#     value = 0

# Faster
value = sample_dict.get("d", 0)
print(f"Value for 'd': {value}")

# Tip 2: Use dict.setdefault() for initialization
data = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]

# Building grouped data efficiently
grouped = {}
for key, value in data:
    grouped.setdefault(key, []).append(value)
print(f"Grouped data: {grouped}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. Dictionary Basics:
   - Dictionaries store key-value pairs
   - Keys must be immutable (strings, numbers, tuples)
   - Values can be any type
   - Dictionaries are mutable and ordered (Python 3.7+)

2. Creating Dictionaries:
   - Literal syntax: {"key": "value"}
   - dict() constructor
   - dict(zip(keys, values))
   - Dictionary comprehensions

3. Accessing Values:
   - dict[key] - raises KeyError if key doesn't exist
   - dict.get(key, default) - returns default if key doesn't exist
   - Use 'in' operator to check key existence

4. Common Methods:
   - keys(), values(), items() - return dictionary views
   - pop(key) - remove and return value
   - update(other) - merge dictionaries
   - setdefault(key, default) - get or set default value

5. Dictionary Comprehensions:
   - {key_expr: value_expr for item in iterable}
   - Can include conditions
   - More readable than loops for simple transformations

6. Best Practices:
   - Use get() instead of direct key access when key might not exist
   - Use meaningful key names
   - Consider using collections.defaultdict for grouping
   - Be careful with nested dictionary access

Common Patterns:
- Frequency counting
- Data grouping
- Configuration management
- Caching/memoization
- Database-like operations

Performance Notes:
- Dictionary lookup is O(1) average case
- Use get() instead of checking existence + access
- setdefault() is efficient for list initialization
- Dictionary comprehensions are generally faster than loops
"""

print("\n" + "="*50)
print("END OF MODULE 02 - DICTIONARIES")
print("="*50)
