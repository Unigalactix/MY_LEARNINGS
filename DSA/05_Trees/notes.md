# Trees – Notes

Key ideas:
- A tree is an acyclic connected graph; a binary tree has up to 2 children per node.
- Depth/height definitions: depth(root)=0, height(node) is longest path to a leaf.
- Traversals:
  - DFS: preorder (NLR), inorder (LNR), postorder (LRN)
  - BFS: level order (queues)
- BST property: left < node < right (strictly or non-strict depending on problem)

Patterns:
- Traversals: recursion or explicit stacks/queues
- Validate BST via inorder monotonic check or bounds
- Level-order uses a queue (collections.deque)

Complexities:
- Traversals: O(n) time, O(h) space recursion (h=height); BFS uses O(w) space (w=max width)
