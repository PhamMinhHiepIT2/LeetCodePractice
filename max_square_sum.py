from heapq import heapify, heappop, heappush
from re import A
from typing import List
from time import sleep
import numpy as np


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        sub = [-abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        n = len(sub)
        # sub.sort(reverse=True)
        # print("Sub: {}".format(sub))
        heapify(sub)
        print(sub)
        k = (k1 + k2)*-1
        if k == 0:
            return square_sum(sub)
        if k <= sum(sub):
            return 0
        if len(sub) == 1:
            a = sub[0] - k
            if a <= 0:
                return 0
            else:
                return a**2
        while k < 0 and sub:

            a = heappop(sub)
            b = k // n * -1 if k < n*-1 else 1
            a += b
            heappush(sub, a)
            k += b
        # print(sub)
        return square_sum(sub)


def square_sum(arr: list):
    return sum([i**2 for i in arr])


def swap(a, b):
    c = a
    a = b
    b = c
    return a, b


if __name__ == "__main__":
    nums1 = [19, 18, 19, 18, 18, 19, 19]
    nums2 = [1, 0, 1, 0, 0, 1, 1]
    k1 = 10
    k2 = 33
    print(Solution().minSumSquareDiff(nums1, nums2, k1, k2))
