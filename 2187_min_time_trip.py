from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, h = 0, min(time) * totalTrips
        while l < h:
            m = (l + h) // 2
            s_trips = sum(m // t for t in time)
            print(f'l={l}, h={h}, m={m}, total_trips={s_trips}')

            if s_trips >= totalTrips:
                h = m
            else:
                l = m + 1
        return int(h)


if __name__ == "__main__":
    time = [1, 2, 3]
    totalTrips = 5
    sol = Solution()
    print(sol.minimumTime(time, totalTrips))
