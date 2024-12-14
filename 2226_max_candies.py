from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total_candies = sum(candies)
        if total_candies < k:
            return 0

        l, h = 1, max(candies)
        while l <= h:
            m = (l + h) // 2  # m: number of candies of each person
            can = sum(c // m for c in candies)
            # print(f"low={l}, high={h}, mid={m}, candiate={can}")
            if can >= k:
                l = m + 1
            else:
                h = m - 1
        return h


if __name__ == "__main__":
    candies = [5, 8, 6]
    k = 3
    sol = Solution()
    print(sol.maximumCandies(candies, k))

    print("===========================")
    candies = [4, 7, 5]
    k = 4
    print(sol.maximumCandies(candies, k))

    print("===========================")
    candies = [1, 2, 3, 4, 10]
    k = 5
    print(sol.maximumCandies(candies, k))
    # assert sol.maximumCandies(candies, k) == 3

    print("===========================")
    candies = [4, 7, 5]
    k = 16
    print(sol.maximumCandies(candies, k))

    print("===========================")
    candies = [5, 6, 4, 10, 10, 1, 1, 2, 2, 2]
    k = 9
    print(sol.maximumCandies(candies, k))

    print("===========================")
    candies = [1]
    k = 1
    print(sol.maximumCandies(candies, k))
