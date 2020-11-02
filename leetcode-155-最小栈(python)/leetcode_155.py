class MinStack:

    def __init__(self):
        self.stack = []
        self.assist = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.assist or x <= self.assist[-1]:
            self.assist.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.assist[-1]:
            self.assist.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.assist[-1]

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # --> 返回 -3.
    minStack.pop()
    print(minStack.top())     # --> 返回 0.
    print(minStack.getMin())
