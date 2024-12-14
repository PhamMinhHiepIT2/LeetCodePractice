from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        j = 1
        n = len(nums)
        nums = [i for n, i in enumerate(nums) if i not in nums[:n]]
        if len(nums) < k:
            return 0
        n = len(nums)
        # nums = (set(nums))
        print(nums)

        dp = [0]*n
        dp[0] = sum(nums[:k])
        cur_arr = nums[:k]

        while j <= n-k:
            sub_arr = nums[j:j+k]
            dp[j] = dp[j-1] - cur_arr[0] + sub_arr[-1]
            j += 1
            cur_arr = sub_arr
        return max(dp)


if __name__ == "__main__":
    nums = [3, 5, 3, 4]
    k = 2
    print(Solution().maximumSubarraySum(nums, k))
