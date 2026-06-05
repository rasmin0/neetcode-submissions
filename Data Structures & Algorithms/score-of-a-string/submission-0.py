class Solution:
    def scoreOfString(self, s: str) -> int:
        sSum = 0

        for i in range(len(s) - 1):
            sSum += abs(ord(s[i]) - ord(s[i + 1]))
        
        return sSum