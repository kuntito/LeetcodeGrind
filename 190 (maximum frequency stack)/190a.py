# https://leetcode.com/problems/maximum-frequency-stack/description/

import heapq

# use a maxHeap, heapify after pushing an existing element
# heapify after popping
class FreqStack:
    def __init__(self):
        pass
        self.counter = {}
        self.maxHeap = []
        
    def push(self, val: int) -> None:
        pass
        
        counter, maxHeap = self.counter, self.maxHeap
        
        if val in counter:
            pass
            counter[val][0] -= 1
            heapq.heapify(maxHeap)
        else:
            pass
            counter[val] = [-1, val]
            heapq.heappush(maxHeap, counter[val])
        

    def pop(self) -> int:
        pass
        topMost = heapq.heappop(self.maxHeap)
        
        negFreq, val = topMost
        
        negFreq += 1
        if negFreq < 0:
            heapq.heappush(self.maxHeap, [negFreq, val])
            
        print(val)
        
        return val


sol = FreqStack()
sol.push(5)
sol.push(7)
sol.push(5)
sol.push(7)
sol.push(4)
sol.push(5)
sol.pop()
sol.pop()
sol.pop()
sol.pop()
