# Graphs – Notes

Representations:
- Adjacency list: dict[list[int]] – efficient for sparse graphs
- Adjacency matrix: n x n – simple but O(n^2) space

Traversals:
- BFS: queue; shortest path in unweighted graphs
- DFS: recursion/stack; detect cycles, connected components

Tips:
- Track visited set
- For shortest path unweighted, store parent to reconstruct path
