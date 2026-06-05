class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)-1
        COLS = len(matrix[0])-1

        L = 0
        R = ROWS
        print("L : ", L)
        print("R : ", R)
        
        while L <= R:
            M = (L+R)//2
            
            print("M front: ", matrix[M][0])
            print("M end :",matrix[M][-1] )

            if target < matrix[M][0]:
                R = M-1
            elif target > matrix[M][-1]:
                L = M + 1
            elif matrix[M][0] <= target and target <= matrix[M][-1] :  #found the right row
                l = 0
                r = COLS
                while l <= r:
                    m = (l+r)//2
                    print("in row m: ", matrix[M][m])
                    if matrix[M][m] == target:
                        return True
                    elif matrix[M][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
        return False 
        