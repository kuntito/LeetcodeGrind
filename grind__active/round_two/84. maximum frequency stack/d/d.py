# https://leetcode.com/problems/maximum-frequency-stack/

import heapq

class FreqStack:

    def __init__(self):
        self.recency = 0
        self.maxHeap = []
        self.hashMap = {}

    def push(self, val: int) -> None:
        if val in self.hashMap:
            # increase the frequency
            self.hashMap[val][0] += 1
        else:
            self.hashMap[val] = [1, self.recency]
            
            self.recency -= 1
            
        freq, recency = self.hashMap[val]
        
        heapq.heappush(
            self.maxHeap,
            (-1 * freq, recency, val)
        )
        

    def pop(self) -> int:
        _, _, elem = heapq.heappop(self.maxHeap)
        
        # reduce the frequency
        self.hashMap[elem][0] -= 1
        
        # if frequency is zero, del entry
        if self.hashMap[elem][0] == 0:
            del self.hashMap[elem]
            
        print(elem)
        return elem
    
sol = FreqStack()
# sol.push(5)
# sol.push(7)
# sol.push(5)
# sol.push(7)
# sol.push(4)
# sol.push(5)
# sol.pop()
# sol.pop()
# sol.pop()
# sol.pop()

# ANOTHER EXAMPLE
sol.push(1)
sol.push(0)
sol.push(0)
sol.push(1)
sol.push(5)
sol.push(4)
sol.push(1)
sol.push(5)
sol.push(1)
sol.push(6)
sol.pop()
sol.pop()
sol.pop()
sol.pop()
sol.pop()
sol.pop()
sol.pop()
sol.pop()
sol.pop()
sol.pop()