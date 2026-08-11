class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
            # left half is sorted
            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = l + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1
        
        return False
