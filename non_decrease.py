from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        if check_non_decrease_list(nums):
            return count
        for i in range(n):
            unpected_indexes = find_index(nums)
            nums = remove_unexpected_index(nums, indexes=unpected_indexes)
            count += 1
            if check_non_decrease_list(nums):
                break
        return count


def find_index(arr):
    n = len(arr)
    indexes = []
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            indexes.append(i)
    return indexes


def remove_unexpected_index(arr: list, indexes: list):
    indexes.sort(reverse=True)
    for index in indexes:
        arr.pop(index)
    return arr


def check_non_decrease_list(arr: list):
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return 1
    else:
        return 0


def find_all_round_to_remove(arr):
    n = len(arr)
    ans = 0
    lst = [[nums[0], 0]]
    for i in range(1, len(nums)):
        cnt = 0
        while lst and lst[-1][0] > nums[i]:
            cnt = max(cnt + 1, lst[-1][1])
            lst.pop()
        lst.append([nums[i], cnt])
        ans = max(ans, cnt)
    return ans


class Solution1:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i]+1, dp[stack[-1]])
                stack.pop()
            stack.append(i)
        return max(dp)

    def totalStepsBFS(self, nums: List[int]) -> int:
        n = len(nums)
        l = [i-1 for i in range(n)]
        r = [i+1 for i in range(n)]
        q = []
        dist = dict()
        ans = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                q.append(i)
                dist[i] = 1
                ans = 1
        while len(q) != 0:
            u = q.pop(0)
            ans = max(ans, dist[u])
            if r[u] < n:
                l[r[u]] = l[u]
            if l[u] > -1:
                r[l[u]] = r[u]
            if r[u] not in dist and r[u] < n and nums[r[u]] < nums[l[u]]:
                dist[r[u]] = dist[u] + 1
                q.append(r[u])
        return ans


if __name__ == "__main__":
    nums = [7, 14, 4, 14, 13, 2, 6, 13]
    # nums.reverse()
    # print(nums)
    tmp = nums.copy()
    # print(find_all_round_to_remove(tmp))
    print(Solution1().totalSteps(nums))
