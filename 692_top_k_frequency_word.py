from itertools import count
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        res = []
        st = []
        sorted_counter = []
        for item in counter.most_common():
            print(f"Item: {item}")
            if len(st) == 0 or item[1] == st[-1][1]:
                st.append(item)
            elif item[1] != st[-1][1]:
                st.sort(reverse=False)

                sorted_counter += st
                st = []
                st.append(item)
        st.sort(reverse=True)
        while st:
            sorted_counter.append(st.pop())
        for i in range(k):
            res.append(sorted_counter[i][0])
        return res


if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    print(Solution().topKFrequent(words, k))
