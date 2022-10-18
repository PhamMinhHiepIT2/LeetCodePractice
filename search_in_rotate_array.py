from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = find_k_rotate(nums, 0, n-1)
        print("k: {}".format(k))
        p1 = nums[:k]
        p2 = nums[k:]
        new_nums = p2+p1
        res = binary_search(new_nums, 0, n-1, target, k)

        return res


def binary_search(arr, l, r, x, k):
    n = len(arr)
    if r >= l:
        mid = l + (r-l) // 2
        if(arr[mid] == x):
            return (mid+k) % n
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, r, x, k)
        else:
            return binary_search(arr, l, mid-1, x, k)
    return -1


def find_k_rotate(arr, l, r):
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[1] - arr[0] < 0:
            return 1
        else:
            return 0
    if r >= l and r <= len(arr):
        mid = l + (r-l) // 2
        if mid >= 1 and arr[mid] - arr[mid-1] < 0:
            return mid
        else:
            left_res = find_k_rotate(arr, l, mid-1)
            right_res = find_k_rotate(arr, mid+1, r)
            return left_res if left_res != 0 else right_res
    return 0


if __name__ == "__main__":
    nums = [1, 3, 5]
    target = 5
    print(Solution().search(nums, target))
