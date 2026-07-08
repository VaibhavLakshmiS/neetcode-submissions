class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(n):
                coin = coins[j]

                if i - coin >= 0:
                    curr_amount = 1 + dp[i - coin]
                    dp[i] = min(dp[i], curr_amount)

        if dp[amount] == float("inf"):
            return -1

        return dp[amount]
        
