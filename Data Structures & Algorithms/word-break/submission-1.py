class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        s="neetcode"
        wordDict=["neet","code"]
        n=8
        dp = [True,False,False,False,True,False,False,False,True]
        neet
        word_len=4
        end = 0+4
        if end<=8 and s[0:4] == word = = neet:
            dp[end]=True
        word code
        word_len=4
        end = 0+4
        if end<=8 and s[0:4] == word! code 
        skip
        start = 1
        start = 2
        start=3
        start=4
        neet case that would be invalid
        code case
        word-len =4
        end = 4+4 = 8
        if 8<=8 and s[4:8] == code:
            dp[8] = True
        dp[n]
        -3
        -3>=0 no 

         


        """
        n = len(s)

        dp = [False] * (n + 1)

        dp[0] = True

        for start in range(0,n + 1):
            if dp[start] == True:

                for word in wordDict:
                    word_length = len(word)
                    end = start + word_length

                    if end <= n and s[start:end] == word:
                        dp[end] = True

        return dp[n]