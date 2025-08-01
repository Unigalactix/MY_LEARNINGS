"""
05_OBJECT_ORIENTED_PROGRAMMING - CLASSES AND OBJECTS
=====================================================

This module covers the fundamentals of Object-Oriented Programming (OOP) in Python:
- Class definition and object creation
- Instance variables and methods
- Constructor (__init__) method
- Instance vs class attributes
- Method types (instance, class, static)
- Encapsulation basics

Learning Objectives:
- Understand OOP concepts and terminology
- Create classes and instantiate objects
- Work with instance variables and methods
- Master the constructor pattern
- Learn about different method types
"""

# ============================================================================
# BASIC CLASS DEFINITION
# ============================================================================

print("=== Basic Class Definition ===")

# Simple class definition
class Dog:
    """A simple class representing a dog."""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, breed, age):
        """Initialize a new dog instance."""
        # Instance attributes (unique to each instance)
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Return basic information about the dog."""
        return f"{self.name} is a {self.age}-year-old {self.breed}"

# Creating objects (instances)
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "German Shepherd", 5)

print(f"Dog 1: {dog1.get_info()}")
print(f"Dog 2: {dog2.get_info()}")
print(f"Dog 1 barks: {dog1.bark()}")
print(f"Both dogs are: {Dog.species}")

# ============================================================================
# INSTANCE VARIABLES AND METHODS
# ============================================================================

print("\n=== Instance Variables and Methods ===")

class BankAccount:
    """A class representing a bank account."""
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a bank account."""
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew ${amount:.2f}")
                return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Insufficient funds"
        else:
            return "Withdrawal amount must be positive"
    
    def get_balance(self):
        """Get current account balance."""
        return f"Current balance: ${self.balance:.2f}"
    
    def get_transaction_history(self):
        """Get transaction history."""
        if self.transaction_history:
            return "Transaction History:\n" + "\n".join(self.transaction_history)
        else:
            return "No transactions yet"

# Using the BankAccount class
account = BankAccount("Alice Johnson", 1000)
print(f"Account holder: {account.account_holder}")
print(account.get_balance())

print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # Should fail
print(account.get_transaction_history())

# ============================================================================
# CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ============================================================================

print("\n=== Class vs Instance Attributes ===")

class Employee:
    """Employee class demonstrating class vs instance attributes."""
    
    # Class attributes (shared by all instances)
    company_name = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, position, salary):
        """Initialize an employee."""
        # Instance attributes (unique to each instance)
        self.name = name
        self.position = position
        self.salary = salary
        
        # Update class attribute
        Employee.employee_count += 1
    
    def get_details(self):
        """Get employee details."""
        return f"{self.name} - {self.position} at {self.company_name}"
    
    def give_raise(self, amount):
        """Give employee a raise."""
        self.salary += amount
        return f"{self.name} received a ${amount} raise. New salary: ${self.salary}"

# Creating employees
emp1 = Employee("John Smith", "Developer", 75000)
emp2 = Employee("Jane Doe", "Designer", 70000)

print(f"Company: {Employee.company_name}")
print(f"Total employees: {Employee.employee_count}")
print(f"Employee 1: {emp1.get_details()}")
print(f"Employee 2: {emp2.get_details()}")

print(emp1.give_raise(5000))

# ============================================================================
# METHOD TYPES
# ============================================================================

print("\n=== Method Types ===")

class Calculator:
    """Calculator class demonstrating different method types."""
    
    # Class attribute
    precision = 2
    
    def __init__(self, name):
        """Initialize calculator with a name."""
        self.name = name
    
    # Instance method (operates on instance data)
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        print(f"{self.name} calculated: {a} + {b} = {result}")
        return result
    
    # Class method (operates on class data)
    @classmethod
    def set_precision(cls, precision):
        """Set the precision for all calculators."""
        cls.precision = precision
        print(f"Precision set to {precision} for all calculators")
    
    @classmethod
    def create_scientific_calculator(cls):
        """Factory method to create a scientific calculator."""
        return cls("Scientific Calculator")
    
    # Static method (doesn't need class or instance data)
    @staticmethod
    def is_even(number):
        """Check if a number is even."""
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        """Calculate factorial of a number."""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Using different method types
calc1 = Calculator("Basic Calculator")
calc1.add(5, 3)

# Using class method
Calculator.set_precision(3)
print(f"Current precision: {Calculator.precision}")

