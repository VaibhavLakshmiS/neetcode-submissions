class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        # Count characters in s1
        for char in s1:
            need[char] = 1 + need.get(char, 0)

        left = 0

        for right in range(len(s2)):
            # Add right character into the window
            char = s2[right]
            window[char] = 1 + window.get(char, 0)

            # If window is bigger than len(s1), remove left character
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                left += 1

            # If current window count matches s1 count, permutation exists
            if window == need:
                return True

        return False