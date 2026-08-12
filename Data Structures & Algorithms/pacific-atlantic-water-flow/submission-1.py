class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []
        globalVisited = set()

        def bfs(r, c):
            q = deque()
            visited = set()

            q.append((r, c))
            visited.add((r, c))

            pacific = False
            atlantic = False
            while q:
                row, col = q.popleft()
                

                if row == 0 or col == 0:
                    pacific = True
                if row == ROWS - 1 or col == COLS - 1:
                    atlantic = True
                if pacific and atlantic:
                    globalVisited.add((r, c))
                    return
                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] <= heights[row][col] and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        for i in range(ROWS):
            for j in range(COLS):
                bfs(i, j)
        
        for r, c in globalVisited:
            res.append([r, c])

        return res

                