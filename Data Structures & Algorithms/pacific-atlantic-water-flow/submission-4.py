class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q1 = deque()
        q2 = deque()
        pacVisited = set()
        atlVisited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    q1.append((i, j))
                    pacVisited.add((i, j))
                if i == ROWS - 1 or j == COLS - 1:
                    q2.append((i, j))
                    atlVisited.add((i, j))
        
        def bfs(q, visited):
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[row][col] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        bfs(q1, pacVisited)
        bfs(q2, atlVisited)

        inter = pacVisited.intersection(atlVisited)

        res = []

        for r, c in inter:
            res.append([r, c])
        
        return res

        

                