from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mat_1d = []
        for row in matrix:
            mat_1d += row
        heapq.heapify(mat_1d)
        print(mat_1d)
        res = -1e9
        while k > 0:
            res = heapq.heappop(mat_1d)
            k -= 1
        return res


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(Solution().kthSmallest(matrix, k))
