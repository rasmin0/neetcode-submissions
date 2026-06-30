class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == '+' or s == '*' or s == '-' or s == '/':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if s == '+':
                    stack.append(num1 + num2)
                elif s == '*':
                    stack.append(num1 * num2)
                elif s == '-':
                    stack.append(num1 - num2)
                else:
                    stack.append(num1 / num2)
            else:
                stack.append(s)

        return int(stack[-1])