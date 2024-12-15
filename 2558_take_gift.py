from typing import List
import heapq
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        neg_gifts = [-1 * el for el in gifts]
        heapq.heapify(neg_gifts)
        for _ in range(k):
            max_piles = heapq.heappop(neg_gifts) * -1
            heapq.heappush(neg_gifts, math.ceil(math.sqrt(max_piles) * -1))

        return sum(neg_gifts) * -1


if __name__ == "__main__":
    gifts = [25, 64, 9, 4, 100]
    k = 4
    sol = Solution()
    print(sol.pickGifts(gifts, k))
