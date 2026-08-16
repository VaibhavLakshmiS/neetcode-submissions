class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hs = {}
        new_list = []
        n = len(nums)
        for i in nums:
            if i in hs:
                hs[i]+=1
            else:
                hs[i] = 1
        for k,v in hs.items():
            if v > n//3:
                new_list.append(k)
        return new_list
