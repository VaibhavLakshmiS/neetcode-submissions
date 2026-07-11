class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,4,6]
        
        Output: [48,24,12,8]
        """
        n = len(nums)
        arr_res = [0]*n
        for i in range(n):
            prod=1
            for j in range(n):
                if i!=j:
                    prod*=nums[j]
            arr_res[i]=prod
        return arr_res
                