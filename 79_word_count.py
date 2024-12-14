import time
from typing import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


def check_result(board, word):
    c = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "*":
                c += 1
    if c == len(word):
        return True
    return False


def backtrack(board, x, y, ch, word):

    if x - 1 >= 0:
        if board[x-1][y] == ch:
            board[x-1][y] = "*"


# def sol(board: List[List[str]], word: str):
#     m = len(board[0])
#     n = len(board)
#     w = len(word)
#     res = []
#     mem = []
#     prev_x = 0
#     prev_y = 0
#     for k in range(len(word)):
#         arr = []
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[k]:
#                     board[i][i] = "*"
#                     prev_x = i
#                     prev_y = j
#                     if


def sol1(arr: list):
    n = len(arr)
    res = []
    tmp = []
    i = 0
    while n > 0:
        if i < n-1 and i >= 0:
            if arr[i] not in tmp:
                tmp.append(arr[i])
                arr.remove(arr[i])
                n = len(arr)
            else:
                i += 1
                n = len(arr)
            print(i, n, arr, tmp)
        else:
            print("LAST", i, n, arr, tmp)
            if n > 0:
                if arr[-1] not in tmp:
                    tmp.append(arr[-1])
                    arr.remove(arr[-1])
                    res.append(tmp)
                    i = 0
                else:
                    i = 0
                    res.append(tmp)
                tmp = []
        n = len(arr)
    return res


if __name__ == "__main__":
    arr = [6, 4, 6, 4, 3, 3, 6, 2]
    print(sol1(arr))
