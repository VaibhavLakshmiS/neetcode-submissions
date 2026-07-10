class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_total = sum(nums)

        # Odd total cannot be divided equally
        if sum_total % 2 != 0:
            return False

        tar = sum_total // 2

        dp = [False] * (tar + 1)
        dp[0] = True

        for num in nums:
            for j in range(tar, num - 1, -1):
                if dp[j - num] == True:
                    dp[j] = True

        return dp[tar]
                 
