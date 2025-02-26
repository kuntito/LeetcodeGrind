# https://leetcode.com/problems/design-circular-queue/description/

# TODO review 180a.py, deep the last wrong submission
# TODO https://neetcode.io/solutions/design-circular-queue
class MyCircularQueue:

    def __init__(self, k: int):
        pass
        # `queue` is a list of size `k`
        self.dim = k
        self.queue = [None for _ in range(self.dim)]
        self.start = 0
        self.end = -1
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.end += 1
        actual_idx = self.end % self.dim
        self.queue[actual_idx] = value
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.start += 1
        
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        
        actualIdx = self.start % self.dim
        return self.queue[actualIdx]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        
        actualIdx = self.end % self.dim
        return self.queue[actualIdx]

    def isEmpty(self) -> bool:
        return self.start > self.end

    def isFull(self) -> bool:
        dist = (self.end - self.start) + 1
        return dist == self.dim


sol = MyCircularQueue(3)
print(sol.enQueue(1))
print(sol.enQueue(2))
print(sol.enQueue(3))
print(sol.enQueue(4))
print(sol.Rear())
print(sol.isFull())
print(sol.deQueue())
print(sol.enQueue(4))
print(sol.Rear())
# print(sol.queue)
