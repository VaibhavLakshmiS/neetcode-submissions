class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        [-3,-2,-1]
         n= 3
         res =-3
         prefix =suffix = 0
         pre = -3
         suf = -1
         res = max(-3,max(-3,-1)) = -1

         pre = -2*-3 = 6
         suf = -2*-1 = 2
         res = 6
         6
         """
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res