"""Rotate array by k steps in-place using reverse trick
Time: O(n), Space: O(1)
"""

def rotate(nums, k):
    n = len(nums)
    k %= n

    def rev(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    rev(0, n-1)
    rev(0, k-1)
    rev(k, n-1)
    return nums


def _test():
    assert rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
    assert rotate([-1,-100,3,99], 2) == [3,99,-1,-100]
    print("rotate_array OK")


if __name__ == "__main__":
    _test()
