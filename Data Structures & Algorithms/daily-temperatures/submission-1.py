class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            else:
                res[i] = 0
            stack.append((temperatures[i], i))
        
        return res