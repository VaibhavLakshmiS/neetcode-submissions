class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        q =[(1,0)]
        v =[(0,0),(1,0),(1,1)]
        """
        q = collections.deque()
        visit = set()
        row = len(grid) # 2
        column = len (grid[0]) #2
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        directions= [[1,0],[-1,0],[0,1],[0,-1]]
        dist = 0
        while q:
            r,c = q.popleft()
            # grid[r][c] = dist
            for dr,dc in directions:
                n_r = r+dr # 1
                n_c = c+dc # 1
                if (n_r<0 or n_r == row or n_c<0 or n_c==column or (n_r,n_c)in visit or grid[n_r][n_c]==-1):
                    continue
                grid[n_r][n_c]= grid[r][c]+1

                visit.add((n_r,n_c))
                q.append((n_r,n_c))
