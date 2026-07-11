class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,4,6]
        prefix = [1,1,2,8]
        postfix = [48,24,6,1]
        res = [1*48,1*24,2*6,1*8]

        arr_res [1,1,2,8]
        arr_res [1,1,12,8]

       postfix=48
       j = 0
       res[j] =48


        """
        n = len(nums)
        arr_res = [1]*n
        prefix = 1
        postfix = 1
        for i in range(n):
            arr_res[i] = prefix
            prefix*=nums[i]
        for j in range(n-1,-1,-1):
            arr_res[j]*=postfix
            postfix*=nums[j]
        return arr_res


        
            