# Using factory method
sci_calc = Calculator.create_scientific_calculator()
sci_calc.add(10, 20)

# Using static methods
print(f"Is 10 even? {Calculator.is_even(10)}")
print(f"5! = {Calculator.factorial(5)}")

# ============================================================================
# ENCAPSULATION AND PRIVATE ATTRIBUTES
# ============================================================================

print("\n=== Encapsulation and Private Attributes ===")

class Person:
    """Person class demonstrating encapsulation."""
    
    def __init__(self, name, age):
        """Initialize a person."""
        self.name = name  # Public attribute
        self._age = age   # Protected attribute (convention: single underscore)
        self.__ssn = None # Private attribute (name mangling: double underscore)
    
    def get_age(self):
        """Get person's age (getter method)."""
        return self._age
    
    def set_age(self, age):
        """Set person's age with validation (setter method)."""
        if 0 <= age <= 150:
            self._age = age
        else:
            raise ValueError("Age must be between 0 and 150")
    
    def set_ssn(self, ssn):
        """Set SSN (private information)."""
        if len(ssn) == 9 and ssn.isdigit():
            self.__ssn = ssn
        else:
            raise ValueError("SSN must be 9 digits")
    
    def _get_ssn_last_four(self):
        """Protected method to get last 4 digits of SSN."""
        if self.__ssn:
            return self.__ssn[-4:]
        return None
    
    def display_info(self):
        """Display person information."""
        ssn_display = f"***-**-{self._get_ssn_last_four()}" if self._get_ssn_last_four() else "Not provided"
        return f"Name: {self.name}, Age: {self._age}, SSN: {ssn_display}"

# Using encapsulation
person = Person("Alice Smith", 30)
print(person.display_info())

# Accessing public attribute
print(f"Name: {person.name}")

# Using getter/setter methods
print(f"Age: {person.get_age()}")
person.set_age(31)
print(f"New age: {person.get_age()}")

# Setting private information
person.set_ssn("123456789")
print(person.display_info())

# Demonstrating access levels
print(f"Public name: {person.name}")           # OK
print(f"Protected age: {person._age}")         # Works but not recommended
# print(f"Private SSN: {person.__ssn}")       # Would cause AttributeError

# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: Student Management System
class Student:
    """Student class for academic management."""
    
    def __init__(self, student_id, name, major):
        """Initialize a student."""
        self.student_id = student_id
        self.name = name
        self.major = major
        self.grades = {}
        self.credits = 0
    
    def add_grade(self, course, grade, credit_hours):
        """Add a grade for a course."""
        if 0 <= grade <= 100:
            self.grades[course] = {"grade": grade, "credits": credit_hours}
            self.credits += credit_hours
            return f"Added grade {grade} for {course}"
        else:
            return "Grade must be between 0 and 100"
    
    def calculate_gpa(self):
        """Calculate GPA based on grades."""
        if not self.grades:
            return 0.0
        
        total_points = 0
        total_credits = 0
        
        for course_info in self.grades.values():
            grade = course_info["grade"]
            credits = course_info["credits"]
            
            # Convert to 4.0 scale
            if grade >= 97: points = 4.0
            elif grade >= 93: points = 4.0
            elif grade >= 90: points = 3.7
            elif grade >= 87: points = 3.3
            elif grade >= 83: points = 3.0
            elif grade >= 80: points = 2.7
            elif grade >= 77: points = 2.3
            elif grade >= 73: points = 2.0
            elif grade >= 70: points = 1.7
            elif grade >= 67: points = 1.3
            elif grade >= 65: points = 1.0
            else: points = 0.0
            
            total_points += points * credits
            total_credits += credits
        
        return total_points / total_credits if total_credits > 0 else 0.0
    
    def get_transcript(self):
        """Generate student transcript."""
        transcript = f"TRANSCRIPT\n"
        transcript += f"Student: {self.name} (ID: {self.student_id})\n"
        transcript += f"Major: {self.major}\n"
        transcript += "-" * 40 + "\n"
        
        for course, info in self.grades.items():
            transcript += f"{course}: {info['grade']} ({info['credits']} credits)\n"
        
        transcript += "-" * 40 + "\n"
        transcript += f"Total Credits: {self.credits}\n"
        transcript += f"GPA: {self.calculate_gpa():.2f}"
        
        return transcript

