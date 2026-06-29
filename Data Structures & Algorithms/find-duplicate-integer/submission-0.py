class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        print(freq)
        for key, val in freq.items():
            if val > 1:
                return key