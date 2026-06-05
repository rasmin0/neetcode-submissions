class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        frq = set()        # track freq of characters

        l = 0
        r = 1
        frq.add(s[l])
        bestLen = 1

        while r < len(s):
            if s[r] not in frq:
                frq.add(s[r])
                r += 1
                bestLen = max(bestLen, len(frq))
            elif s[r] in frq:
                frq.remove(s[l])
                l += 1
        return bestLen


            
        