from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)  # min and max posible bags
        while low < high:
            mid = (low + high) // 2
            print(f"Mid={mid}, low={low}, high={high}")
            a = sum((n - 1) // mid for n in nums)
            print(f"Sum = {a}")
            if a <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return high


if __name__ == "__main__":
    nums = [9]
    maxOperations = 2
    sol = Solution()
    print(sol.minimumSize(nums, maxOperations))
