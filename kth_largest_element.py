import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = -1e9
        n = len(nums)
        remove_no = n - k

        while remove_no >= 0:
            res = heapq.heappop(nums)
            remove_no -= 1
        return res


heapq.nlargest()
