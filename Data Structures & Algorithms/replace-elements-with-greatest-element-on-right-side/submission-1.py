class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)

        res[-1] = -1

        curMax = 0

        for i in range(len(arr) - 1, 0 , -1):
            curMax = max(res[i], arr[i])
            res[i - 1] = curMax
        
        return res


        
