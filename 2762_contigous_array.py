from typing import List
from collections import deque


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, res = 0, 0
        minD, maxD = deque(), deque()

        for r in range(len(nums)):
            while minD and nums[minD[-1]] >= nums[r]:
                minD.pop()
            while maxD and nums[maxD[-1]] <= nums[r]:
                maxD.pop()
            minD.append(r)
            maxD.append(r)
            print(f"r={r}, minD={minD}, maxD={maxD}")

            while nums[maxD[0]] - nums[minD[0]] > 2:
                l += 1
                if minD[0] < l:
                    minD.popleft()
                if maxD[0] < l:
                    maxD.popleft()

            res += r - l + 1
            print(f"l={l}, r={r}, res={res}")

        return res


if __name__ == "__main__":
    nums = [5, 4, 2, 4]
    sol = Solution()
    print(sol.continuousSubarrays(nums))
