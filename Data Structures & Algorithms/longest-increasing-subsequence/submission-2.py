class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Let LIS(i) denote the length of the longest increasing
        # subsequence ending at index i.

        # 0 <= i < n

        # Solve max(LIS(i))

        n = len(nums)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)