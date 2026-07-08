class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(n):
                coin = coins[j]
                rem_amount = i-coin
                if rem_amount >= 0:
                    curr_amt = 1+dp[rem_amount]
                    dp[i]  = min(dp[i],curr_amt)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
               
        
