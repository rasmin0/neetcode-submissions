class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area



        visited = set()
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = dfs(i, j)
                    maxArea = max(area, maxArea)
        
        return maxArea

