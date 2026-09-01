class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        q = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1) and board[i][j] == 'O':
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and board[nr][nc] == 'O':
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        
