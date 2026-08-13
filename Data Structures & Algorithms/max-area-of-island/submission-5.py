class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            area = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        area += 1
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
            return area



        visited = set()
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs(i, j)
                    maxArea = max(area, maxArea)
        
        return maxArea

