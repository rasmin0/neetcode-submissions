class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let HR(i) denote the max amount of money 
        # you can rob from the first i houses
        # 0 <= i <= n, n = len(nums)
        # Solve HR(n)
        # BC: if i = 0: 0
        # HR(i) = 0 if i = 0
        #         max(nums[i] + HR(i - 2), HR(i - 1)) if i > 0

        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        
        return dp[n]

