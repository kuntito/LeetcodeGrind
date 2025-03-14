# https://leetcode.com/problems/lfu-cache/description/

# it's a hashmap with max capacity
# once full, the hashmap makes room by removing the least frequently used item
# if multiple items have the same least frequency, remove the one that's least recently used

# in other words, use an actual hashmap to store the items
# a global variable for capacity
# a global variable for recency, once a value is used update it's recency

# use a heap to store items
# each item is list of [frequency, recency, key]
# the heap remains dormant and is only heapified when the cache wants to make room

import heapq

class LFUCache:
    def __init__(self, capacity: int):
        pass
        self.slotsLeft = capacity
        self.recency = 0
        self.hashMap = {}
        
        self.minHeap = []
        

    def get(self, key: int) -> int:
        res = -1
        if key in self.hashMap:                
            item = self.hashMap[key]
            res = item[3]
            
            # updating frequency
            item[0] += 1
            
            # updating recency
            item[1] = self.recency
            self.recency += 1
            
        print(res)
        return res

    def put(self, key: int, value: int) -> None:

        if key not in self.hashMap:
            if self.slotsLeft == 0:
                # remove LFU or LRU
                self.removeItem()
            else:
                self.slotsLeft -= 1
            item = [0, 0, key, value]
            self.hashMap[key] = item
            heapq.heappush(self.minHeap, item)
        
        # updating the frequency
        self.hashMap[key][0] += 1
        # updating the recency
        self.hashMap[key][1] += self.recency
        self.hashMap[key][3] = value
        
        self.recency += 1

    def removeItem(self):
        heapq.heapify(self.minHeap)
        
        leastFreq = self.minHeap[0][0]
        leastRecent = self.recency
        
        arr = []
        while self.minHeap and self.minHeap[0][0] == leastFreq:
            item = heapq.heappop(self.minHeap)
            leastRecent = min(
                item[1],
                leastRecent
            )
            arr.append(item)

        while arr:
            item = arr.pop()
            if item[1] == leastRecent:
                key = item[2]
                del self.hashMap[key]
                continue
            
            heapq.heappush(self.minHeap, item)
            
        


# sol = LFUCache(2)
# sol.put(1, 1)
# sol.put(2, 2)
# sol.get(1)
# sol.put(3, 3)
# sol.get(2)
# sol.get(3)
# sol.put(4, 4)
# sol.get(1)
# sol.get(3)
# sol.get(4)

sol = LFUCache(2)
sol.put(3, 1)
sol.put(2, 1)
sol.put(2, 2)
sol.put(4, 4)
sol.get(2)
