class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m
            else:
                return nums[l]

