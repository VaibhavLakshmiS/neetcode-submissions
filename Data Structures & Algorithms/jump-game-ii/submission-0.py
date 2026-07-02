class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curr_end= 0
        max_step = 0 
        for i in range(len(nums)-1):
            max_step = max(max_step,i+nums[i])
            if i == curr_end:
                jump = jump + 1
                curr_end = max_step

        return jump