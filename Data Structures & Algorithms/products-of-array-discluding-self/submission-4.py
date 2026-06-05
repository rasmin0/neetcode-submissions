class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = [0] * len(nums)
        res = []

        pre.append(nums[0])

        for i in range(1, len(nums)):
            pre.append(nums[i] * pre[i - 1])
        
        post[-1] = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            post[i - 1] = post[i] * nums[i - 1]

        # nums = [1, 2, 4, 6]

        # pre = [1, 2, 8, 48]
        # post = [48, 48, 24, 6]

        res.append(post[1])
        for i in range(1, len(nums) - 1):
            res.append(pre[i - 1] * post[i + 1])
        res.append(pre[-2])

        return res
