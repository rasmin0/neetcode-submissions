class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        

        def bfs(r, c):
            nonlocal grid, ROWS, COLS
            q = deque()
            visited = set()

            q.append((r, c))
            visited.add((r, c))

            length = 1

            while q:
                levelSize = len(q)

                for _ in range(levelSize):
                    row, col = q.popleft()

                    if row == ROWS - 1 and col == COLS - 1:
                        return length

                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                    for dr, dc in directions:
                        nR = row + dr
                        nC = col + dc

                        if nR in range(ROWS) and nC in range(COLS) and (nR, nC) not in visited and grid[nR][nC] == 0:
                            q.append((nR, nC))
                            visited.add((nR, nC))
                length += 1
            
            return -1
        
        return bfs(0, 0)