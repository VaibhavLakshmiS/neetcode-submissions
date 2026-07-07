class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        dp[0] = 0
        for i in range(2,n+1):
            onestep = dp[i-1]+cost[i-1]
            twostep = dp[i-2]+cost[i-2]
            dp[i] = min(onestep,twostep)

        return dp[n]