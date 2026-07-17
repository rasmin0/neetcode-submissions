class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        h = len(nums) - 1
        while l <= h:
            m = (l + h) // 2

            if nums[m] < target:
                l = m + 1
            else:
                h = m
            if l == m == h:
                break
        l1 = l
        if l1 >= len(nums) or nums[l1] != target:
            return [-1, -1]

        h = len(nums) - 1
        right = -1
        
        while l <= h:
            m = (l + h) // 2

            if nums[m] <= target:
                if nums[m] == target:
                    right = m
                l = m + 1
            else:
                h = m - 1
            
        if nums[l1] == target and nums[right] == target:
            return [l1, right]
        else:
            return[-1, -1]