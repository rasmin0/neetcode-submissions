class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # s = "(])"
        # stack = ')' 
        for p in s:
            if p == '(' or p == '{' or p == '[':
                if p == '(':
                    stack.append(')')
                elif p == '{':
                    stack.append('}')
                else:
                    stack.append(']')
            else:
                if stack:
                    if p == ')' and stack[-1] == ')':
                        stack.pop()
                    elif p == '}' and stack[-1] == '}':
                        stack.pop()
                    elif p == ']' and stack[-1] == ']':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if stack:
            return False
        else:
            return True