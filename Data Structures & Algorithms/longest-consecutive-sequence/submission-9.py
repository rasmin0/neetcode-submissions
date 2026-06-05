class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set()

        startNums = []

        for num in nums:
            numSet.add(num)
        
        for num in numSet:
            if num - 1 not in numSet:
                startNums.append(num)
        print(numSet)
        print(startNums)

        bestLen = 1
        curLen = 1

        for i in range(len(startNums)):
            curNum = startNums[i]
            for num in numSet:
                if curNum + 1 in numSet:
                    curLen += 1
                    curNum += 1
                else:
                    break
            bestLen = max(bestLen, curLen)
            curLen = 1
        print(bestLen)

        return bestLen
