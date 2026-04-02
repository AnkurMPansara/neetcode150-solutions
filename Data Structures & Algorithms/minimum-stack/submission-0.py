class MinStack:

    def __init__(self):
        self.stack = []
        self.minCounter = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minCounter and self.minCounter[-1] < val:
            self.minCounter.append(self.minCounter[-1])
        else:
            self.minCounter.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minCounter.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minCounter[-1]
