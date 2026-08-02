class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))

        minutes = 0

        while q:
            sizeQ = len(q)
            rotted = False

            for i in range(sizeQ):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (
                        0 <= nr < ROWS 
                        and 0 <= nc < COLS 
                        and grid[nr][nc] == 1
                        ):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        rotted = True
            if rotted:
                minutes += 1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return minutes
