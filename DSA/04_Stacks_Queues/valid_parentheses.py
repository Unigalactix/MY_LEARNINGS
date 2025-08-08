"""Valid Parentheses using stack
Time: O(n), Space: O(n)
"""

def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs.get(ch, None):
                return False
            stack.pop()
    return not stack


def _test():
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([{}])") is True
    print("valid_parentheses OK")


if __name__ == "__main__":
    _test()
