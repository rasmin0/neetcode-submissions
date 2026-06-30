class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
                self.stack.append(val)
            else:
                self.stack.append(val)
        else:
            self.minStack.append(val)
            self.stack.append(val)

    def pop(self) -> None:
        if self.stack and self.minStack:
            if self.stack[-1] == self.minStack[-1]:
                self.stack.pop()
                self.minStack.pop()
            else:
                self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

