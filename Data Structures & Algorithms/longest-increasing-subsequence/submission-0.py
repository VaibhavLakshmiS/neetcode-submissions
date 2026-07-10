class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        input: nums=[9,1,4,2,3,3,7]
        dp = [1, 1, 2, 2, 3, 3, 4]
        
        """
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp [i] = max(dp[i],1+dp[j])
        return max(dp)