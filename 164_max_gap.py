from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res, n = 0, len(nums)
        if n < 2:
            return 0
        for i in range(n-1):
            res = max(res, abs(nums[i+1] - nums[i]))
        return res
