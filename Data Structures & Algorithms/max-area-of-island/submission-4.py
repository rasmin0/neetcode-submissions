class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(r, c, visited):
            q = deque()
            q.append((r, c, 1))
            visited.add((r, c))

            area = 0
            while q:
                row, col, length = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc, length + 1))
                        visited.add((nr, nc))
            
            return area

                    

        visited = set()
        maxArea = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs(i, j, visited)
                    maxArea = max(maxArea, area)
                    visited.add((i, j))
        return maxArea