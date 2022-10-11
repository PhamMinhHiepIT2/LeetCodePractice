class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0]*(n+1) for i in range((m+1))]

        f[0][:] = [0]*(n+1)
        f[:][0] = [0]*(m+1)
        print(f)
        f[0][1] = 0
        f[1][0] = 0
        f[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                print(i, j)
                f[i][j] = f[i-1][j] + f[i][j-1]
                print("f[%d][%d]=%d" % (i, j, f[i][j]))
        return f[m][n]


if __name__ == "__main__":
    m = 3
    n = 2
    print(Solution().uniquePaths(m, n))
