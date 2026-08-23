class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        q = deque()
        visited= set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        distance = 1
        while q:
            size = len(q)

            for _ in range(size):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        grid[nr][nc] = distance
            distance += 1
        
        
        
