class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            days = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    days += 1
                else:
                    res[i] = days
                    break
        
        return res