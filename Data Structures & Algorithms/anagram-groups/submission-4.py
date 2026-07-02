class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            alp = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                alp[index] += 1

            key = tuple(alp)

            if key not in d:
                d[key] = []

            d[key].append(word)

        return list(d.values())