class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        [[1,1,0],[0,1,1],[0,1,2]]
        fresh = 5
        q = (2,2)


        """

        q = collections.deque()
        fresh = 0
        time = 0
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                        n_r, n_c = r + dr, c + dc
                        if (n_r in range(len(grid))
                            and n_c in range(len(grid[0]))
                            and grid[n_r][n_c] == 1
                        ):
                            grid[n_r][n_c] = 2
                            q.append((n_r, n_c))
                            fresh -= 1
            time += 1
        return time if fresh == 0 else -1
            


        