# Using Student class
student = Student("S12345", "John Doe", "Computer Science")
student.add_grade("Math 101", 85, 3)
student.add_grade("CS 101", 92, 4)
student.add_grade("Physics 101", 78, 3)

print(student.get_transcript())

# Example 2: Shopping Cart System
class Product:
    """Product class for e-commerce."""
    
    def __init__(self, id, name, price, stock):
        """Initialize a product."""
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        """Update stock quantity."""
        if self.stock + quantity >= 0:
            self.stock += quantity
            return True
        return False
    
    def __str__(self):
        """String representation of product."""
        return f"{self.name} (${self.price:.2f}) - Stock: {self.stock}"

class ShoppingCart:
    """Shopping cart for e-commerce system."""
    
    def __init__(self):
        """Initialize empty shopping cart."""
        self.items = {}  # {product_id: {"product": Product, "quantity": int}}
    
    def add_item(self, product, quantity):
        """Add item to cart."""
        if product.stock >= quantity:
            if product.id in self.items:
                self.items[product.id]["quantity"] += quantity
            else:
                self.items[product.id] = {"product": product, "quantity": quantity}
            return f"Added {quantity} x {product.name} to cart"
        else:
            return f"Insufficient stock. Only {product.stock} available"
    
    def remove_item(self, product_id, quantity=None):
        """Remove item from cart."""
        if product_id in self.items:
            if quantity is None:
                removed = self.items[product_id]
                del self.items[product_id]
                return f"Removed all {removed['product'].name} from cart"
            else:
                if self.items[product_id]["quantity"] >= quantity:
                    self.items[product_id]["quantity"] -= quantity
                    if self.items[product_id]["quantity"] == 0:
                        del self.items[product_id]
                    return f"Removed {quantity} items from cart"
                else:
                    return "Cannot remove more items than in cart"
        else:
            return "Item not in cart"
    
    def calculate_total(self):
        """Calculate total cart value."""
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["quantity"]
        return total
    
    def get_cart_summary(self):
        """Get cart summary."""
        if not self.items:
            return "Cart is empty"
        
        summary = "SHOPPING CART\n" + "-" * 30 + "\n"
        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            line_total = product.price * quantity
            summary += f"{product.name} x {quantity} = ${line_total:.2f}\n"
        
        summary += "-" * 30 + "\n"
        summary += f"Total: ${self.calculate_total():.2f}"
        return summary

# Using shopping cart system
products = [
    Product("P001", "Laptop", 999.99, 10),
    Product("P002", "Mouse", 29.99, 50),
    Product("P003", "Keyboard", 79.99, 30)
]

cart = ShoppingCart()
print(cart.add_item(products[0], 1))  # Add laptop
print(cart.add_item(products[1], 2))  # Add 2 mice
print(cart.add_item(products[2], 1))  # Add keyboard

print("\n" + cart.get_cart_summary())

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

"""
Key Points to Remember:

1. Class Definition:
   - Use 'class' keyword with CapitalCase naming
   - Include docstrings for documentation
   - Define __init__ method for initialization

2. Instance vs Class Attributes:
   - Instance attributes: unique to each object (self.attribute)
   - Class attributes: shared by all instances (ClassName.attribute)
   - Instance attributes override class attributes

3. Method Types:
   - Instance methods: operate on instance data (self as first parameter)
   - Class methods: operate on class data (@classmethod, cls as first parameter)
   - Static methods: independent utility functions (@staticmethod)

4. Encapsulation:
   - Public: normal attributes (no underscore)
   - Protected: single underscore prefix (convention only)
   - Private: double underscore prefix (name mangling)

5. Constructor (__init__):
   - Called automatically when object is created
   - Initialize instance attributes
   - Can have default parameters

6. Best Practices:
   - Use meaningful class and method names
   - Keep classes focused (Single Responsibility)
   - Provide proper documentation
   - Use encapsulation appropriately
   - Validate input in methods

OOP Benefits:
- Code organization and reusability
- Data encapsulation and security
- Easier maintenance and debugging
- Real-world modeling
- Polymorphism and inheritance (covered in next modules)

Common Patterns:
- Data containers (like Student, Product)
- State machines (like BankAccount)
- Factory methods for object creation
- Getter/setter methods for controlled access
"""

print("\n" + "="*50)
print("END OF MODULE 05 - CLASSES AND OBJECTS")
print("="*50)
