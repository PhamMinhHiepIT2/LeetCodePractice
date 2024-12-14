from typing import List
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        l, h = 1, 1e7
        n = len(dist)

        while l < h:
            m = (l + h) // 2
            total_time = 0
            for i in range(n):
                if i == n-1:
                    total_time += dist[i] / m
                else:
                    total_time += ceil(dist[i] / m)
            if total_time <= hour:
                h = m
            else:
                l = m + 1
        return int(h)


if __name__ == "__main__":
    dist = [1, 3, 2]
    hour = 2.7
    sol = Solution()
    print(sol.minSpeedOnTime(dist, hour))

    print("=============")
    dist = [1, 3, 2]
    hour = 6
    print(sol.minSpeedOnTime(dist, hour))

    print("=============")
    dist = [1, 3, 2]
    hour = 1.9
    print(sol.minSpeedOnTime(dist, hour))

    print("=============")
    dist = [1, 1]
    hour = 1.0
    print(sol.minSpeedOnTime(dist, hour))
