class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_steps = len(cost)
        dp = [0] * (total_steps + 1)
        for i in range(2, total_steps + 1):
            onestep= dp[i-1]+cost[i-1]
            twostep = dp[i-2]+cost[i-2]
            dp[i] = min(onestep,twostep)
        return dp[total_steps]
            