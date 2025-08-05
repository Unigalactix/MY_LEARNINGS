# Python Practice Exercises - Roadmap.sh Aligned
## 🎯 Based on industry-standard Python developer roadmap

> **📊 Legend:** ⏱️ = Estimated time | 🌟 = Difficulty (1-5 stars) | 💡 = Key learning concepts | 🏢 = Industry relevance

---

## � **UPDATED STRUCTURE NOTICE**

**🎉 Your Python learning path has been restructured based on roadmap.sh recommendations!**

### **📁 New Organization:**
- **Phase-based learning** (6 phases + specialization)
- **Industry-aligned curriculum** following current Python best practices
- **Project-driven approach** with portfolio development
- **Modern Python features** (type hints, async/await, dataclasses)
- **Professional development practices** (testing, CI/CD, deployment)

### **📋 Key Documents:**
- 📊 **PROGRESS_TRACKER.md** - Track your learning journey
- 🏗️ **PROJECT_MILESTONES.md** - Professional portfolio projects
- 🗺️ **ROADMAP_BASED_STRUCTURE.md** - Complete learning roadmap
- 📁 **NEW_STRUCTURE_PLAN.md** - Detailed folder reorganization

---

## 📚 **Phase 1: Python Fundamentals (Weeks 1-4)**

### Exercise 1.1: Variables and Data Types (Industry Standards)
**⏱️ 20-25 minutes | 🌟 2/5 | 💡 PEP 8, type hints, modern formatting | 🏢 Essential for all Python roles**

1. Create variables following PEP 8 naming conventions
2. Add type hints to all variable declarations
3. Use f-strings for all string formatting
4. Demonstrate understanding of truthy/falsy values
5. Implement safe type conversion with error handling

**🎯 Professional Requirements:**
```python
from typing import Optional
from decimal import Decimal

# Type-hinted variables with descriptive names
user_age: int = 25
account_balance: Decimal = Decimal('1234.56')
is_authenticated: bool = True
username: Optional[str] = None

# Modern f-string formatting
print(f"User {username or 'Anonymous'} (age {user_age}) has ${account_balance}")
```

**🔍 Assessment Criteria:**
- [ ] All variables follow snake_case convention
- [ ] Type hints used throughout
- [ ] F-strings used for formatting
- [ ] Error handling for type conversions
- [ ] Code passes `flake8` linting

### Exercise 1.2: Modern String Operations
**⏱️ 25-30 minutes | 🌟 2/5 | 💡 F-strings, string methods, validation | 🏢 Used in data processing, APIs**

1. Create a user input validator using string methods
2. Implement email and phone number validation
3. Use f-strings with advanced formatting options
4. Handle Unicode and special characters
5. Create a template system using string formatting

**🎯 Professional Example:**
```python
import re
from typing import Tuple

def validate_email(email: str) -> Tuple[bool, str]:
    """Validate email format and return result with message."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = bool(re.match(pattern, email))
    message = f"✅ Valid email: {email}" if is_valid else f"❌ Invalid email format: {email}"
    return is_valid, message
```

### Exercise 1.3: Data Structures with Modern Python
**⏱️ 30-40 minutes | 🌟 3/5 | 💡 Collections, comprehensions, type hints | 🏢 Core skill for all Python development**
1. Ask the user for their first and last name
2. Create a username by taking the first 3 letters of first name + first 3 letters of last name
3. Convert the username to lowercase
4. Print a welcome message with the username

### Exercise 3: Lists and Basic Operations
1. Create a list of your 5 favorite movies
2. Add 2 more movies to the list
3. Remove one movie from the list
4. Print the list in alphabetical order
5. Print the number of movies in your list

### Exercise 4: Dictionaries
1. Create a dictionary with information about yourself (name, age, city, hobbies)
2. Add a new key-value pair for your favorite color
3. Print all keys in the dictionary
4. Print all values in the dictionary
5. Update your age and print the updated dictionary

### Exercise 5: Control Flow - Conditionals
1. Write a program that asks for a number and determines if it's positive, negative, or zero
2. Create a simple grade calculator:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - Below 60: F
3. Write a program to check if a year is a leap year

### Exercise 6: Loops
1. Print numbers from 1 to 10 using a for loop
2. Print even numbers from 0 to 20 using a while loop
3. Create a multiplication table for a number (ask user for input)
4. Count and print the number of vowels in a given string

