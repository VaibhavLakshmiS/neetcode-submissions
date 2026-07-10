class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        nums = [1, 2, 3, 4]

        total_sum = 10
        target = 10 // 2 = 5

        """

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                prev = i - num

                if dp[prev]:
                    dp[i] = True

        return dp[target]
