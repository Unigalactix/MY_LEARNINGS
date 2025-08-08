"""Longest Substring Without Repeating Characters
Sliding window, Time: O(n), Space: O(min(n, alphabet))
"""

def length_of_longest_substring(s: str) -> int:
    last = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best


def _test():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    print("longest_substring_no_repeat OK")


if __name__ == "__main__":
    _test()
