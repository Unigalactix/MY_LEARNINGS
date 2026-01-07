# Coding Challenges Template 💻

This template provides a structure for creating hands-on coding challenges throughout the learning materials.

## How to Use This Template

1. Copy this template to any folder (e.g., `PYTHON/01_Basics/CHALLENGES.md`)
2. Replace sample challenges with topic-specific exercises
3. Provide multiple difficulty levels
4. Include clear success criteria and test cases

---

## Coding Challenges: [Topic Name]

**Total Challenges**: [Number]  
**Estimated Time**: [X] hours  
**Prerequisites**: [List required knowledge]

**Instructions**: 
- Try to solve challenges independently before checking solutions
- Test your code with the provided test cases
- Optimize your solution after getting it working
- Compare your approach with the provided solution

---

## Challenge #1: [Challenge Title] ⭐

**Difficulty**: Beginner  
**Time**: 10-15 minutes  
**Concepts**: [List key concepts being practiced]

### Problem Statement

[Clear description of what needs to be built/solved]

**Example**:
```
Input: [sample input]
Output: [expected output]
```

### Requirements

- ✅ Requirement 1
- ✅ Requirement 2
- ✅ Requirement 3

### Test Cases

```python
# Test Case 1
input_1 = [test input]
expected_output_1 = [expected result]

# Test Case 2
input_2 = [test input]
expected_output_2 = [expected result]

# Test Case 3 (Edge case)
input_3 = [edge case input]
expected_output_3 = [expected result]
```

### Hints

<details>
<summary>Click for Hint 1</summary>

[First hint - gentle nudge in right direction]

</details>

<details>
<summary>Click for Hint 2</summary>

[Second hint - more specific guidance]

</details>

<details>
<summary>Click for Hint 3</summary>

[Third hint - nearly gives away the approach]

</details>

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
def solution_function(input_param):
    """
    Clear docstring explaining the approach
    
    Args:
        input_param: Description of parameter
    
    Returns:
        Description of return value
    
    Time Complexity: O(?)
    Space Complexity: O(?)
    """
    # Step 1: [Explanation]
    
    # Step 2: [Explanation]
    
    # Step 3: [Explanation]
    
    return result


# Test the solution
print(solution_function(input_1))  # Expected: expected_output_1
print(solution_function(input_2))  # Expected: expected_output_2
print(solution_function(input_3))  # Expected: expected_output_3
```

**Explanation**:
- **Approach**: [Describe the algorithm/approach]
- **Why it works**: [Explain the logic]
- **Complexity Analysis**: 
  - Time: O(?) because [reason]
  - Space: O(?) because [reason]

**Alternative Solutions**:
1. [Alternative approach 1] - Pros and Cons
2. [Alternative approach 2] - Pros and Cons

</details>

---

## Challenge #2: [Challenge Title] ⭐⭐

**Difficulty**: Intermediate  
**Time**: 20-30 minutes  
**Concepts**: [List key concepts]

### Problem Statement

[More complex problem description]

**Example 1**:
```
Input: [input]
Output: [output]
Explanation: [why this is the output]
```

**Example 2**:
```
Input: [input]
Output: [output]
Explanation: [why this is the output]
```

### Requirements

- ✅ [Functional requirement]
- ✅ [Performance requirement]
- ✅ [Edge case handling]
- ✅ [Code quality requirement]

### Constraints

- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

### Test Cases

```python
# Test Case 1: Normal case
test_case_1 = {
    'input': [input],
    'expected': [output],
    'description': 'Basic functionality'
}

# Test Case 2: Edge case
test_case_2 = {
    'input': [edge case],
    'expected': [output],
    'description': 'Handle edge case'
}

# Test Case 3: Large input
test_case_3 = {
    'input': [large input],
    'expected': [output],
    'description': 'Performance test'
}
```

### Hints

<details>
<summary>Click for Hint 1</summary>

Think about [high-level approach]

</details>

<details>
<summary>Click for Hint 2</summary>

Consider using [data structure or technique]

</details>

<details>
<summary>Click for Hint 3</summary>

The key insight is [specific technique or pattern]

</details>

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# [Well-documented solution code]
```

**Detailed Explanation**:
[Step-by-step walkthrough]

**Key Insights**:
- [Insight 1]
- [Insight 2]
- [Insight 3]

**Common Mistakes to Avoid**:
- [Mistake 1]
- [Mistake 2]

</details>

---

## Challenge #3: [Challenge Title] ⭐⭐⭐

**Difficulty**: Advanced  
**Time**: 45-60 minutes  
**Concepts**: [Advanced concepts]

