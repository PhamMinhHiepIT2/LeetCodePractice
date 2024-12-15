from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l, h = nums[0], max(nums)

        if nums[0] == max(nums):
            return nums[0]

        n = len(nums)
        s = sum(nums)

        while l < h:
            m = (l + h) // 2