### Exercise 6.5: String Formatting (New!)
**⏱️ 15-20 minutes | 🌟 2/5 | 💡 f-strings, .format(), % formatting**

1. Create variables for name, age, and city
2. Print a sentence using f-string formatting
3. Use .format() method to create the same sentence
4. Use % formatting for the same sentence
5. Format a number to 2 decimal places using each method

**💡 Try This:** Create a mad-libs game using string formatting!

### Exercise 6.8: Sets and Tuples (New!)
**⏱️ 20-25 minutes | 🌟 2/5 | 💡 Set operations, tuple unpacking**

1. Create two sets of your favorite foods and a friend's favorite foods
2. Find common foods using set intersection
3. Find unique foods using set difference
4. Create a tuple with coordinate points (x, y, z)
5. Unpack the tuple into separate variables

## 🚀 Intermediate Level Exercises

### Exercise 7: Functions
**⏱️ 30-40 minutes | 🌟 3/5 | 💡 Function definition, parameters, return values**

1. Write a function to calculate the area of a rectangle
2. Create a function that takes a list of numbers and returns the average
3. Write a function to check if a string is a palindrome
4. Create a function that generates the Fibonacci sequence up to n terms

**🔥 Challenge:** Add type hints to all your functions!

### Exercise 7.5: Lambda Functions and Built-ins (New!)
**⏱️ 25-30 minutes | 🌟 3/5 | 💡 Lambda, map(), filter(), reduce()**

1. Use lambda to create a function that squares a number
2. Use map() to apply the square function to a list
3. Use filter() to get even numbers from a list
4. Use reduce() to find the product of all numbers in a list
5. Sort a list of tuples by the second element using lambda

### Exercise 8: List Comprehensions
**⏱️ 25-35 minutes | 🌟 3/5 | 💡 List comprehensions, conditional expressions**
1. Create a list of squares for numbers 1-10 using list comprehension
2. Filter even numbers from a list using list comprehension
3. Create a list of lengths of words in a sentence
4. Generate a list of all combinations of two lists

### Exercise 9: File Handling
1. Write a program to create a text file and write your favorite quotes to it
2. Read the file and count the number of lines
3. Append new quotes to the existing file
4. Create a simple contact book that saves/loads from a file

### Exercise 10: Exception Handling
1. Write a calculator that handles division by zero
2. Create a program that asks for a number and handles invalid input
3. Write a file reader that handles file not found errors
4. Create a function that validates email addresses and raises custom exceptions

### Exercise 11: Classes and Objects
1. Create a `Student` class with name, age, and grades attributes
2. Add methods to calculate average grade and determine if passing
3. Create a `BankAccount` class with deposit, withdraw, and balance methods
4. Implement a simple `Library` system with books and borrowing functionality

## 🎯 Advanced Level Exercises

### Exercise 12: Decorators and Generators
1. Create a decorator that measures function execution time
2. Write a decorator that logs function calls
3. Create a generator that yields prime numbers
4. Create a generator that reads a large file line by line

### Exercise 12.5: Context Managers and JSON (New!)
**⏱️ 30-35 minutes | 🌟 4/5 | 💡 with statements, JSON handling, custom context managers**

1. Use context managers to safely read and write files
2. Parse JSON data from a file and extract specific information
3. Convert Python dictionaries to JSON and save to file
4. Create a custom context manager for database connections
5. Handle JSON parsing errors gracefully

### Exercise 12.8: Type Hints and Dataclasses (New!)
**⏱️ 25-30 minutes | 🌟 4/5 | 💡 Type annotations, dataclasses, mypy**

1. Add type hints to existing functions
2. Create a dataclass for a Person with name, age, and email
3. Use Optional and Union types for flexible parameters
4. Create a dataclass with default values and post-init processing
5. Use typing.Protocol to define interfaces

### Exercise 13: Data Processing
**⏱️ 45-60 minutes | 🌟 4/5 | 💡 File processing, data analysis, visualization**
1. Process a CSV file of student grades and calculate statistics
2. Create a word frequency counter for a text file
3. Parse and analyze log files to find error patterns
4. Build a simple data visualization using matplotlib

### Exercise 14: Web and APIs
1. Use the `requests` library to fetch data from a public API
2. Parse JSON data and extract specific information
3. Create a simple web scraper using BeautifulSoup
4. Build a weather app that fetches current weather data

