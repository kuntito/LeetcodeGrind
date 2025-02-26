# https://leetcode.com/problems/design-circular-queue/description/

# 
class MyCircularQueue:

    def __init__(self, k: int):
        pass
        self.dim = k
        self.queue = [None for _ in range(k)]
        self.size = 0
        self.startIdx = 0
        self.endIdx = -1

    def enQueue(self, value: int) -> bool:
        pass
        if self.size == self.dim:
            return False
    
        self.endIdx += 1
        insertIdx = self.endIdx % self.dim
        self.queue[insertIdx] = value

        self.size += 1
        
        return True
        

    def deQueue(self) -> bool:
        pass
        if self.size == 0:
            return False
        
        self.startIdx += 1
        self.size -= 1
        
        return True

    def Front(self) -> int:
        pass
        if self.size == 0: return -1
        
        idx = self.startIdx % self.dim
        return self.queue[idx]

    def Rear(self) -> int:
        if self.size == 0: return -1
        
        idx = self.endIdx % self.dim
        return self.queue[idx]


    def isEmpty(self) -> bool:
        return self.size > 0

    def isFull(self) -> bool:
        return self.size == self.dim

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
