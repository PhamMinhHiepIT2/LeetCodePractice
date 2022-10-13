from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        p = 0
        for i in range(n-2):
            # if nums[0], nums[1], nums[2] not accepted => nums[0] >= nums[1] + nums[2] >= nums[1] + nums[3], ...
            if check_rectangle(nums[i], nums[i+1], nums[i+2]):
                return calculate_perimeter(nums[i], nums[i+1], nums[i+2])
        return p


def check_rectangle(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        return 1
    else:
        return 0


def calculate_perimeter(x, y, z):
    return x + y + z


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(Solution().largestPerimeter(nums))
