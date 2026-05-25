class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = []
        start = 0
        end = len(s)

        while start < end:
            if s[start] in seen:
                while s[start] in seen:
                    seen.pop(0)

            seen.append(s[start])
            max_len = max(max_len, len(seen))

            start += 1

        return max_len
