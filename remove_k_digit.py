class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []
        if k >= n:
            return 0
        if list(set(num))[0] == '0':
            return 0

        for i in range(n):
            while st and k > 0 and num[i] < st[-1]:
                st.pop()
                k -= 1

            if st and num[i] != '0':
                st.append(num[i])

        while st and k > 0:
            st.pop()
            k -= 1
            if len(st) == 0:
                return 0
        if len(st) == 0:
            return 0
        res = ""
        while st:
            res += st.pop()

        print(res)


if __name__ == "__main__":
    num = "1432219"
    k = 3
    print(Solution().removeKdigits(num, k))
