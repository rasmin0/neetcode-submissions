class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')
            
            if s[i] == ')':
                if stack and stack[-1] == ')':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack and stack[-1] == ']':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack and stack[-1] == '}':
                    stack.pop()
                else:
                    return False
        
        return not stack