class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        
        m = 0
        res = ""

        while m < len(s):
            l, r = m, m

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if len(s[l:r+1]) > len(res):
                        res = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
            
            l1 = m
            r1 = m + 1

            while l1 >= 0 and r1 < len(s):
                if s[l1] == s[r1]:
                    if len(s[l1:r1+1]) > len(res):
                        res = s[l1:r1+1]
                    l1 -= 1
                    r1 += 1
                else:
                    break
            m += 1
        
        return res
        