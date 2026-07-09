class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        nums = [2,4,-3,5]
        n=4
        max_dp = [2,8,-3,5]
        min_dp = [2,4,-24,-120]
        ans = 2
        max_dp[1]= max(4,2*4,2*4)= 8
        min_dp[1]=min(4,2*4,2*4) = 4
        max_dp[2]= max(-3,8*-3,4*-3)= -3
        min_dp[2]=min(-3,8*-3,4*-3) = -24
        max_dp[3]= max(5,5*-3,-24*5)= 5
        min_dp[3]=min(5,-3*5,-24*5) = -120
        ans=max(ans,max_dp[i]) 
        8

        [-3,0,-2]
        n=3
        max_dp = [-3,0,0]
        min_dp = [-3,0,-2]
        max_dp[1]= max(0,-3*0,-3*0)= 0
        min_dp[1]=min(0,-3*0,-3*0) = 0
        max_dp[2]= max(-2,-2*0,-2*0)= 0
        min_dp[2]=min(-2,0,0) = -2
        ans = 0


        """
        n = len(nums) 
        max_dp = [0] * n
        min_dp = [0] * n
       
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        ans = nums[0]

        for i in range(1, n):

            max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i])

            ans = max(ans, max_dp[i])

        return ans
