from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count_0 = 0
        count_1 = 0
        count_2 = 0

        for i in nums:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            else:
                count_2 += 1
        for i in range(n):
            if count_0 > 0:
                nums[i] = 0
                count_0 -= 1
                continue
            elif count_1 > 0:
                nums[i] = 1
                count_1 -= 1
                continue
            else:
                nums[i] = 2
                count_2 -= 1
        print(nums)


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    sol.sortColors(nums=nums)
