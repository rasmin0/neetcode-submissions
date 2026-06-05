class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return None

        output = []
        product = 1
        zeroCnt = 0
        zeroProd = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCnt += 1
            else:
                zeroProd *= nums[i]
            product *= nums[i]
        
        if zeroCnt >= 2:
            return [0] * len(nums)

        
        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(zeroProd)
            else:
                output.append(product // nums[i])
        
        return output