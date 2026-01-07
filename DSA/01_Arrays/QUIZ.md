# Arrays Quiz - DSA 📝

**Topic**: Arrays and Common Patterns  
**Difficulty**: ⭐⭐ Intermediate  
**Time**: ~25 minutes

**Instructions**: 
- Try to answer all questions before checking the answers
- Focus on understanding time/space complexity
- Practice the patterns mentioned in the notes

---

## Section 1: Time Complexity Questions

### Question 1 (⭐⭐ Intermediate)
**What is the time complexity of accessing an element by index in an array?**

A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)

<details>
<summary>Click to reveal answer</summary>

**Answer: A - O(1)**

**Explanation**: 
Arrays store elements in contiguous memory locations. The memory address of any element can be calculated directly using the formula: `base_address + (index × element_size)`. This is a constant-time operation, regardless of array size.

**Example**:
```python
arr = [10, 20, 30, 40, 50]
print(arr[0])   # O(1) - Instant access
print(arr[4])   # O(1) - Also instant, no matter position
print(arr[100]) # O(1) - Would be instant if index existed
```

This is why arrays are called "random access" data structures.

</details>

---

### Question 2 (⭐⭐ Intermediate)
**What is the time complexity of inserting an element at the beginning of an array?**

A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)

<details>
<summary>Click to reveal answer</summary>

**Answer: C - O(n)**

**Explanation**: 
When inserting at the beginning, all existing elements must be shifted one position to the right to make room for the new element. This requires touching every element in the array, resulting in O(n) time complexity.

**Visual representation**:
```python
# Before: [2, 3, 4, 5]
# Insert 1 at beginning
# Step 1: Shift everything right: [_, 2, 3, 4, 5]
# Step 2: Place new element: [1, 2, 3, 4, 5]

arr = [2, 3, 4, 5]
arr.insert(0, 1)  # O(n) operation
print(arr)  # [1, 2, 3, 4, 5]
```

**Why it's O(n)**:
- Must shift n elements
- Each shift is O(1)
- Total: O(1) × n = O(n)

**Better alternatives for frequent insertions at beginning**:
- Use `collections.deque` (double-ended queue) for O(1) insertions at both ends
- Use linked lists for O(1) insertions at beginning

</details>

---

## Section 2: Pattern Recognition

### Question 3 (⭐⭐ Intermediate)
**Which pattern would you use to find two numbers in a SORTED array that sum to a target?**

A) Hash Map  
B) Two Pointers  
C) Sliding Window  
D) Kadane's Algorithm

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Two Pointers**

**Explanation**: 
For a sorted array, the two-pointer technique is optimal. Place one pointer at the start and one at the end, then move them based on whether the sum is too small or too large.

**Implementation**:
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]  # Found!
        elif current_sum < target:
            left += 1   # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # Not found

# Example
arr = [1, 2, 3, 4, 6, 8, 9]
target = 10
print(two_sum_sorted(arr, target))  # [2, 5] (3 + 8 = 10)
```

**Why this works**:
- Time: O(n) - single pass through array
- Space: O(1) - only two pointers
- For unsorted arrays, use Hash Map instead (also O(n) time but O(n) space)

**Key insight**: Sorted array allows us to make decisions about which direction to move pointers.

</details>

---

### Question 4 (⭐⭐⭐ Advanced)
**Which pattern is best for finding the maximum sum of a contiguous subarray?**

A) Two Pointers  
B) Binary Search  
C) Kadane's Algorithm  
D) Prefix Sum

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Kadane's Algorithm**

**Explanation**: 
Kadane's Algorithm is specifically designed for the maximum subarray problem. It maintains two variables: the maximum ending at the current position and the overall maximum found so far.

**Implementation**:
```python
def max_subarray_sum(arr):
    """
    Find maximum sum of contiguous subarray.
    Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 ([4,-1,2,1])
    """
    if not arr:
        return 0
    
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Key decision: extend current subarray or start new?
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # 6
```

**Why it works**:
- At each position, decide: continue current subarray or start fresh?
- If current sum becomes negative, starting fresh is better
- Time: O(n), Space: O(1)

**Alternative approaches**:
- Brute force: O(n²) - check all subarrays
- Divide and conquer: O(n log n)
- Kadane's is optimal: O(n)

</details>

---

## Section 3: Code Analysis

### Question 5 (⭐⭐⭐ Advanced)
**What does this code do, and what is its time complexity?**

```python
def mystery_function(arr):
    result = []
    seen = set()
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result
```

A) Removes duplicates in O(n²)  
B) Removes duplicates in O(n)  
C) Sorts array in O(n log n)  
D) Finds most frequent element in O(n)

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Removes duplicates in O(n)**

**Explanation**: 
This function removes duplicates while preserving the order of first occurrence. It uses a set for O(1) lookups to check if an element has been seen before.

**How it works**:
```python
arr = [1, 2, 2, 3, 1, 4, 3, 5]

# Step by step:
# num=1: not in seen → add to result [1], add to seen {1}
# num=2: not in seen → add to result [1,2], add to seen {1,2}
# num=2: in seen → skip
# num=3: not in seen → add to result [1,2,3], add to seen {1,2,3}
# num=1: in seen → skip
# num=4: not in seen → add to result [1,2,3,4], add to seen {1,2,3,4}
# num=3: in seen → skip
# num=5: not in seen → add to result [1,2,3,4,5], add to seen {1,2,3,4,5}

