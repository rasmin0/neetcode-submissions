class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for num in nums:
            if num in frq:
                frq[num] += 1
            else:
                frq[num] = 1
        print(frq)
        
        bucket = [[] for i in range(max(frq.values()) + 1)]

        for key, val in frq.items():
            bucket[val].append(key)
        print(frq)
        print(bucket)

        res = []

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                res += bucket[i]
            if len(res) == k:
                return res


