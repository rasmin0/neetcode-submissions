class Solution:
    def rob(self, nums: List[int]) -> int:
        # Let HR(i) denote the maximum amount of money you can rob from
        # the first i houses.

        # 0 <= i <= n
        # Solve HR(n)

        n = len(nums)

        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
        
        return dp[n]