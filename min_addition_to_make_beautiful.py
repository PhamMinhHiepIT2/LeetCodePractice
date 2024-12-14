from symbol import power
import time


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        if target > 108:
            return 0
        if calculate_sum_digits(n) <= target:
            return 0
        if n == 1 and target == 1:
            return 0
        if target == 1 and n != 1:
            return 10**(len(str(n))) - n
        i = 10 - n % 10
        r = 10**(len(str(n))) - n
        # print(f"r: {r} | i: {i}")
        for j in range(0, r, 10):
            # print(f"n+i: {n+i} | sum: {calculate_sum_digits(n+i+j)} | i: {i}")
            if calculate_sum_digits(n+i+j) <= target:
                return i+j

        return 0


def calculate_sum_digits(n: int):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    # print(s)
    return s


def bs(l: int, r: int, target: int, ans: int):
    if r <= l:
        return l

    mid = l + (r-l) // 2
    # print(mid)
    if calculate_sum_digits(mid) <= target and mid < ans:
        ans = mid
        return ans
    else:
        left_res = bs(l, mid-1, target, ans)
        print(f"Left res: {left_res}")
        right_res = bs(mid+1, r, target, ans)
        print(f"Right res: {right_res}")
        return min(left_res, right_res)


if __name__ == "__main__":
    # print(Solution().makeIntegerBeautiful(575, 8))
    print(bs(467, 1000, 6, 1000))
