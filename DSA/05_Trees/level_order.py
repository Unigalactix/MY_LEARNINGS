"""Level Order Traversal (BFS) of a binary tree
"""
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    q = deque([root])
    ans = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


def _test():
    #    1
    #   / \
    #  2   3
    #     / \
    #    4   5
    r = Node(1, Node(2), Node(3, Node(4), Node(5)))
    assert level_order(r) == [[1],[2,3],[4,5]]
    print("level order OK")


if __name__ == "__main__":
    _test()
