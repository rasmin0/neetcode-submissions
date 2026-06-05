class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        res = r

        while l <= r:
            rate = (l+r)//2
            hours = 0
            for b in piles:
                hours += math.ceil(b/rate)

            if hours <= h:
                r = rate - 1
                res = min(res,rate)
            else:
                l = rate + 1
            

        
        return res


        