class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        nums = [1, 2, 3, 4]

        total_sum = 10
        target = 10 // 2 = 5

        dp[i] = can we create sum i?

        dp = [True, False, False, False, False, False]

        After processing 1:
        dp = [True, True, False, False, False, False]

        After processing 2:
        dp = [True, True, True, True, False, False]

        After processing 3:
        dp = [True, True, True, True, True, True]

        dp[5] is True, so return True.
        """

        total_sum = sum(nums)

        # An odd total cannot be divided into two equal sums
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # dp[i] = whether we can create sum i
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for current_sum in range(target, num - 1, -1):
                previous_sum = current_sum - num

                if dp[previous_sum]:
                    dp[current_sum] = True

            # Stop early if the target can already be created
            if dp[target]:
                return True

        return False