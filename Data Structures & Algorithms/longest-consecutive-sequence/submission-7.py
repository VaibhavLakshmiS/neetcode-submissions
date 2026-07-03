class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        start_streak =1 
        longest = 1
        if not nums:
            return 0
        for i in range (len(nums_sorted)-1):
            count=0
            if nums_sorted[i] == nums_sorted[i+1]:
                continue
            if nums_sorted[i]+1 == nums_sorted[i+1]:
                start_streak+=1
            else:
                start_streak=1
            longest = max(longest, start_streak)
        return longest
        