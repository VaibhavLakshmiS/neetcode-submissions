class Solution:
    def maxArea(self, height: List[int]) -> int:
      l = 0
      r = len(height)-1
      max_area = 0
      while l<r:
        width = r - l
        area = min(height[l],height[r])*width
        max_area = max(max_area,area)
        if height[r]>height[l]:
            l+=1
        else:
            r-=1
      return max_area