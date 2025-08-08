# DSA Overview

Use this as a quick guide while following the referenced playlist. Concepts are written originally here and do not reproduce the video content.

Playlist reference: https://www.youtube.com/playlist?list=PLGtXWdsgkXsS39pJdWsd5JF-Qg52rrPcy

## Big-O Cheatsheet
- O(1): constant – dictionary lookups
- O(log n): logarithmic – binary search
- O(n): linear – single pass over data
- O(n log n): typical good sorts – merge/quick (avg)
- O(n^2): nested loops – naive pair comparisons
- O(2^n)/O(n!): brute-force recursion (subsets/permutations)

## Core patterns
- Two pointers: sorted arrays/strings, dedupe, window boundaries
- Sliding window: substring/array segment with constraints
- Hash map/set: fast membership, frequency count
- Stack: matching, monotonic stack, expression evaluation
- Queue/Deque: BFS, window min/max
- Recursion/Backtracking: explore choices; prune with constraints
- DP: overlapping subproblems + optimal substructure
- Graph traversal: BFS shortest path (unweighted), DFS exploration

## Templates

### Sliding window (variable length)
```python
from collections import Counter

def longest_substring_k_distinct(s: str, k: int) -> int:
    freq = Counter()
    left = 0
    best = 0
    for right, ch in enumerate(s):
        freq[ch] += 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Binary search (bound search)
```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

### DFS (recursion)
```python
import sys
sys.setrecursionlimit(1_000_000)

def dfs(u, graph, seen):
    if u in seen:
        return
    seen.add(u)
    for v in graph[u]:
        dfs(v, graph, seen)
```
