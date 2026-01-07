# Data Structures and Algorithms (DSA) 🧮

A practical, hands-on DSA track with comprehensive notes, interactive quizzes, and clean Python examples. Master algorithms and data structures essential for technical interviews and competitive programming.

## 🎯 What You'll Learn

- **Core Data Structures**: Arrays, Strings, Linked Lists, Stacks, Queues, Trees, Graphs, Heaps
- **Essential Algorithms**: Sorting, Searching, Recursion, Dynamic Programming, Greedy Algorithms
- **Problem-Solving Patterns**: Two Pointers, Sliding Window, Backtracking, Bit Manipulation
- **Complexity Analysis**: Time and space complexity for every algorithm
- **Interview Preparation**: LeetCode-style problems with detailed solutions

---

## 📚 Course Structure

### Beginner Track (Weeks 1-6)

#### [00_Overview](./00_Overview/) - Start Here! ⭐
- Big-O notation and complexity analysis
- Common problem-solving patterns
- How to approach DSA problems

#### [01_Arrays](./01_Arrays/) 📊
- **Topics**: Indexing, traversal, two pointers, sliding window, Kadane's algorithm
- **Must-solve**: Two Sum, Maximum Subarray, Rotate Array
- **Resources**: [Comprehensive Notes](./01_Arrays/notes.md) | [Interactive Quiz](./01_Arrays/QUIZ.md)
- **Problems**: `two_sum.py`, `kadane.py`, `rotate_array.py`

#### [02_Strings](./02_Strings/) 📝
- **Topics**: Palindromes, anagrams, pattern matching
- **Patterns**: Sliding window, two pointers, hashing
- **Common problems**: Valid palindrome, longest substring, group anagrams

#### [03_Linked_List](./03_Linked_List/) 🔗
- **Topics**: Traversal, reversal, cycle detection, merge operations
- **Key problems**: Reverse linked list, detect cycle, merge sorted lists
- **Techniques**: Fast/slow pointers, dummy nodes

### Intermediate Track (Weeks 7-12)

#### [04_Stacks_Queues](./04_Stacks_Queues/) 📚
- **Topics**: LIFO/FIFO operations, monotonic stacks
- **Problems**: Valid parentheses, MinStack, Daily temperatures
- **Applications**: Expression evaluation, browser history

#### [05_Trees](./05_Trees/) 🌳
- **Topics**: Binary trees, BST, traversals (inorder, preorder, postorder, level-order)
- **Key concepts**: Recursion, DFS, BFS
- **Problems**: Maximum depth, validate BST, lowest common ancestor

#### [08_Graphs](./08_Graphs/) 🕸️
- **Topics**: Adjacency lists, BFS, DFS, shortest paths
- **Algorithms**: Dijkstra's, topological sort
- **Problems**: Number of islands, course schedule, shortest path

### Advanced Track (Weeks 13-16)

#### [09_Sorting_Searching](./09_Sorting_Searching/) 🔍
- **Sorting**: Quick sort, merge sort, heap sort
- **Searching**: Binary search and variations
- **Complexity**: Time/space analysis for each algorithm

#### [11_Dynamic_Programming](./11_Dynamic_Programming/) 💎
- **Concepts**: Memoization vs tabulation
- **Patterns**: Fibonacci, LCS, LIS, knapsack, coin change
- **Approach**: Identify overlapping subproblems

---

## 🗺️ Learning Path

### Path 1: Complete Beginner (16 weeks)
```
Week 1-2:   Overview + Arrays fundamentals
Week 3-4:   Strings and basic patterns
Week 5-6:   Linked Lists
Week 7-8:   Stacks and Queues
Week 9-10:  Trees (Binary Trees, BST)
Week 11-12: Graphs basics
Week 13-14: Sorting and Searching
Week 15-16: Introduction to Dynamic Programming
```

### Path 2: Interview Preparation (8-10 weeks)
```
Week 1:     Arrays (Two Pointers, Sliding Window, Kadane's)
Week 2:     Strings + Hash Tables
Week 3-4:   Linked Lists, Stacks, Queues
Week 5-6:   Trees (all traversals + BST operations)
Week 7:     Graphs (BFS, DFS, basic algorithms)
Week 8:     Sorting/Searching + Binary Search variations
Week 9-10:  Dynamic Programming (common patterns)
```

---

## 📖 How to Use This Repository

### 1. Start with Overview
Begin with `00_Overview/` to understand Big-O notation and problem-solving approaches.

