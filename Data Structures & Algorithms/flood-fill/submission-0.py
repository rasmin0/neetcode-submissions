class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        originalColor = image[sr][sc]
        def dfs(image, r, c, visit):
            nonlocal sr, sc, color
            if min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != originalColor or (r, c) in visit:
                return

            image[r][c] = color

            visit.add((r, c))

            dfs(image, r + 1, c, visit)
            dfs(image, r, c + 1, visit)
            dfs(image, r - 1, c, visit)
            dfs(image, r, c - 1, visit)


            return image

        return dfs(image, sr, sc, set())