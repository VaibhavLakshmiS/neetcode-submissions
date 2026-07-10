class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        dfs


        """
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        island_count = 0

        def dfs(row, col):
            # Stop if outside the grid
            if row < 0 or row >= rows:
                return

            if col < 0 or col >= cols:
                return

            # Stop if this cell is water
            if grid[row][col] == "0":
                return

            # Stop if already visited
            if (row, col) in visited:
                return

            # Mark current land as visited
            visited.add((row, col))

            # Visit all four neighbours
            dfs(row - 1, col)  # up
            dfs(row + 1, col)  # down
            dfs(row, col - 1)  # left
            dfs(row, col + 1)  # right

        # Check every cell
        for row in range(rows):
            for col in range(cols):

                # New unvisited land means a new island
                if grid[row][col] == "1" and (row, col) not in visited:
                    island_count += 1
                    dfs(row, col)

        return island_count
    