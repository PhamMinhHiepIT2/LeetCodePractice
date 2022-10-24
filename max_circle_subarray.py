from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp = [nums[i % n] for i in range(2*n)]
        # dp[2*n-1] = nums[-1]
        # for i in range(2*n-2, -1, -1):
        #     dp[i] = max(dp[i], dp[i+1], dp[i+1] + nums[i % n])
        # print(dp)
        # return max(dp) // 2
        return solve(nums)


def solve(nums: List):
    double_nums = nums + nums
    n = len(nums)
    if n == 1:
        return nums[0]
    ans = -1e9
    for i in range(2*n):
        for j in range(i+1, i+n+1):
            sub_arr = double_nums[i:j]
            if i == 0:
                print(sub_arr)
            ans = max(ans, sum(sub_arr))
    return ans


if __name__ == "__main__":
    nums = [5, -3, 5]
    print(Solution().maxSubarraySumCircular(nums))
    print(solve(nums))
