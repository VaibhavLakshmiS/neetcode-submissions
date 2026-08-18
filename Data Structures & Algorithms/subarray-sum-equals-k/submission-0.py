class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        prefix sum 
        nums = [2,-1,1,2]
        k=2
        """
        res = 0 
        curSum = 0
        prefix = {0:1}
        for n in nums:
            curSum+=n
            dif = curSum-k
            res+= prefix.get(dif,0)
            prefix[curSum] = 1+prefix.get(curSum,0)
        return res
        

