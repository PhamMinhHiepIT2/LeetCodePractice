from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        cur_max, max_so_far, cur_min, min_so_far = nums[0], nums[0], nums[0], nums[0]
        for i in range(1, n):
            cur_max = max(cur_max + nums[i], nums[i])
            max_so_far = max(cur_max, max_so_far)
            cur_min = min(cur_min + nums[i], nums[i])
            min_so_far = min(cur_min, min_so_far)
        if min_so_far == s:
            return max_so_far
        return max(max_so_far, s - min_so_far)


if __name__ == "__main__":
    nums = [-3, -2, -3]
    print(Solution().maxSubarraySumCircular(nums))
