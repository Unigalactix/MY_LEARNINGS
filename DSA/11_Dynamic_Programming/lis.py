"""Longest Increasing Subsequence (O(n log n))
Patience sorting idea with tails array.
"""

def lis_length(nums):
    import bisect
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def _test():
    assert lis_length([10,9,2,5,3,7,101,18]) == 4
    assert lis_length([0,1,0,3,2,3]) == 4
    assert lis_length([7,7,7,7]) == 1
    print("LIS OK")


if __name__ == "__main__":
    _test()
