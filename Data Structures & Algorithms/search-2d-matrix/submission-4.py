class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:
            midRow = (top + bot) // 2

            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
            
        if not (top <= bot):
            return False
            
        l = 0
        r = COLS - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[midRow][mid]:
                l = mid + 1
            elif target < matrix[midRow][mid]:
                r = mid - 1
            else:
                return True
        return False