from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        flag = 0
        res = 0
        if len(s) == 0:
            return 0
        s_list = list(s)
        if len(set(s_list)) == 1:
            return len(s_list)
        for i in set(s_list):
            count = s.count(i)
            print("Count %s is %d" % (i, count))
            if count % 2 == 0:
                res += count
            elif count % 2 == 1 and flag == 0:
                res += count
                flag = 1
            elif count % 2 == 1 and flag != 0:
                res += count - 1
        print(res)
        return res


class HashMapSolution:
    def longestPalindrome(self, s: str) -> int:
        print(Counter(s))
        count = sum([(x//2) * 2 for x in Counter(s).values()])
        return count if count == len(s) else (count + 1)


if __name__ == "__main__":
    s = "bababababa"
    print(HashMapSolution().longestPalindrome(s))