### Exercise 15: Database Operations
1. Create a SQLite database for a todo list application
2. Implement CRUD operations (Create, Read, Update, Delete)
3. Build a simple inventory management system
4. Create a database-backed address book

## 🏗️ Project-Based Exercises

> **💡 Pro Tip:** Start each project with pseudocode and break it into smaller functions!

### Project 1: Number Guessing Game
**⏱️ 2-3 hours | 🌟 2/5 | 💡 Random, loops, conditionals, file I/O**

**Core Features:**
- Computer generates a random number between 1-100
- User has limited attempts to guess
- Provide hints (higher/lower)
- Keep track of high scores
- Allow replay functionality

**🚀 Extension Ideas:**
- Different difficulty levels (range and attempts)
- Multiplayer mode
- GUI version with tkinter
- Sound effects and animations

**📝 Starter Template:**
```python
import random

def generate_number(min_val=1, max_val=100):
    # Your code here
    pass

def get_user_guess():
    # Handle input validation
    pass

def main_game_loop():
    # Main game logic
    pass
```

### Project 2: Todo List Application
**⏱️ 3-4 hours | 🌟 3/5 | 💡 Classes, file handling, data structures**
Build a command-line todo list manager:
- Add, remove, and mark tasks as complete
- Save tasks to a file
- Priority levels for tasks
- Due date functionality
- Search and filter capabilities

### Project 3: Simple Calculator
Create a calculator application:
- Basic arithmetic operations
- Memory functions (store, recall, clear)
- History of calculations
- Error handling for invalid operations
- Scientific calculator functions (optional)

### Project 4: Text-Based Adventure Game
Develop a simple adventure game:
- Multiple rooms/locations
- Inventory system
- Character stats (health, items)
- Save/load game functionality
- Interactive storyline

### Project 5: Personal Finance Tracker
Build a personal finance application:
- Track income and expenses
- Categorize transactions
- Generate monthly reports
- Data visualization with charts
- Budget planning and alerts

### Project 6: Web Scraper
Create a web scraping application:
- Scrape news headlines from multiple sources
- Extract product prices from e-commerce sites
- Monitor job postings for specific keywords
- Save data to different formats (CSV, JSON)
- Schedule automatic scraping

## 🧪 Testing and Debugging Exercises

### Exercise 16: Unit Testing
1. Write unit tests for your calculator functions
2. Test edge cases for your palindrome checker
3. Create tests for your BankAccount class
4. Write integration tests for your todo list application

### Exercise 17: Debugging Practice
1. Debug a program with logical errors
2. Fix syntax errors in provided code snippets
3. Resolve runtime errors in file handling code
4. Optimize slow-performing code

## 📊 Data Science Exercises

### Exercise 18: Data Analysis with Pandas
1. Load and explore a dataset (CSV file)
2. Clean data (handle missing values, duplicates)
3. Perform basic statistical analysis
4. Create data visualizations
5. Export processed data

### Exercise 19: Machine Learning Basics
1. Implement a simple linear regression
2. Create a basic classification model
3. Analyze model performance
4. Visualize results and predictions

## ⚡ Quick Challenges & Code Golf (New!)

### 5-Minute Challenges
**Perfect for daily practice sessions!**

1. **FizzBuzz** - Print 1-100, but "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both
2. **Reverse Words** - Reverse each word in a sentence while keeping word order
3. **Two Sum** - Find two numbers in a list that add up to a target
4. **Anagram Checker** - Check if two strings are anagrams
5. **Prime Check** - Determine if a number is prime in the most efficient way

### Code Golf Challenges
**Write the shortest Python code possible!**

1. Calculate factorial of n
2. Generate first 10 Fibonacci numbers
3. Check if a string is a palindrome
4. Remove duplicates from a list while preserving order
5. Count word frequency in a sentence

## 🧩 Coding Interview Prep (New!)

### Easy Level
1. **Valid Parentheses** - Check if brackets are properly matched
2. **Merge Two Sorted Lists** - Combine two sorted lists
3. **Roman to Integer** - Convert Roman numerals to integers
4. **Longest Common Prefix** - Find common prefix among strings

### Medium Level
1. **Group Anagrams** - Group words that are anagrams
2. **Longest Substring** - Find longest substring without repeating characters
3. **Container With Most Water** - Find maximum area between vertical lines
4. **3Sum** - Find three numbers that sum to zero

