class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for i in s:
            if i == '(':
                res.append(')')
            elif i == '[':
                res.append(']')
            elif i == '{':
                res.append('}')
            elif res and res[-1] == i:
                res.pop()
            else:
                return False

        return True if len(res) == 0 else False
        