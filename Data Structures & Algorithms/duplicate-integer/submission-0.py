class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}

        for num in nums:
            if num in myMap:
                myMap[num] += 1
            else:
                myMap[num] = 1
        
        for vals in myMap.values():
            if vals > 1:
                return True
        
        return False
