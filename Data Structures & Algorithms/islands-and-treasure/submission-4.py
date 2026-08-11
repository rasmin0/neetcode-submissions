class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        distance = 0

        while q:
            size = len(q)

            for _ in range(size):
                row, col = q.popleft()

                if grid[row][col] == 2147483647:
                    grid[row][col] = distance

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            distance += 1

