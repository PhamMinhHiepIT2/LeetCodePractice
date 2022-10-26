from typing import List
import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        if n == 1:
            return ["Gold Medal"]
        st = []
        for i in range(n):
            st.append((score[i], i))
        st.sort(key=lambda x: x[0], reverse=True)
        res = [None for _ in range(n)]
        for i in range(n):
            if i == 0:
                res[st[i][1]] = "Gold Medal"
            elif i == 1:
                res[st[i][1]] = "Silver Medal"
            elif i == 2:
                res[st[i][1]] = "Bronze Medal"
            else:
                res[st[i][1]] = str(i+1)
        return res


def solve_with_heap(score: List):
    n = len(score)
    print(score)
    st = {}
    for i in range(n):
        st[score[i]] = i
    print(st)
    heapq.heapify(score)
    top_prize = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    res = [None for _ in range(n)]
    rank = n
    while score:
        a = heapq.heappop(score)
        if rank <= 3:
            res[st[a]] = top_prize[rank-1]
        else:
            res[st[a]] = str(rank)
        rank -= 1
    return res


if __name__ == "__main__":
    score = [5, 4, 3, 2, 1]
    print(Solution().findRelativeRanks(score))
    score = [5, 4, 3, 2, 1]
    solve_with_heap(score)
