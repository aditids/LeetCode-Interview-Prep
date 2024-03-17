# 155. Min Stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = inf

    def push(self, val: int) -> None:
        if val<=self.min:
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        #print(self.stack)
        k = self.stack.pop()
        if k==self.min:
            self.min = min(self.stack)
            self.min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()