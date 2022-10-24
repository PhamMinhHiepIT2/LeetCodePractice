import numpy as np


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        st = []
        n = len(s)
        ans = 0
        for i in range(n-1, -1, -1):
            if not st:
                st.append(s[i])
            else:
                st.append(s[i])
                if s[i] == '1' and calc_val_from_binary(st) > k:
                    st.pop()
        # print("Prior stack: {}".format(st))
        while st and calc_val_from_binary(st) > k:
            # print("Stack before removed: {}".format(st))
            max_idx = find_max_index_of_element(st, '1')
            # print("Remove index: {}".format(max_idx))
            st.pop(max_idx)
        ans = len(st)
        # print("Value: {}".format(calc_val_from_binary(st)))
        # print("Length: {}".format(ans))
        # print("End Stack: {}".format(st))
        return ans


def calc_val_from_binary(s: list):
    n = len(s)
    res = 0
    k = 0
    for i in range(n):
        res += int(s[i]) * 2**k
        k += 1
    return res


def find_max_index_of_element(st: list, el: str):
    # for i in range(len(st)-1, -1, -1):
    #     if st[i] == el:
    #         return i

    # return -1

    idx = np.where(st == el)[-1]
    return idx


if __name__ == "__main__":
    s = "1001010"

    k = 5
    print(Solution().longestSubsequence(s, k))
    print(calc_val_from_binary(['1', '0', '1', '1']))
