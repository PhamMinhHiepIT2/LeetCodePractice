from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = 0

        n1 = len(nums1)
        n2 = len(nums2)
        m = n1+n2
        if k == m:
            max_num = merge_2_array(nums1, nums2, k)
            print(max_num)
            return convert_int_to_list(max_num)

        for i in range(m-k+1):
            if i > n1 or i > n2:
                continue
            max_num1 = removeKdigits(nums1, i)
            max_num2 = removeKdigits(nums2, m-k-i)
            print("Array 1: {}".format(max_num1))
            print("Array 2: {}".format(max_num2))
            max_num = merge_2_array(max_num1, max_num2, k)

            if ans < max_num:
                ans = max_num
        res = convert_int_to_list(ans)
        print("Final result: {}".format(res))
        return res


def removeKdigits(num: str, k: int) -> str:
    print("Remove {} number".format(k))
    n = len(num)
    st = []
    if k >= n:
        return []

    for i in range(n):
        print(i)
        while st and k > 0 and num[i] > st[-1]:
            st.pop()
            k -= 1

        st.append(num[i])
        print(st)

    while st and k > 0:
        st.pop()
        k -= 1
        if len(st) == 0:
            return []
    if len(st) == 0:
        return []

    return st


def merge_2_array(num1: list, num2: list, k: int):
    max_num = ""
    print("Array: {} has length {}".format(num1, len(num1)))
    print("Array: {} has length {}".format(num2, len(num2)))
    if len(num1) == 0:
        res = num2
    if len(num2) == 0:
        res = num1
    n1 = len(num1)
    n2 = len(num2)
    n = min(len(num1), len(num2))
    id1, id2 = 0, 0
    res = []
    while id1 < n1 and id2 < n2:
        if num1[id1] > num2[id2]:
            res.append(num1[id1])
            id1 += 1
        elif num1[id1] > num2[id2]:
            res.append(num2[id2])
            id2 += 1
        else:
            if nums1[id1] < nums2[id2+1] and nums2[id2] < num1[id1+1] and nums1[id1+1] < nums2[id2+1] and id1 < n1-1 and id2 < n2-1:
                res.append(nums2[id2])
                id2 += 1

            elif nums1[id1] < nums2[id2+1] and nums2[id2] < num1[id1+1] and nums1[id1+1] > nums2[id2+1] and id1 < n1-1 and id2 < n2-1:
                res.append(nums1[id1])
                id1 += 1
            elif nums1[id1] < nums2[id2+1] and nums2[id2] < num1[id1+1] and nums1[id1+1] < nums2[id2+1] and id1 < n1-1 and id2 < n2-1:
                pass
    if id2 == n2:
        for i in range(id1, len(num1)):
            res.append(num1[i])
    elif id1 == n1:
        for i in range(id2, len(num2)):
            res.append(num2[i])

    if len(res) > k:
        res = res[0:k]
        print("Remove {} number from {}".format(len(res) - k, res))

    print("Merge {} and {} ===> {}".format(num1, num2, res))

    for num in res:
        max_num += str(num)
    if max_num:
        return int(max_num)
    else:
        return 0


def convert_list_to_int(num: list):
    num_str = ""
    if len(num) == 0:
        return 0
    for i in num:
        num_str += str(i)
    return int(num_str)


def convert_int_to_list(num: int):
    res = []
    for i in str(num):
        res.append(int(i))
    return res


if __name__ == "__main__":

    nums1 = [2, 5, 6, 4, 4, 0]
    nums2 = [7, 3, 8, 0, 6, 5, 7, 6, 2]
    k = 15
    print(Solution().maxNumber(nums1, nums2, k))
    # print(removeKdigits(nums2, 2))
