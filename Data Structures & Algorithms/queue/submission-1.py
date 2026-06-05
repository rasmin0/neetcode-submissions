class Deque:
    
    def __init__(self):
        self.stack = []
        self.size = 0

    def isEmpty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False

    def append(self, value: int) -> None:
        self.stack.append(value)
        self.size += 1

    def appendleft(self, value: int) -> None:
        self.stack.insert(0, value)
        self.size += 1

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            num = self.stack[-1]
            del self.stack[-1]
            self.size -= 1
            return num

    def popleft(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            numb = self.stack[0]
            del self.stack[0]
            self.size -= 1
            return numb