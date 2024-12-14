from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        temp = height[0]
        cur_idx = 0
        start = False
        for i in range(n):
            if height[i] != 0:
                start = True
            if height[i] == 0 and start == False:
                continue

            if height[i] >= temp:
                print(
                    f"Checking index {i}: temp = {temp}, cur_idx = {cur_idx}")
                for j in range(cur_idx+1, i):
                    print(f"\tpre result = {res}")
                    res += abs(height[cur_idx] - height[j])
                    print(
                        f'\theight[i] = {height[cur_idx]}, height[j]={height[j]}, res = {res} ')
                print(f"\tResult checking index {i}: res = {res}")
                cur_idx = i
                temp = height[i]
        print(f"Cur_idx = {cur_idx}")
        if cur_idx != n-1:
            res += self.sub(height=height[cur_idx:][::-1])
            # for i in range(cur_idx+1, n):
            #     print(f"\tpre result = {res}")
            #     if i < n-1 and height[i+1] > 0:
            #         res += abs(height[cur_idx+1] - height[i])
            #         print(
            #             f'\theight[i] = {height[cur_idx+1]}, height[j]={height[i]}, res = {res} ')
            #     print(f"\tResult checking index {i}: res = {res}")
            #     if i == n-1 and height[i] > height[i-1]:
            #         res += abs(height[i] - height[i-1])
        print(res)
        return res

    def sub(self, height):
        n = len(height)
        res = 0
        temp = height[0]
        cur_idx = 0
        start = False
        for i in range(n):
            if height[i] != 0:
                start = True
            if height[i] == 0 and start == False:
                continue

            if height[i] >= temp:
                for j in range(cur_idx+1, i):
                    res += abs(height[cur_idx] - height[j])
                cur_idx = i
                temp = height[i]
        return res


if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [4, 2, 3]
    # height = [5, 4, 1, 2]
    sol = Solution()
    sol.trap(height=height)
