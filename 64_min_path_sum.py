from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(0, m):
                if i > 0:
                    dp[i][j] = min(dp[i-1][j] + grid[i][j],
                                   dp[i][j-1] + grid[i][j])
                else:
                    if j > 0:
                        dp[i][j] = dp[i][j-1] + grid[i][j]
        return dp[n-1][m-1]


if __name__ == "__main__":
    # grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # sol = Solution()
    # print(sol.minPathSum(grid))

    grid = [[1, 2, 3], [4, 5, 6]]
    sol = Solution()
    print(sol.minPathSum(grid))
