class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if len(s) < numRows:
            return s
        if numRows == 1:
            return s
        f = [[None]*n]*numRows
        count = 0
        cur_i, cur_j = 0, 0
        while cur_j < n:
            if cur_j % 2 == 0:
                for _ in range(numRows):
                    f[cur_i][cur_j] = s[count]
                    print("f[%d][%d] = %s" % (cur_i, cur_j, s[count]))
                    cur_i += 1
                    if count == n:
                        break
                    else:
                        count += 1
                cur_i -= 1
                cur_j += 1
                print(cur_i, cur_j)
                print(f)
            else:
                f[cur_i][cur_j] = s[count]
                if count == n:
                    break
                else:
                    count += 1
                cur_i -= 1
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
    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))
