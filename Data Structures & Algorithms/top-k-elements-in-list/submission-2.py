class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums:
            if num not in frq:
                frq[num] = 1
            else:
                frq[num] += 1
        
        arr = [[] for i in range(max(frq.values()) + 1)]

        for key, val in frq.items():
            arr[val].append(key)
        
        res = []
        for i in range(len(arr) - 1, - 1, -1):
            res += arr[i]
            if len(res) == k:
                return res