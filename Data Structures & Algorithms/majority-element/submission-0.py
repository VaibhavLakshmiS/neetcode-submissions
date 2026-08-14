class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """

        """
        hs = {}
        for i in nums:
            if i not in hs:
                hs[i]=1
            hs[i]+=1
        key = max(hs,key=hs.get)
        return key
        