### Problem Statement

[Complex, real-world scenario or advanced algorithmic problem]

### Requirements

- ✅ [Complex requirement 1]
- ✅ [Complex requirement 2]
- ✅ [Optimization requirement]
- ✅ [Error handling]
- ✅ [Code documentation]

### Test Cases

```python
# Include comprehensive test suite
import pytest  # or unittest

def test_basic_functionality():
    """Test basic use case"""
    pass

def test_edge_cases():
    """Test boundary conditions"""
    pass

def test_performance():
    """Test with large inputs"""
    pass

def test_error_handling():
    """Test invalid inputs"""
    pass
```

### Hints

<details>
<summary>Hint 1: Overall Strategy</summary>

[Strategic guidance]

</details>

<details>
<summary>Hint 2: Key Algorithm</summary>

[Algorithm or pattern to use]

</details>

<details>
<summary>Hint 3: Optimization Technique</summary>

[Optimization approach]

</details>

### Solution

<details>
<summary>Click to reveal solution</summary>

```python
# [Production-quality code with full documentation]
```

**Complete Analysis**:
- **Algorithm**: [Detailed algorithm description]
- **Correctness**: [Proof or explanation of why it works]
- **Complexity**: 
  - Time: O(?) with detailed analysis
  - Space: O(?) with detailed analysis
- **Optimizations**: [What optimizations were made and why]
- **Trade-offs**: [Discuss any trade-offs in the solution]

**Real-World Applications**:
- [Where this pattern is used in production]
- [Similar problems this solves]

</details>

---

## Bonus Challenge: [Project-Based Challenge] 🎯

**Difficulty**: Project Level  
**Time**: 2-4 hours  
**Concepts**: [Multiple concepts integrated]

### Project Description

Build a [complete small application or system] that demonstrates mastery of [topic].

### Features to Implement

1. **Core Feature 1**: [Description]
2. **Core Feature 2**: [Description]
3. **Core Feature 3**: [Description]
4. **Bonus Feature** (Optional): [Description]

### Requirements

- [ ] Feature completeness
- [ ] Code quality and organization
- [ ] Error handling
- [ ] Documentation
- [ ] Test coverage
- [ ] Performance considerations

### Project Structure

```
project_name/
├── main.py           # Entry point
├── module1.py        # Core logic
├── module2.py        # Additional functionality
├── tests/            # Test files
│   └── test_main.py
├── README.md         # Project documentation
└── requirements.txt  # Dependencies
```

### Evaluation Criteria

| Criteria | Points | Description |
|----------|--------|-------------|
| Functionality | 40 | Does it work as specified? |
| Code Quality | 20 | Is it clean, readable, maintainable? |
| Error Handling | 15 | Are edge cases handled? |
| Documentation | 15 | Is it well documented? |
| Testing | 10 | Are there adequate tests? |
| **Total** | **100** | |

### Example Implementation

<details>
<summary>Click to reveal starter code</summary>

```python
# Starter code with basic structure
# Students should fill in the implementation
```

</details>

<details>
<summary>Click to reveal full solution</summary>

```python
# Complete, production-quality implementation
# With comprehensive documentation
```

**Architecture Overview**:
[Explain the design decisions and architecture]

**Key Learning Points**:
- [What this project teaches]
- [Skills demonstrated]
- [Real-world relevance]

</details>

---

## Progress Tracking

Use this checklist to track your progress:

- [ ] Challenge #1 Completed
- [ ] Challenge #2 Completed
- [ ] Challenge #3 Completed
- [ ] Bonus Challenge Completed
- [ ] All tests passing
- [ ] Code reviewed and refactored
- [ ] Solutions compared and learned from

---

## Next Steps

After completing these challenges:

1. **Review**: Compare your solutions with provided ones
2. **Optimize**: Can you make your solutions more efficient?
3. **Extend**: Add additional features or handle more edge cases
4. **Share**: Discuss your approaches with others
5. **Apply**: Use these concepts in a larger project

---

## Additional Resources

- [Link to related lessons]
- [Link to advanced topics]
- [Link to practice platforms]
- [Link to community discussions]

---

## Tips for Success

💡 **Write tests first**: Test-driven development helps clarify requirements  
💡 **Start simple**: Get a basic solution working before optimizing  
💡 **Refactor**: Improve your code after it works  
💡 **Learn from solutions**: Even if you solve it, check the provided solution  
💡 **Explain out loud**: Teaching others solidifies understanding

---

**Happy Coding!** 🚀
