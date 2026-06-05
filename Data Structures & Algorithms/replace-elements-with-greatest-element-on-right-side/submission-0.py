class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)

        for i in range(len(arr)):
            if i != len(arr) - 1:
                res[i] = max(arr[(i+1):])
            else:
                res[-1] = -1
        return res
