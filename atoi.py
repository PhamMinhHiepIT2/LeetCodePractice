import re


class Solution:
    def __init__(self):
        self.neg = -2**31
        self.pos = 2**31 - 1

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        regex = "^[-+]?[\d]+"
        x = re.compile(regex)
        mo = x.search(s)
        if mo is None:
            return 0
        res = int(mo.group())
        if res < self.neg:
            return self.neg
        elif res > self.pos:
            return self.pos
        else:
            return res


if __name__ == "__main__":
    s = "-4193 with words"
    print(Solution().myAtoi(s))
