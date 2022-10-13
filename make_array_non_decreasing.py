from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i]+1, dp[stack[-1]])
                stack.pop()
            stack.append(i)
        return max(dp)


if __name__ == "__main__":
    nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]
    print(Solution().totalSteps(nums))
