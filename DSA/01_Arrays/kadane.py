"""Kadane's Algorithm – Maximum Subarray Sum
Time: O(n), Space: O(1)
"""

def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def _test():
    assert max_subarray([5, -2, 3, 4]) == 10
    assert max_subarray([-1, -2, -3]) == -1
    assert max_subarray([1, 2, 3]) == 6
    print("kadane OK")


if __name__ == "__main__":
    _test()
