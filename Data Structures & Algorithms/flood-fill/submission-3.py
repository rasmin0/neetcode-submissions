class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        og = image[sr][sc]
        visited = set()

        def bfs(r, c):
            if image[r][c] == og:
                image[r][c] = color
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            directions = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nR = row + dr
                    nC = col + dc

                    if 0 <= nR < ROWS and 0 <= nC < COLS and image[nR][nC] == og and (nR, nC) not in visited:
                        image[nR][nC] = color
                        q.append((nR, nC))
                        visited.add((nR, nC))
            
            return image
        
        return bfs(sr, sc)

