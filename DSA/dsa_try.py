"""
Tiny sampler to quickly run a few DSA snippets.
Run with: python .\\DSA\\dsa_try.py
"""

def two_sum(nums, target):
    idx = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in idx:
            return [idx[y], i]
        idx[x] = i
    return []


def kadane(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def main():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert kadane([5,-2,3,4]) == 10
    print("Sampler OK: two_sum and kadane passed.")


if __name__ == "__main__":
    main()
