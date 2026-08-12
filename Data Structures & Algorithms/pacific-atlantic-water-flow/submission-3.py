class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        q1 = deque()
        pacificVisited = set()

        for i in range(ROWS):
            q1.append((i, 0))
            pacificVisited.add((i, 0))

        for j in range(1, COLS):
            q1.append((0, j))
            pacificVisited.add((0, j))
        
        while q1:
            row, col = q1.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[row][col] and (nr, nc) not in pacificVisited:
                    q1.append((nr, nc))
                    pacificVisited.add((nr, nc))
        
        q2 = deque()
        atlanticVisited = set()
        
        for i in range(ROWS):
            q2.append((i, COLS - 1))
            atlanticVisited.add((i, COLS - 1))
        
        for j in range(COLS - 1):
            q2.append((ROWS - 1, j))
            atlanticVisited.add((ROWS - 1, j))
        
        while q2:
            row, col = q2.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[row][col] and (nr, nc) not in atlanticVisited:
                    q2.append((nr, nc))
                    atlanticVisited.add((nr, nc))
        
        res = []
        union = pacificVisited.intersection(atlanticVisited)

        for r, c in union:
            res.append([r, c])
        
        return res