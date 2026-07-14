class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            
            if grid[row][col] == 0:
                return 0

            # Mark this land as visited
            grid[row][col] = 0

            area = 1
            area += dfs(row - 1, col)  # up
            area += dfs(row + 1, col)  # down
            area += dfs(row, col + 1)  # right
            area += dfs(row, col - 1)  # left

            return area

        max_area = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 1:
                    current_area = dfs(row, col)
                    max_area = max(max_area, current_area)

        return max_area