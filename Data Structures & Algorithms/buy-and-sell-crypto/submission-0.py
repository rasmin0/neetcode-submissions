class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # track cur profit
        # track best profit -> update if cur profit better
        # track cur min
        # track best min -> update if cur min better

        bestMin = prices[0] 
        bestProfit = 0 

        for r in range(1, len(prices)):
            curProfit = prices[r] - bestMin 
            bestProfit = max(bestProfit, curProfit) 
            bestMin = min(bestMin, prices[r])
        
        return bestProfit


