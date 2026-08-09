class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        max_ar = 0
        while left<right:
                width = right-left
                area = min(heights[left],heights[right])*width
                max_ar = max(max_ar,area)
                if heights[left]<heights[right]:
                    left+=1
                else:
                    right-=1
                
        return max_ar
