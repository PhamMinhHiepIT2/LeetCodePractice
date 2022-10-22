from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12:
            return []
        l = []
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ip = s[:i+1] + '.' + s[i+1:j+1] + \
                        '.' + s[j+1:k+1] + '.' + s[k+1:]
                    print(ip)
                    if is_valid(ip):
                        l.append(ip)

        return list(set(l))


def is_valid(ip):
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
                i[0] == '0'):
            return False
    return True


def convert(s):
    sz = len(s)
    if sz > 12:
        return []
    l = []
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                ip = s[:i+1] + '.' + s[i+1:j+1] + \
                    '.' + s[j+1:k+1] + '.' + s[k+1:]

                if is_valid(ip):
                    l.append(ip)

    return list(set(l))


if __name__ == "__main__":
    s = "0000"
    print(Solution().restoreIpAddresses(s))