## 🎯 Self-Assessment Quizzes (New!)

### After Beginner Section
**Test your understanding before moving on!**

1. What's the difference between `==` and `is`?
2. How do you handle index errors when accessing list elements?
3. What's the output of `print([1, 2] * 3)`?
4. When should you use a tuple instead of a list?

### After Intermediate Section
1. What's the difference between `@staticmethod` and `@classmethod`?
2. How does Python's garbage collection work?
3. What's the GIL and why does it matter?
4. Explain the difference between deep and shallow copy.

## 🌐 Web Development Exercises

### Exercise 20: Flask Web Application
1. Create a simple "Hello World" web app
2. Build a form that accepts user input
3. Create a multi-page application
4. Implement basic authentication
5. Connect to a database

## 💡 Tips for Practice

### 📈 Progress Tracking (New!)
**Keep track of your learning journey!**

Create a simple progress tracker:
```
□ Beginner Exercises (1-6) - Date completed: ___
□ String Formatting & Sets - Date completed: ___
□ Intermediate Exercises (7-11) - Date completed: ___
□ Advanced Exercises (12-20) - Date completed: ___
□ Quick Challenges (5 completed) - Date completed: ___
□ First Project Completed - Date completed: ___
□ All Projects Completed - Date completed: ___
```

### 🎯 Learning Strategies

1. **Start Simple**: Begin with basic exercises and gradually increase complexity
2. **Code Daily**: Practice coding every day, even if just for 15-30 minutes
3. **Active Learning**: Type code instead of copying - muscle memory matters!
4. **Explain Your Code**: If you can't explain it, you don't understand it
5. **Build Projects**: Apply your knowledge by building real projects
6. **Debug Actively**: Don't fear errors; they're learning opportunities
7. **Document Your Code**: Write clear comments and docstrings
8. **Use Version Control**: Learn Git to track your progress
9. **Seek Feedback**: Share your code with others for review
10. **Stay Curious**: Explore new libraries and Python features

### 🔧 Essential Tools & Setup
**Optimize your learning environment:**

- **IDE**: VS Code, PyCharm, or Sublime Text
- **Version Control**: Git and GitHub
- **Virtual Environments**: `venv` or `conda`
- **Code Formatting**: `black` and `flake8`
- **Testing**: `pytest` framework
- **Documentation**: Learn to read Python docs effectively

### 🎪 Fun Practice Ideas

1. **Code a Day**: Write one small program daily
2. **Recreate Games**: Implement classic games (Snake, Pong, Tic-tac-toe)
3. **Automation Scripts**: Automate boring tasks in your daily life
4. **API Exploration**: Play with interesting APIs (weather, jokes, quotes)
5. **Code Golf**: Challenge yourself to write the shortest solution
6. **Teaching**: Explain concepts to others or write blog posts

## 📚 Additional Resources

### 🏆 Practice Platforms
- **Beginner Friendly**: Codecademy, Python.org exercises, Repl.it
- **Coding Challenges**: HackerRank, LeetCode, Codewars, Exercism
- **Project Ideas**: GitHub awesome-python repositories
- **Interactive Learning**: freeCodeCamp, Real Python tutorials

### 📖 Essential Reading
- **Books**: 
  - "Automate the Boring Stuff with Python" (Beginner)
  - "Python Crash Course" (Beginner to Intermediate)
  - "Effective Python" (Intermediate)
  - "Fluent Python" (Advanced)
- **Documentation**: Official Python documentation
- **Blogs**: Real Python, Planet Python, Python Software Foundation

### 🌟 Communities & Support
- **Reddit**: r/Python, r/learnpython
- **Discord/Slack**: Python Discord, Python Developers Slack
- **Forums**: Stack Overflow, Python Forum
- **Local**: Python meetups in your area

### 🎥 Video Resources
- **YouTube Channels**: Corey Schafer, Real Python, Sentdex
- **Courses**: CS50P (Harvard), Python for Everybody (Coursera)
- **Live Coding**: Twitch programming streams

---

**Happy Coding!** 🐍✨

**🎯 Your Learning Journey Starts Here!**

Remember: The key to mastering Python is consistent practice and building real projects. Start with Exercise 1 today and track your progress!

> **💪 Challenge yourself:** Complete at least one exercise every day for the next 30 days!
