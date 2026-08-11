class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # left half is sorted
            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            # right half is sorted
            else:
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1
        
        return -1
            