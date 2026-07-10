class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngeMap = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            
            if stack:
                ngeMap[nums2[i]] = stack[-1]
            
            else:
                ngeMap[nums2[i]] = -1
            
            stack.append(nums2[i])
        
        # ngeMap = {4 : -1, 3 : 4, 2 : 3, 1 : 2}

        res = [0] * len(nums1)

        for i in range(len(nums1)):
            res[i] = ngeMap[nums1[i]]
        
        return res
            

