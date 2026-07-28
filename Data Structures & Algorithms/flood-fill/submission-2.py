class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        og = image[sr][sc]

        def dfs(r, c, visited):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or image[r][c] != og or (r, c) in visited:
                return image
            
            visited.add((r, c))

            image[r][c] = color

            dfs(r + 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r - 1, c, visited)
            dfs(r, c - 1, visited)

            return image
        
        return dfs(sr, sc, set())