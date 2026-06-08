class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        res = ""
        for i in range(len(s)):
            l = i
            r = i + 1
            cur1 = ""
            cur2 = ""
            best = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            cur1 = s[l+1:r]
            
            if i >= 1 and len(s) >= 3:
                l = i - 1
                r = i + 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                cur2 = s[l+1:r]
            else:
                cur2 += s[i]
            
            if len(cur1) > len(cur2):
                best = cur1
            else:
                best = cur2

            if len(best) > len(res):
                res = best

        return res
            