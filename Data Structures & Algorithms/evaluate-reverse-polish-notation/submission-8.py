class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(tokens[i])
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(num1 + num2)
                elif tokens[i] == '-':
                    stack.append(num1 - num2)
                elif tokens[i] == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 / num2)
        
        return int(stack[-1])
            
                