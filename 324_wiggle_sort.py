from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        tmp = nums.copy()
        n = len(nums)
        idx = 0
        for i in range(1, n, 2):
            nums[i] = tmp[idx]
            idx += 1
        for i in range(0, n, 2):
            nums[i] = tmp[idx]
            idx += 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5, 2, 1, 6, 4]
    a = s.wiggleSort(nums)
    print(a)
