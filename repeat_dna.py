from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        res = {}
        for i in range(n-9):
            sub_dna = s[i:i+10]
            print(i, sub_dna)
            if sub_dna not in res:
                res[sub_dna] = 1
            else:

                res[sub_dna] += 1
            print(res[sub_dna])
        print(res)
        ans = []
        for key, val in res.items():
            if val > 1:
                ans.append(key)
        return ans


if __name__ == "__main__":
    s = "AAAAAAAAAAA"
    print(Solution().findRepeatedDnaSequences(s))
