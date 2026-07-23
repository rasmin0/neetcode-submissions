class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, visited):
            if (r not in range(ROWS) 
                or c not in range(COLS) 
                or grid[r][c] == 0 
                or (r, c) in visited):

                return 0
            
            visited.add((r, c))

            cur = 1

            cur += dfs(r + 1, c, visited)
            cur += dfs(r - 1, c, visited)
            cur += dfs(r, c + 1, visited)
            cur += dfs(r, c - 1, visited)

            return cur

        maxCount = 0
        visited = set()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxCount = max(maxCount, dfs(i, j, visited))
        
        return maxCount
