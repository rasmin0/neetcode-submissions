class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        
        m = 0
        resL = 0
        resR = 0

        while m < len(s):
            l, r = m, m

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if (r - l) + 1 > (resR - resL) + 1:
                        resL = l
                        resR = r
                    l -= 1
                    r += 1
                else:
                    break
            
            l1 = m
            r1 = m + 1

            while l1 >= 0 and r1 < len(s):
                if s[l1] == s[r1]:
                    if (r1 - l1) + 1 > (resR - resL) + 1:
                        resL = l1
                        resR = r1
                    l1 -= 1
                    r1 += 1
                else:
                    break
            m += 1
        
        return s[resL:resR + 1]
        