class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c, visited):
            q = deque()

            q.append((r, c))
            visited.add((r, c))

            cur = 1
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    nR = row + dr
                    nC = col + dc

                    if (
                        nR in range(ROWS)
                        and nC in range(COLS)
                        and grid[nR][nC] == 1
                        and (nR, nC) not in visited
                    ):
                        cur += 1
                        visited.add((nR, nC))
                        q.append((nR, nC))

            return cur
        
        maxArea = 0
        visited = set()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, bfs(i, j, visited))

        return maxArea           

