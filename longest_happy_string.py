from time import sleep


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        st = [['a', a], ['b', b], ['c', c]]
        st.sort(key=lambda x: x[1], reverse=True)
        # print(st)
        s = ""
        while st[0][1] > 0 or st[1][1] > 0 or st[2][1] > 0:
            if not s:
                s = st[0][0]
                st[0][1] -= 1
            else:
                if len(s) >= 2 and s[-1] == s[-2]:
                    # print("Go to 1")
                    if st[0][0] == s[-1]:
                        if st[1][1] > 0:
                            s += st[1][0]
                            st[1][1] -= 1
                        elif st[2][1] > 0:
                            s += st[2][0]
                            st[2][1] -= 1
                        else:
                            break
                    else:
                        if st[0][1] > 0:
                            s += st[0][0]
                            st[0][1] -= 1
                        else:
                            break
                else:
                    # print("Go to 2")
                    if st[0][1] > 0:
                        s += st[0][0]
                        st[0][1] -= 1
                    elif st[1][1] > 0:
                        s += st[1][0]
                        st[1][1] -= 1
                    elif st[2][1] > 0:
                        s += st[2][0]
                        st[2][1] -= 1
                    else:
                        break
            # print(s)
            # print(st)
            st.sort(key=lambda x: x[1], reverse=True)
            # sleep(1)
        return s


if __name__ == "__main__":
    a = 1
    b = 3
    c = 5
    print(Solution().longestDiverseString(a, b, c))
