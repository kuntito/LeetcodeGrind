# https://leetcode.com/problems/min-stack/description/

# TODO deep this solution.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.min = val
        elif val < self.min:
            self.min = val
        self.stack.append(val)
        self.min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min = self.min_stack[-1] if self.min_stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min