# Result: [1, 2, 3, 4, 5]
```

**Complexity Analysis**:
- **Time**: O(n)
  - Loop through n elements: O(n)
  - Each set lookup/add: O(1) average
  - Each append: O(1) amortized
  - Total: O(n)

- **Space**: O(n)
  - Set stores up to n unique elements
  - Result list stores up to n elements

**Alternative approaches**:
```python
# Using dict (Python 3.7+, preserves order)
def remove_duplicates_v2(arr):
    return list(dict.fromkeys(arr))

# Without extra space (modifies original, doesn't preserve all elements)
def remove_duplicates_inplace(arr):
    # Only works for sorted arrays efficiently
    if not arr:
        return 0
    write_idx = 1
    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[write_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    return write_idx
```

</details>

---

### Question 6 (⭐⭐⭐ Advanced)
**What is the space complexity of this array rotation implementation?**

```python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    
    arr[:] = arr[-k:] + arr[:-k]
```

A) O(1)  
B) O(k)  
C) O(n)  
D) O(n + k)

<details>
<summary>Click to reveal answer</summary>

**Answer: C - O(n)**

**Explanation**: 
Although this looks elegant, slicing creates new lists. The expression `arr[-k:] + arr[:-k]` creates two new lists and concatenates them, requiring O(n) extra space.

**Space breakdown**:
```python
arr = [1, 2, 3, 4, 5]
k = 2

# arr[-k:] creates new list [4, 5]           → O(k) space
# arr[:-k] creates new list [1, 2, 3]        → O(n-k) space
# Concatenation creates [4, 5, 1, 2, 3]     → O(n) space
# Total: O(k) + O(n-k) + O(n) = O(n)
```

**Better O(1) space solution using reverse trick**:
```python
def rotate_array_optimal(arr, k):
    n = len(arr)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)

# Example: [1, 2, 3, 4, 5], k=2
# After reverse(0, 4): [5, 4, 3, 2, 1]
# After reverse(0, 1): [4, 5, 3, 2, 1]
# After reverse(2, 4): [4, 5, 1, 2, 3] ✓
```

**Key lesson**: Slicing is convenient but often uses O(n) space. For in-place operations, use indices and swapping.

</details>

---

## Section 4: Problem Solving

### Question 7 (⭐⭐⭐ Advanced)
**You need to find if any value appears at least twice in an array. Which approach is most efficient?**

A) Nested loops - O(n²) time, O(1) space  
B) Sort then check neighbors - O(n log n) time, O(1) space  
C) Use set - O(n) time, O(n) space  
D) All equally good

<details>
<summary>Click to reveal answer</summary>

**Answer: C - Use set - O(n) time, O(n) space**

**Explanation**: 
While option B is also reasonable, option C provides the best time complexity. The trade-off between time and space depends on constraints, but O(n) time is optimal for this problem.

**All approaches compared**:

**Approach A - Nested Loops**:
```python
def has_duplicate_v1(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```
- Time: O(n²) - check every pair
- Space: O(1) - no extra space
- ❌ Too slow for large arrays

**Approach B - Sort First**:
```python
def has_duplicate_v2(arr):
    arr_sorted = sorted(arr)  # or arr.sort() to modify in place
    for i in range(len(arr_sorted) - 1):
        if arr_sorted[i] == arr_sorted[i + 1]:
            return True
    return False
```
- Time: O(n log n) - sorting dominates
- Space: O(1) if sort in place, O(n) for sorted()
- ✓ Decent solution

**Approach C - Set (Best)**:
```python
def has_duplicate_v3(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Or more Pythonic:
def has_duplicate_v4(arr):
    return len(set(arr)) != len(arr)
```
- Time: O(n) - single pass
- Space: O(n) - store seen elements
- ✅ Optimal time complexity

**When to use each**:
- **Space constrained**: Use approach B
- **Time critical**: Use approach C
- **Small arrays**: Any approach works

</details>

---

## Scoring Guide

**Total Questions**: 7

- **6-7 correct (86-100%)**: Excellent! Array patterns mastered! 🎉
- **4-5 correct (57-71%)**: Good! Review specific patterns. 👍
- **2-3 correct (29-43%)**: Keep studying! Practice more problems. 📚
- **0-1 correct (0-14%)**: Review notes and examples thoroughly. 💪

---

## Practice Problems

Try implementing these algorithms from memory:

1. **Two Sum** (Hash Map pattern)
2. **Maximum Subarray** (Kadane's Algorithm)
3. **Rotate Array** (Reverse trick)
4. **Remove Duplicates from Sorted Array** (Two Pointers)

---

## Next Steps

### If you scored well (75%+):
- ✅ Solve problems in this folder: `two_sum.py`, `kadane.py`, `rotate_array.py`
- ✅ Move to next DSA topic: Strings or Linked Lists
- ✅ Practice on LeetCode/NeetCode

### If you need more practice:
- 📖 Review [notes.md](./notes.md) carefully
- 💻 Implement each pattern from scratch
- 🔄 Retake this quiz
- 📊 Analyze time/space complexity of your solutions

---

## Related Materials

- [notes.md](./notes.md) - Comprehensive array patterns guide
- [two_sum.py](./two_sum.py) - Hash map pattern example
- [kadane.py](./kadane.py) - Maximum subarray problem
- [rotate_array.py](./rotate_array.py) - In-place rotation

---

**Keep practicing!** 🚀
