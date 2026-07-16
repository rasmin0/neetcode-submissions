class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            if nums[m] > nums[h] and target <= nums[h]:
                l = m + 1
            elif nums[m] > nums[h] and target > nums[m]:
                l = m + 1
            elif nums[m] > target and target >= nums[l]:
                h = m - 1
            elif nums[m] < target and target <= nums[h]:
                l = m + 1
            elif nums[m] < nums[l] and target >= nums[l]:
                h = m - 1
            elif nums[m] < nums[l] and target < nums[m]:
                h = m - 1
            else:
                return -1
