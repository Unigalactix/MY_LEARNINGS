"""Two Sum
Time: O(n), Space: O(n)
"""

def two_sum(nums, target):
    idx = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in idx:
            return [idx[y], i]
        idx[x] = i
    return []


def _test():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]
    print("two_sum OK")


if __name__ == "__main__":
    _test()
