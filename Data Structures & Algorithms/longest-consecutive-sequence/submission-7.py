class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set()

        for i in range(len(nums)):
            numSet.add(nums[i])
        
        arr = []

        for num in numSet:
            arr.append(num)


        arr1 = sorted(arr)

        print("arr 1: ", arr1)

        maxLen = 1
        lastNum = arr1[0]
        bestLen = 1
        maxArr = []
        for i in range(len(arr1) - 1):
            if arr1[i + 1] == arr1[i] + 1 or arr1[i + 1] == lastNum + 1:
                maxLen += 1
                lastNum = arr1[i]
                maxArr.append(maxLen)
            else:
                maxLen = 1

        print("maxArr: ", maxArr)

        if maxArr:
            return max(maxArr)
        else:
            return 1
        
        # numSet = set()

        # for i in range(len(nums)):
        #     numSet.add(nums[i])
        
        # print(numSet)

        # arr = []

        # for num in numSet:
        #     if num - 1 in numSet:
        #         arr.append(num - 1)
        # print(arr)
        # return len(arr)