### 2. Follow Sequential Learning
Work through folders in order (01 → 02 → 03...). Each builds on previous concepts.

### 3. Study the Notes
Read the comprehensive `notes.md` in each folder for:
- Key concepts and explanations
- Common patterns
- Complexity analysis
- Pitfalls to avoid

### 4. Take the Quiz
Test your understanding with interactive quizzes (where available):
- Multiple choice questions
- Code analysis problems
- Complexity questions

### 5. Practice with Examples
Run and modify the provided Python files:
```bash
# From repository root
python ./DSA/01_Arrays/two_sum.py
python ./DSA/05_Trees/traversals.py
```

### 6. Solve Problems
- Start with easier problems in each section
- Progress to harder variations
- Try to solve before looking at solutions
- Analyze time and space complexity

---

## 🎯 Problem-Solving Strategy

### The UPER Framework

1. **Understand**: Read problem carefully, identify inputs/outputs, constraints
2. **Plan**: Choose appropriate data structure and algorithm
3. **Execute**: Write clean, working code
4. **Review**: Test with edge cases, optimize if needed

### Complexity Analysis Checklist

For every solution, ask:
- ⏱️ What's the time complexity?
- 💾 What's the space complexity?
- 🎯 Can it be optimized?
- 🧪 What are the edge cases?

---

## 🛠️ Setup & Prerequisites

### Requirements
- Python 3.9+ (Python 3.7+ works for most examples)
- Basic Python knowledge (variables, functions, loops)
- Text editor or IDE (VS Code, PyCharm recommended)

### Running Examples

**Method 1: Direct execution**
```bash
cd DSA/01_Arrays
python two_sum.py
```

**Method 2: From repository root**
```bash
# Windows PowerShell
python .\\DSA\\01_Arrays\\two_sum.py

# Linux/Mac
python ./DSA/01_Arrays/two_sum.py
```

---

## 📊 Recommended Practice Platforms

- **[LeetCode](https://leetcode.com/)** - Most popular, great for interview prep
- **[NeetCode](https://neetcode.io/)** - Curated problem lists with patterns
- **[HackerRank](https://www.hackerrank.com/)** - Good for beginners
- **[Codeforces](https://codeforces.com/)** - Competitive programming
- **[GeeksforGeeks](https://www.geeksforgeeks.org/)** - Comprehensive theory and practice

---

## 📚 Additional Resources

### Learning Resources
- [VisuAlgo](https://visualgo.net/) - Algorithm visualizations
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- Referenced video series: [YouTube Playlist](https://www.youtube.com/playlist?list=PLGtXWdsgkXsS39pJdWsd5JF-Qg52rrPcy)

### Books (Recommended)
- "Cracking the Coding Interview" by Gayle Laakmann McDowell
- "Introduction to Algorithms" by CLRS
- "Grokking Algorithms" by Aditya Bhargava

---

## 🎓 Success Tips

### For Interview Preparation
1. **Practice regularly**: Solve 1-2 problems daily
2. **Time yourself**: Practice under interview conditions
3. **Explain your approach**: Talk through solutions out loud
4. **Review solutions**: Learn from optimal approaches
5. **Focus on patterns**: Recognize common problem types

### For Long-term Mastery
1. **Understand, don't memorize**: Focus on concepts, not rote learning
2. **Teach others**: Explain solutions to solidify understanding
3. **Implement from scratch**: Code algorithms without looking
4. **Analyze complexity**: Always think about time and space

---

## ✅ Progress Tracking

### Beginner Level Checklist
- [ ] Understand Big-O notation
- [ ] Master array traversal and basic operations
- [ ] Solve 20+ easy problems
- [ ] Understand recursion basics
- [ ] Implement basic sorting algorithms

### Intermediate Level Checklist
- [ ] Master two pointers and sliding window
- [ ] Understand tree traversals (DFS, BFS)
- [ ] Solve 50+ medium problems
- [ ] Implement common graph algorithms
- [ ] Understand basic dynamic programming

### Advanced Level Checklist
- [ ] Solve 20+ hard problems
- [ ] Master advanced DP patterns
- [ ] Implement advanced graph algorithms
- [ ] Optimize solutions to O(1) space when possible
- [ ] Participate in coding contests

---

**Ready to start?** Begin with [00_Overview](./00_Overview/) or jump straight to [01_Arrays](./01_Arrays/)!

**Happy Coding!** 🚀💻
