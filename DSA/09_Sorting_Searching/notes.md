# Sorting & Searching – Notes

Sorting:
- Stable: merge sort; Unstable: quicksort (typical)
- Python: Timsort (hybrid, stable) – sorted()/list.sort()

Binary Search patterns:
- Any true/false monotonic predicate → lower/upper bound templates
- Beware integer overflow (Python safe), loop conditions, and off-by-one
