"""Binary Search Variants: exact, lower_bound, upper_bound
"""

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def _test():
    arr = [1,2,4,4,5,6]
    assert binary_search(arr, 5) == 4
    assert lower_bound(arr, 4) == 2
    assert upper_bound(arr, 4) == 4
    assert lower_bound(arr, 3) == 2
    assert upper_bound(arr, 3) == 2
    print("binary search variants OK")


if __name__ == "__main__":
    _test()
