from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes.sort(key=lambda x: x[0]/x[1], reverse=False)
        heap = []
        for p, t in classes:
            benefit = (p+1)/(t+1) - p/t
            heapq.heappush(heap, (-benefit, p, t))
        print(heap)
        while extraStudents > 0:
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            new_benefit = (p+1)/(t+1) - p/t
            heapq.heappush(heap, (-new_benefit, p, t))
            extraStudents -= 1
        res = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            res += p / t

        n = len(classes)
        res = res / n

        return round(res, 5)


if __name__ == "__main__":
    classes = [[1, 2], [2, 2], [3, 5]]
    extraStudents = 2
    sol = Solution()
    print(sol.maxAverageRatio(classes, extraStudents))

    print()
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4
    sol = Solution()
    print(sol.maxAverageRatio(classes, extraStudents))

    print()
    classes = [[583, 868], [783, 822], [65, 262],
               [121, 508], [461, 780], [484, 668]]
    extraStudents = 8
    sol = Solution()
    print(sol.maxAverageRatio(classes, extraStudents))
