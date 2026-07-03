class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        n_s = set(nums)
        lc=0
        for num in n_s:
            if num-1 not in n_s:
               lc = 1
               cur = num
               while cur+1 in n_s:
                    lc+=1
                    cur+=1
               longest = max(longest,lc)
        return longest

