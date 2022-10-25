from typing import List
from collections import Counter


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        judge = -1
        flag = 1
        normal_p = [el[0] for el in trust]
        trusted_p = [el[1] for el in trust]
        normal_counter = Counter(normal_p)
        trusted_counter = Counter(trusted_p)
        for el in trusted_counter.most_common():
            if el[1] == n-1:
                for i in normal_counter.most_common():
                    if el[0] == i[0]:
                        flag = 0
                        continue
                if flag == 1:
                    judge = el[0]

        return judge
        # print(trusted_counter)
        # print(normal_counter)


if __name__ == "__main__":
    n = 2
    trust = [[2, 1]]
    print(Solution().findJudge(n, trust))
