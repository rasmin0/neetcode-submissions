class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c, 1))

            while q:
                row, col, length = q.popleft()

                if row == ROWS - 1 and col == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (
                        0 <= nr < ROWS 
                        and 0 <= nc < COLS 
                        and grid[nr][nc] == 0 
                        and (nr, nc) not in visited
                        ):
                        q.append((nr, nc, length + 1))
                        visited.add((nr, nc))
            return -1
            
        return bfs(0, 0)





