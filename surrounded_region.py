from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                dfs(board, i, 0)
            if board[i][n-1] == 'O':
                dfs(board, i, n-1)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[m-1][i] == 'O':
                dfs(board, m-1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
        print(board)


def dfs(mat, i, j):
    m = len(mat)
    n = len(mat[0])
    mat[i][j] = '*'
    cell_steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for k in range(4):
        x = i + cell_steps[k][0]
        y = j + cell_steps[k][1]
        if x >= 0 and x < m and y >= 0 and y < n and mat[x][y] == 'O':
            dfs(mat, x, y)


if __name__ == "__main__":
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    Solution().solve(board)
