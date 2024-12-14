from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i % 6 == 0:
                res.append(i)
        if len(res) == 0:
            return 0
        return sum(res) // len(res)


if __name__ == "__main__":
    nums = [1, 3, 6, 10, 12, 15]
    print(Solution().averageValue(nums))
