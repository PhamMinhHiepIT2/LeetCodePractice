from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        fractions = []
        for i in range(n):
            for j in range(i, n):
                fractions.append([arr[i]/arr[j], i, j])
        fractions.sort(key=lambda x: x[0], reverse=False)
        kth = fractions[k-1]
        print(fractions, kth)
        return [arr[kth[1]], arr[kth[2]]]


if __name__ == "__main__":
    arr = [1, 2, 3, 5]
    k = 3
    sol = Solution()
    print(sol.kthSmallestPrimeFraction(arr, k))
