from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        expected_sum = n*(n+1)/2
        res = int(expected_sum - s)
        print("Result: ", res)
        return res


if __name__ == "__main__":
    arr = [0, 1]
    s = Solution()
    s.missingNumber(arr)
