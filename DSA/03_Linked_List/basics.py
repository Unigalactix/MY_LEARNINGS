"""Singly Linked List basics: build, traverse, reverse, cycle detect
"""

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def from_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    cur = head
    seen = set()
    while cur:
        if id(cur) in seen:
            out.append("<cycle>")
            break
        seen.add(id(cur))
        out.append(cur.val)
        cur = cur.next
    return out


def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def _test():
    head = from_list([1,2,3])
    assert to_list(head) == [1,2,3]
    r = reverse_list(head)
    assert to_list(r) == [3,2,1]

    a = ListNode(1); b = ListNode(2); c = ListNode(3)
    a.next = b; b.next = c; c.next = b
    assert has_cycle(a) is True

    print("linked_list basics OK")


if __name__ == "__main__":
    _test()
