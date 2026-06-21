class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [0] * (days[-1] + 1)
        sDays = set(days)

        for i in range(1, days[-1] + 1):
            if i in sDays:
                dp[i] = min(costs[0] + dp[max(0, i - 1)], costs[1] + dp[max(0, i - 7)], costs[2] + dp[max(0, i - 30)])
            else:
                dp[i] = dp[i - 1]
        
        return dp[days[-1]]