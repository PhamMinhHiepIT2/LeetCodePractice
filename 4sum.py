from typing import List

from numpy import mat


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        print(n)
        nums.sort()
        print(nums)
        res = []
        i, j, m, k = 0, 0, 0, 0
        for i in range(0, n-3, 1):
            for j in range(i+1, n-2, 1):
                for m in range(j+1, n-1, 1):
                    s = nums[i] + nums[j] + nums[m]
                    left_value = target - s
                    final_el = binary_search(nums, m+1, n-1, left_value)
                    if final_el != -110:
                        match = [nums[i], nums[j], nums[m], final_el]
                        if match not in res:
                            res.append([nums[i], nums[j], nums[m], final_el])
        return res


def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            return binary_search(arr, mid+1, r, x)
        else:
            return binary_search(arr, l, mid-1, x)
    else:
        return -110


if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    print(Solution().fourSum(arr, 0))
