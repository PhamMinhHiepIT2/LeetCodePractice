class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if len(s) < numRows:
            return s
        if numRows == 1:
            return s
        f = [[None for _ in range(n+2)] for _ in range(numRows+2)]
        count = 0
        cur_i, cur_j = 0, 0
        flag = 0
        while cur_j < n and flag == 0:
            if cur_j % (numRows - 1) == 0 and cur_i == 0:
                for _ in range(numRows):
                    f[cur_i][cur_j] = s[count]
                    cur_i += 1
                    if count == n-1:
                        flag = 1
                        break
                    else:
                        count += 1
                cur_i -= 2
                cur_j += 1
            else:
                f[cur_i][cur_j] = s[count]
                if count == n-1:
                    break
                else:
                    count += 1
                if cur_i > 0:
                    cur_i -= 1
                else:
                    cur_j -= 1
                cur_j += 1
        res = read_matrix(f)
        return res


def read_matrix(f):
    s = ""
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] is not None:
                s += f[i][j]
    return s


if __name__ == "__main__":
    s = "ABCD"
    numRows = 3
    print(Solution().convert(s, numRows))
