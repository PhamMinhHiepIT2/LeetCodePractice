class Solution:
    def __init__(self) -> None:
        self.vowels = ['a', 'e', 'u', 'o', 'i']

    def get_vowels(self, s: str):
        ids = []
        for i in range(len(list(s))):
            c = s[i]
            if c.lower() in self.vowels:
                ids.append(i)
        return ids

    def map_ids(self, ids: list):
        revert_ids = ids[::-1]
        map_ids = []
        for i in range(len(ids)):
            map_ids.append((ids[i], revert_ids[i]))
        return map_ids

    def reverseVowels(self, s: str) -> str:
        vowel_ids = self.get_vowels(s)
        map_vowel_ids = self.map_ids(vowel_ids)
        st = list(s)
        raw = list(s)
        for i in range(len(map_vowel_ids)):
            m = map_vowel_ids[i]
            st[m[0]] = raw[m[1]]
        return "".join(st)


if __name__ == "__main__":
    s = "hello"
    print(Solution().reverseVowels(s))
