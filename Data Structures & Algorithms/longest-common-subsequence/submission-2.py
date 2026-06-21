class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Let LCS(i, j) denote the longest common subsequence between the first i characters of text1
        # and the first j characters of text2.

        # 0 <= i <= n
        # 0 <= j <= m

        # Solve LCS(n, m)

        # LCS(i, j) := 0 if i = 0 or j = 0, 1 + max(LCS(i - 1, j), LCS(i, j - 1))

        n = len(text1)
        m = len(text2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]