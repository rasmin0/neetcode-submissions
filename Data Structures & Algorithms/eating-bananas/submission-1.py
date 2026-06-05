class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        res = r

        while l <= r:
            rate = (l+r)//2
            print("rate: ", rate)
            hours = 0
            for b in piles:
                hours += math.ceil(b/rate)
            print("hours: ", hours)

            if hours <= h:
                r = rate - 1
                print("res before update: ", res)
                print("rate before update :", rate)
                res = min(res,rate)
            else:
                l = rate + 1
            
            print("res after update: ",res )

        
        return res


        