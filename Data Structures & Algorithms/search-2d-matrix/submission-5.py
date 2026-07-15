class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)       # rows
        c = len(matrix[0])    # cols

        l = 0
        h = r - 1
        m1 = 0

        while l <= h:
            m = (l + h) // 2

            if matrix[m][0] > target:
                h = m - 1
            elif matrix[m][0] < target and target < matrix[m][c - 1]:
                m1 = m
                break
            elif target > matrix[m][c - 1]:
                l = m + 1
            else:
                return True
        
        l = 0
        h = c - 1
        while l <= h:
            m2 = (l + h) // 2

            if target > matrix[m1][m2]:
                l = m2 + 1
            elif target < matrix[m1][m2]:
                h = m2 - 1
            else:
                return True
        
        return False



