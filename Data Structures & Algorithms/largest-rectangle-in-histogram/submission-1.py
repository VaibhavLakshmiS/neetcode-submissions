class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        s = [7,1,7,2,2,4]
        width = 6
        n_h =1
        ar = 6
        max_ar = (max_ar, ar) = 6
        """
        max_ar = 0 
        stack = [] # pair of index and height
        for i,h in enumerate(heights):
            start = i # extend 
            while stack and stack[-1][1]>h: # stack[-1][1] the height of the top most elemet in stack
                  ind, height = stack.pop()
                  max_ar = max(max_ar,height*(i-ind))    
                  start = ind
            stack.append((start,h))
        for i,h in stack:
            max_ar = max(max_ar, h*(len(heights)-i))
        return max_ar
