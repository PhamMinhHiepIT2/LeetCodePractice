from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()

        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1

        sorted_count = sorted(
            count.items(), key=lambda kv: kv[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_count[i][0])

        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))

    nums = [3, 0, 1, 0]
    k = 1
    sol = Solution()
    print(sol.topKFrequent(nums, k))
