# Approach 1: Stack Implementation using Array
class Stack:
    def __init__(self, n: int):
        self.myStack = [0] * n
        self.stackSize = -1
        self.n = n

    def push(self, num: int):
        if self.stackSize != self.n - 1:
            self.stackSize += 1
            self.myStack[self.stackSize] = num

    def pop(self) -> int:
        if self.stackSize != -1:
            self.stackSize -= 1
            return self.myStack[self.stackSize + 1]
        else:
            return -1

    def top(self) -> int:
        if self.stackSize != -1:
            return self.myStack[self.stackSize]
        else:
            return -1

    def isEmpty(self) -> int:
        if self.stackSize != -1:
            return 0
        else:
            return 1

    def isFull(self) -> int:
        if self.stackSize != self.n - 1:
            return 0
        else:
            return 1
