class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = set(days)
        n = days[-1]

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i in d:
                dp[i] = min(costs[0] + dp[max(i - 1, 0)], costs[1] + dp[max(i - 7, 0)], costs[2] + dp[max(i - 30, 0)])
            else:
                dp[i] = dp[i - 1]
        
        return dp[n]