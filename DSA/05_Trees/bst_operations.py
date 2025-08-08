"""Basic Binary Search Tree operations: insert, search, delete (simplified)
Note: This is for learning; production code would handle duplicates/edge-cases more robustly.
"""

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return BSTNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    # ignore equal to keep unique set
    return root


def search(root, val):
    cur = root
    while cur:
        if val == cur.val:
            return True
        cur = cur.left if val < cur.val else cur.right
    return False


def find_min(node):
    while node.left:
        node = node.left
    return node


def delete(root, val):
    if not root:
        return None
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # found node
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # two children: swap with inorder successor
        succ = find_min(root.right)
        root.val = succ.val
        root.right = delete(root.right, succ.val)
    return root


def inorder_vals(root):
    return inorder_vals(root.left) + [root.val] + inorder_vals(root.right) if root else []


def _test():
    root = None
    for v in [5,3,7,2,4,6,8]:
        root = insert(root, v)
    assert inorder_vals(root) == [2,3,4,5,6,7,8]
    assert search(root, 6) is True
    assert search(root, 10) is False
    root = delete(root, 7)
    assert inorder_vals(root) == [2,3,4,5,6,8]
    print("bst operations OK")


if __name__ == "__main__":
    _test()
