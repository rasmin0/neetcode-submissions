class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i in range(len(nums)):
            if nums[i] not in myMap:
                myMap[target - nums[i]] = i
            else:
                return [myMap[nums[i]], i]
