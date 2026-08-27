class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        perimeter = 0

        def bfs(r, c):
            nonlocal perimeter
            q = deque()
            visited = set()

            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if not (0 <= nr < ROWS) or not (0 <= nc < COLS) or grid[nr][nc] == 0:
                        perimeter += 1

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    bfs(i, j)
                    return perimeter