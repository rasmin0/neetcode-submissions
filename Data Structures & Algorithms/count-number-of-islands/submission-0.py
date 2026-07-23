class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, visit):
            if (min(r, c) < 0 
            or r >= ROWS 
            or c >= COLS 
            or grid[r][c] == "0" 
            or (r, c) in visit):
                return
            
            visit.add((r, c))

            dfs(r + 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r - 1, c, visit)
            dfs(r, c - 1, visit)
        
        visit = set()

        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visit:
                    count += 1
                    dfs(i, j, visit)
        
        return count
            
