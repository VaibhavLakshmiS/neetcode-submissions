class Solution:
    def rob(self, nums: List[int]) -> int:
        total_house = len(nums)
        dp = [0] * (total_house + 1)

        for i in range(1, total_house + 1):
            rob = dp[i - 2] + nums[i - 1]
            skip = dp[i - 1]

            dp[i] = max(rob, skip)

        return dp[total_house]