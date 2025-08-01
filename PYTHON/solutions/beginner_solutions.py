# ================================
# SOLUTIONS: Python Beginner Exercises
# ================================

# Exercise 1: Variables and Data Types
print("=== Exercise 1: Variables and Data Types ===")

# 1. Create variables
name = "Alice"
age = 25
height = 5.6  # feet
is_student = True

# 2. Print with descriptive messages
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My height is {height} feet")
print(f"Am I a student? {is_student}")

# 3. Convert age to string and concatenate
age_str = str(age)
name_age = name + " is " + age_str + " years old"
print(name_age)

# 4. Calculate age in days
age_in_days = age * 365
print(f"My age in days is approximately {age_in_days} days")

print()

# Exercise 2: Strings and Input
print("=== Exercise 2: Strings and Input ===")

# Simulating user input (in real program, use input())
first_name = "John"  # input("Enter your first name: ")
last_name = "Smith"  # input("Enter your last name: ")

# Create username
username = (first_name[:3] + last_name[:3]).lower()
print(f"Your username is: {username}")

# Welcome message
print(f"Welcome, {username}!")

print()

# Exercise 3: Lists and Basic Operations
print("=== Exercise 3: Lists and Basic Operations ===")

# 1. Create list of favorite movies
movies = ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Pulp Fiction"]

# 2. Add 2 more movies
movies.append("Goodfellas")
movies.append("The Godfather")

# 3. Remove one movie
movies.remove("Pulp Fiction")

# 4. Print in alphabetical order
print("Movies in alphabetical order:")
for movie in sorted(movies):
    print(f"- {movie}")

# 5. Print number of movies
print(f"Total number of movies: {len(movies)}")

print()

# Exercise 4: Dictionaries
print("=== Exercise 4: Dictionaries ===")

# 1. Create dictionary about yourself
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"]
}

# 2. Add favorite color
person["favorite_color"] = "blue"

# 3. Print all keys
print("Keys:", list(person.keys()))

# 4. Print all values
print("Values:", list(person.values()))

# 5. Update age
person["age"] = 26
print("Updated dictionary:", person)

print()

# Exercise 5: Control Flow - Conditionals
print("=== Exercise 5: Control Flow - Conditionals ===")

# 1. Check if number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

test_number = -5
print(f"{test_number} is {check_number(test_number)}")

# 2. Grade calculator
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_score = 85
print(f"Score {test_score} gets grade: {calculate_grade(test_score)}")

# 3. Leap year checker
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

test_year = 2024
print(f"{test_year} is a leap year: {is_leap_year(test_year)}")

print()

# Exercise 6: Loops
print("=== Exercise 6: Loops ===")

# 1. Print numbers 1 to 10 using for loop
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Print even numbers 0 to 20 using while loop
print("Even numbers 0 to 20:")
num = 0
while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
print()

# 3. Multiplication table
def multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

multiplication_table(7)

# 4. Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

test_string = "Hello World"
vowel_count = count_vowels(test_string)
print(f"Number of vowels in '{test_string}': {vowel_count}")

print("\n=== All Beginner Exercises Complete! ===")
