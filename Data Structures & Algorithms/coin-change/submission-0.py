class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # dp[i] = minimum coins needed to make amount i
        dp = [amount + 1] * (amount + 1)

        # To make amount 0, we need 0 coins
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(n):
                coin = coins[j]

                if i - coin >= 0:
                    take_coin = 1 + dp[i - coin]
                    dp[i] = min(dp[i], take_coin)

        if dp[amount] == amount + 1:
            return -1

        return dp[amount]
        
