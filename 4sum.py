from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        flags = {}
        for i in range(n):
            for j in range(n-1, i, -1):
                p = i + 1
                q = j - 1
                while p < q:
                    total = nums[i] + nums[j] + nums[p] + nums[q]
                    if total > target:
                        q -= 1
                    elif total < target:
                        p += 1
                    else:
                        el = sorted([nums[i], nums[j], nums[p], nums[q]])
                        if f"{nums[i]}{nums[j]}{nums[p]}{nums[q]}" not in flags:
                            flags[f"{nums[i]}{nums[j]}{nums[p]}{nums[q]}"] = 1
                            res.append(el)
                        p += 1
                        q -= 1
        return res


def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid+1, r, x)
        else:
            return binary_search(arr, l, mid-1, x)
    else:
        return 201


if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    print(Solution().fourSum(arr, 0))
