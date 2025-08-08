"""Binary Tree Traversals
Includes: recursive and iterative inorder/preorder/postorder

Usage: python .\\DSA\\05_Trees\\traversals.py
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------- Building a sample tree ----------
#       1
#      / \
#     2   3
#    / \
#   4   5

def sample_tree():
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3)
    n1 = TreeNode(1, n2, n3)
    return n1

# ---------- Recursive traversals ----------

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# ---------- Iterative traversals ----------

def inorder_iterative(root):
    res, stack = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


def preorder_iterative(root):
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        # push right first so left pops first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def postorder_iterative(root):
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]

# ---------- BFS Level-order ----------

def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


def _test():
    root = sample_tree()
    assert inorder(root) == [4,2,5,1,3]
    assert preorder(root) == [1,2,4,5,3]
    assert postorder(root) == [4,5,2,3,1]
    assert inorder_iterative(root) == [4,2,5,1,3]
    assert preorder_iterative(root) == [1,2,4,5,3]
    assert postorder_iterative(root) == [4,5,2,3,1]
    assert level_order(root) == [[1],[2,3],[4,5]]
    print("tree traversals OK")


if __name__ == "__main__":
    _test()
