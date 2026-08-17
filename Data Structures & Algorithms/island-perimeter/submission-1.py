class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == 0:
                return 1
            
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            perimeter = 0

            for dr, dc in directions:
                    perimeter += dfs(r + dr, c + dc)
            
            return perimeter


        
        perimeter = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    perimeter = dfs(i, j)
        
        return perimeter