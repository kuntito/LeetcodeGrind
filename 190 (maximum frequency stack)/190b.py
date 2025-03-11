# https://leetcode.com/problems/maximum-frequency-stack/description/

import heapq

# you need a max heap to store the most frequent element
# keep a global variable, `count`
# it is the unique id of each element in the store

# pop the topmost char from the max heap
# if there's a tie, pop all the items with that value
# track the one closest to `self.count`

# add the others back to the heap

# use a hashmap to map value to [count, id]

class FreqStack:
    def __init__(self):
        pass
        self.hashMap = {}
        self.maxHeap = []
        self.id = 0
        
    def push(self, val: int) -> None:
        pass
        # TODO, `id` in it's current form is not sufficient to track the element closest to the top
        # since i only set one new entry
        # if another element is added, it becomes the one at the top
        # you might have to change the heap entries to `[recencyIdx, val]`
        # then the hashmap stores the count of each val
        # but how do you efficiently get the most recent without heap?
        if val not in self.hashMap:
            newEntry = [0, self.id, val]
            self.id += 1
            
            self.hashMap[val] = newEntry
            heapq.heappush(self.maxHeap, newEntry)
            
        self.hashMap[val][0] -= 1
        
        
    def pop(self) -> int:
        heapq.heapify(self.maxHeap)
        
        topFreq = self.maxHeap[0][0]
        
        # find other items with similar frequencies
        mostRecentId = 0
        arr = []
        
        while self.maxHeap and self.maxHeap[0][0] == topFreq:
            item = heapq.heappop(self.maxHeap)
            arr.append(item)
            
            mostRecentId = max(
                mostRecentId,
                item[1]
            )
            
        val = None
        while arr:
            item = arr.pop()
            if item[1] == mostRecentId:
                val = item[2]
                self.hashMap[val][0] += 1
                # continue
            
            heapq.heappush(self.maxHeap, item)
            
        print(val)
        return val
            
        
            
    


# sol = FreqStack()
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

sol = FreqStack()
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

