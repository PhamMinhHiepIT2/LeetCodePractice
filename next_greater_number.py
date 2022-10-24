from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None for _ in range(n)]
        st = []
        tmp = []
        for i in range(n):
            st.append((nums[i], i))
        sorted_st = sorted_enum(st)
        for i in range(n):
            if not tmp:
                tmp.append(sorted_st[i])
            else:
                while tmp and sorted_st[i][0] > tmp[-1][0]:
                    res[tmp[-1][1]] = sorted_st[i][1]
                    tmp.pop()
                tmp.append(sorted_st[i])
        while tmp:
            res[tmp[-1][1]] = -1
            tmp.pop()
        print(res)


def sorted_enum(nums: list):
    return sorted(nums, key=lambda x: x[0])


if __name__ == "__main__":
    nums = [1, 2, 1]
    Solution().nextGreaterElements(nums)
