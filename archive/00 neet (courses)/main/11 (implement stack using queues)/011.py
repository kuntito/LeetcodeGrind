# https://leetcode.com/problems/implement-stack-using-queues/description/
from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
        self.second_queue = deque()

        self.current = self.queue

    def push(self, x: int) -> None:
        self.current.append(x)

    def pop(self) -> int:
        while len(self.current) > 1:
            item = self.current.popleft()
            if self.current == self.queue:
                self.second_queue.append(item)
            else:
                self.queue.append(item)

        res = self.current.popleft()
        self.current = self.queue if self.current == self.second_queue else self.second_queue
        return res

    def top(self) -> int:
        return self.current[-1]

    def empty(self) -> bool:
        return len(self.current) == 0


class MyStackII:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        count = len(self.queue)
        for _ in range(count-1):
            self.queue.append(self.queue.popleft())
        
        return self.queue.popleft()
    
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
    

stack = MyStackII()
res = stack.empty()
print(res)