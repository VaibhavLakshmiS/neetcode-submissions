class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        jumps=0
        max_step = 0 
        while right < len(nums) - 1:
            farthest = 0

            for i in range(left, right + 1):#(0,1)
                farthest = max(farthest, i + nums[i]) #(2,4)

            left = right + 1 #1
            right = farthest#4
            jumps += 1#1

        return jumps

