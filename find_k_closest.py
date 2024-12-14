from typing import List
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        st = [(arr[i], i) for i in range(len(arr))]
        dist = [(abs(st[i][0] - x), i) for i in range(len(st))]
        dist.sort(key=lambda x: x[0])
        for i in range(k):
            res.append(arr[dist[i][1]])
        res.sort()
        return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    print(Solution().findClosestElements(arr, k, x))
