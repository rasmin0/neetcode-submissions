# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs,0,len(pairs)-1)

    
    def mergeSortHelper(self, arr: List[Pair], s, e):
        if e-s+1 <= 1:
            return arr
        
        m = (s+e)//2

        self.mergeSortHelper(arr,s,m)
        self.mergeSortHelper(arr,m+1,e)

        self.merge(arr,s,m,e)

        return arr

    def merge(self,arr,s,m,e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]
        
        l = 0
        r = 0
        i = s

        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                arr[i] = L[l]
                l += 1
            else:
                arr[i] = R[r]
                r += 1
            i += 1
        
        while l < len(L):
            arr[i] = L[l]
            l += 1
            i += 1
        while r < len(R):
            arr[i] = R[r]
            r += 1
            i += 1
        


        

        
        
