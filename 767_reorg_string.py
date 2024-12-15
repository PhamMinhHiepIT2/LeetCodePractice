from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        arr = list(s)
        counter = Counter(arr)

        el = dict(counter)
        el = dict(
            sorted(el.items(), key=lambda item: item[1], reverse=True))
        chars = list(el.keys())
        # print(el)
        res = ""
        for k in range(len(arr)):
            el = dict(
                sorted(el.items(), key=lambda item: item[1], reverse=True))
            chars = list(el.keys())
            i = 0
            for i in range(len(chars)):
                c = chars[i]
                if len(res) == 0:
                    res += c
                    el[c] -= 1
                    break
                else:
                    if res[-1] != c and el[c] > 0:
                        res += c
                        el[c] -= 1
                        break
                    else:
                        el = dict(
                            sorted(el.items(), key=lambda item: item[1], reverse=True))
                        chars = list(el.keys())
                        continue

        if len(res) != len(arr):
            return ""
        else:
            return res


if __name__ == "__main__":
    s = "aab"
    sol = Solution()
    print(sol.reorganizeString(s))
    print()
    s = "vvvlo"
    sol = Solution()
    print(sol.reorganizeString(s))

    print()
    s = "aaab"
    sol = Solution()
    print(sol.reorganizeString(s))

    print()
    s = "baaba"
    sol = Solution()
    print(sol.reorganizeString(s))

    print()
    s = "aabbcc"
    sol = Solution()
    print(sol.reorganizeString(s))
