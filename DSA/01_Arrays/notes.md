# Arrays – Comprehensive Notes 📚

## Overview

Arrays (Python lists) are one of the most fundamental data structures in programming. They store elements in contiguous memory locations, allowing fast access to elements by index.

### Key Characteristics

- **Indexable**: Access any element in O(1) time using its index
- **Contiguous Memory**: Elements stored sequentially in memory  
- **Dynamic in Python**: Unlike static arrays in C/Java, Python lists grow dynamically
- **Random Access**: O(1) time to access any element by index
- **Mutable**: Elements can be changed after creation

---

## Time Complexity Analysis

| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| Access by index | O(1) | Direct memory access |
| Search (unsorted) | O(n) | Must check each element |
| Search (sorted) | O(log n) | Binary search possible |
| Insert at end | O(1) amortized | Occasional resize needed |
| Insert at beginning | O(n) | Shift all elements right |
| Insert at middle | O(n) | Shift elements after insertion point |
| Delete at end | O(1) | Simple pop operation |
| Delete at beginning | O(n) | Shift all elements left |
| Delete at middle | O(n) | Shift elements after deletion point |
| Traversal | O(n) | Visit each element once |

---

## Common Array Patterns

### 1. Two Pointers Pattern
Use two pointers moving towards each other or in the same direction.

**Use Cases**:
- Pair sum problems (sorted array)
- Remove duplicates
- Reverse array
- Palindrome checking

**Example**:
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

**Time**: O(n), **Space**: O(1)

### 2. Sliding Window Pattern
Maintain a window that slides through the array.

**Use Cases**:
- Maximum/minimum sum of subarray of size k
- Longest substring without repeating characters
- Find all anagrams

### 3. Prefix Sum Pattern
Pre-calculate cumulative sums for range query optimization.

**Use Cases**:
- Subarray sum equals k
- Range sum queries
- Equilibrium index

### 4. Hash Map Pattern
Use hash maps to achieve O(1) lookups.

**Use Cases**:
- Two sum problem
- Checking for duplicates
- Frequency counting

### 5. Kadane's Algorithm (Maximum Subarray)
Find maximum sum of contiguous subarray.

**Key Insight**: At each position, decide whether to extend current subarray or start new one.

### 6. In-Place Array Rotation (Reverse Trick)
Rotate array without extra space using reversals.

**Key Insight**: Reverse three times: entire array, first k, last n-k.

---

## Common Pitfalls & How to Avoid Them

### 1. Off-by-One Errors
**Problem**: Incorrect loop bounds or index calculations.

**Prevention**: Double-check loop conditions and test with small arrays.

### 2. Mutating While Iterating
**Problem**: Modifying array while looping can skip elements or cause errors.

**Solution**: Iterate backwards or create a new list.

### 3. Shallow vs Deep Copies
**Problem**: Assignment creates reference, not copy.

**Solution**: Use `.copy()` or `[:]` for shallow copy, `copy.deepcopy()` for nested structures.

---

## Practice Goals

### Beginner Level
- [ ] Understand array indexing and slicing
- [ ] Master basic traversal patterns
- [ ] Solve two-sum problem with hash map
- [ ] Implement simple search algorithms

### Intermediate Level
- [ ] Master two-pointer technique
- [ ] Understand and implement sliding window
- [ ] Solve Kadane's algorithm problems
- [ ] Practice in-place array modifications

### Advanced Level
- [ ] Optimize space complexity to O(1)
- [ ] Handle complex two-pointer scenarios
- [ ] Master prefix sum variations
- [ ] Solve problems with multiple patterns combined

---

## Essential Problems to Master

1. **Two Sum** - Hash map pattern
2. **Maximum Subarray** - Kadane's algorithm
3. **Rotate Array** - In-place rotation with reverse trick
4. **Container With Most Water** - Two pointers
5. **Product of Array Except Self** - Prefix/suffix products
6. **Merge Sorted Arrays** - Two pointers
7. **Remove Duplicates** - Two pointers in-place

---

## Python-Specific Tips

### List Comprehensions
```python
squares = [x**2 for x in arr]
evens = [x for x in arr if x % 2 == 0]
```

### Slicing
```python
first_three = arr[:3]      # First 3 elements
last_three = arr[-3:]      # Last 3 elements
reversed_arr = arr[::-1]   # Reverse
```

### Useful Built-in Functions
```python
max_val = max(arr)
min_val = min(arr)
total = sum(arr)
sorted_arr = sorted(arr)
```

---

## Summary

**Key Takeaways**:
- Arrays provide O(1) access but O(n) insertion/deletion (except at end)
- Master the core patterns: two pointers, sliding window, hash map, prefix sum
- Kadane's algorithm is essential for subarray problems
- Be careful with off-by-one errors and mutating while iterating

**Next Steps**: Practice problems in this folder: `two_sum.py`, `kadane.py`, `rotate_array.py`
