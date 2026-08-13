class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        og = image[sr][sc]
        if og == color:
            return image
        image[sr][sc] = color

        q = deque()
        visited = set()

        q.append((sr, sc))
        visited.add((sr, sc))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = dr + row
                nc = dc + col

                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == og and (nr, nc) not in visited:
                    image[nr][nc] = color
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        return image