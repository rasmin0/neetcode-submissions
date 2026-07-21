class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r = (m + n) - 1
        m1 = m - 1
        n1 = n - 1

        while m1 >= 0 and n1 >= 0:
            if nums1[m1] >= nums2[n1]:
                nums1[r] = nums1[m1]
                r -= 1
                m1 -= 1
            else:
                nums1[r] = nums2[n1]
                r -= 1
                n1 -= 1

        if n1 >= 0:
            while n1 >= 0:
                nums1[r] = nums2[n1]
                r -= 1
                n1 -= 1

