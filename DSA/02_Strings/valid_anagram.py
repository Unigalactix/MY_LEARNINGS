"""Valid Anagram
Time: O(n), Space: O(1) for fixed alphabet (or O(n) general)
"""

from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def _test():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    print("valid_anagram OK")


if __name__ == "__main__":
    _test()
