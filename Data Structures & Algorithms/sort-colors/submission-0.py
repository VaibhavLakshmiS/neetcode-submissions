class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        freq_map={}
        while nums:
            if nums[i] in freq_map:
                freq_map[nums[i]]+=1
            else:
                freq_map[nums[i]]=1
            nums.pop(i)
            
        while freq_map:
            key = min(freq_map)
            count = freq_map[key]
            while count:
                nums.append(key)
                count-=1
            freq_map.pop(key)

    


