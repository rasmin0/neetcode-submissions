class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Let Ways(i, j) denote the number of possible unique paths 
        # from the top left to position (i, j).

        # 0 <= i < m
        # 0 <= j < n
        # Solve Ways(m - 1, n - 1)
        # Ways(i, j) := 1 if i = 0 or j = 0, Ways[i - 1][j] + Ways[i][j - 1]
        
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
        return dp[m - 1][n - 1]