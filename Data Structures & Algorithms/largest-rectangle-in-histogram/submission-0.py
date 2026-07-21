class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        heights = [7, 1, 7, 2, 2, 4]
        indexes =  [0, 1, 2, 3, 4, 5]
        n = 6

        stack stores indexes of bars in increasing-height order.

        Start:
        stack = []
        maxArea = 0

        i = 0, height = 7
        stack is empty
        push index 0
        stack = [0]

        i = 1, height = 1
        heights[0] = 7 >= 1, so pop index 0

        height = 7
        stack is now empty
        width = i = 1
        area = 7 * 1 = 7
        maxArea = 7

        push index 1
        stack = [1]

        i = 2, height = 7
        heights[1] = 1 < 7
        push index 2
        stack = [1, 2]

        i = 3, height = 2
        heights[2] = 7 >= 2, so pop index 2

        height = 7
        stack = [1]
        width = i - stack[-1] - 1
              = 3 - 1 - 1
              = 1
        area = 7 * 1 = 7
        maxArea = 7

        heights[1] = 1 < 2
        push index 3
        stack = [1, 3]

        i = 4, height = 2
        heights[3] = 2 >= 2, so pop index 3

        height = 2
        stack = [1]
        width = 4 - 1 - 1 = 2
        area = 2 * 2 = 4
        maxArea = 7

        push index 4
        stack = [1, 4]

        i = 5, height = 4
        heights[4] = 2 < 4
        push index 5
        stack = [1, 4, 5]

        i = 6, sentinel iteration
        i == n, so remove every remaining index.

        Pop index 5:
        height = 4
        stack = [1, 4]
        width = 6 - 4 - 1 = 1
        area = 4 * 1 = 4
        maxArea = 7

        Pop index 4:
        height = 2
        stack = [1]
        width = 6 - 1 - 1 = 4
        area = 2 * 4 = 8
        maxArea = 8

        Pop index 1:
        height = 1
        stack = []
        width = i = 6
        area = 1 * 6 = 6
        maxArea = 8

        Final answer = 8

        The largest rectangle uses:
        heights [7, 2, 2, 4] from indexes 2 through 5,
        with minimum height 2 and width 4.

        Area = 2 * 4 = 8
        """

        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (
                i == n or heights[stack[-1]] >= heights[i]
            ):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)

            stack.append(i)

        return maxArea