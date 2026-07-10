class Solution:
    def maxArea(self, heights: List[int]) -> int:
      l = 0 
      r = len(heights)-1
      max_ar = 0
      while l<r:
        width = r-l
        length = min(heights[r],heights[l])
        area = width*length
        max_ar = max(max_ar,area)
        if heights[l]<heights[r]:
            l+=1
        else:
            r-=1
      return max_ar


