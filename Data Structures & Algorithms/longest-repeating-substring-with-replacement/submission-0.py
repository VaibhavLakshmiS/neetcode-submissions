class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        seen = {}
        max_freq = 0
        best = 0

        for end in range(len(s)):
            seen[s[end]] = 1 + seen.get(s[end], 0)
            max_freq = max(max_freq, seen[s[end]])

            window_len = end - start + 1

            while window_len - max_freq > k:
                seen[s[start]] -= 1
                start += 1
                window_len = end - start + 1

            best = max(best, window_len)

        return best