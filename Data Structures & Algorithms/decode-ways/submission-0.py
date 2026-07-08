class Solution:
    def numDecodings(self, s: str) -> int:
            n = len(s)
            dp = [0] * (n + 1)
            dp[0] = 1 # empty string
            if s[0] != "0":
                dp[1] = 1
            else:
                return 0

            for i in range(2, n + 1):
                one_digit = s[i - 1]      
                two_digits = s[i - 2:i]   
                # 1- 9
                if one_digit != "0":
                    dp[i] += dp[i - 1]
                # 10 -26
                if 10 <= int(two_digits) <= 26:
                    dp[i] += dp[i - 2]

            return dp[n]