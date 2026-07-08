class Solution:
    def countSubstrings(self, s: str) -> int:
        tot_sub = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tot_sub += 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                tot_sub += 1
                l -= 1
                r += 1

        return tot_sub