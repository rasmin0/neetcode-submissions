class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        pacificQ = deque()
        atlanticQ = deque()
        pVisited = set()
        aVisited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    pacificQ.append((i, j))
                    pVisited.add((i, j))
                if i == ROWS - 1 or j == COLS - 1:
                    atlanticQ.append((i, j))
                    aVisited.add((i, j))
        
        while pacificQ:
            row, col = pacificQ.popleft()

            for dr, dc in directions:
                nr = dr + row
                nc = dc + col

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[row][col] and (nr, nc) not in pVisited:
                    pacificQ.append((nr, nc))
                    pVisited.add((nr, nc))
        
        while atlanticQ:
            row, col = atlanticQ.popleft()

            for dr, dc in directions:
                nr = dr + row
                nc = dc + col

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[row][col] and (nr, nc) not in aVisited:
                    atlanticQ.append((nr, nc))
                    aVisited.add((nr, nc))
        
        union = pVisited.intersection(aVisited)

        res = []
        for r, c in union:
            res.append([r, c])
        
        return res



