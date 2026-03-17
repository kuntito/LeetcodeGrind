# https://leetcode.com/problems/lfu-cache/

import heapq

# TODO don't rush to write, figure out why it fails this test case
# then fix.

# ["LFUCache","put","put","get","get","put","get","get","get"]
# [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]

# my output
# [null,null,null,2,1,null,-1,2,3]

# correct output
# [null,null,null,2,1,null,1,-1,3]

class LFUCache:
    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.keyValueMap = {}
        self.frequencyMap = {}
        self.recencyMap = {}
        self.minHeap = []
        
        self.recency = 0

    def get(self, key: int) -> int:
        if key in self.keyValueMap:
            self.updateMetrics(key)
            return self.keyValueMap[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        isNewKey = key not in self.keyValueMap
        isCapacityFull = len(self.keyValueMap) == self.maxCapacity
        if isNewKey and isCapacityFull:
            self.removeLeast()
            
        self.keyValueMap[key] = value
        self.updateMetrics(key)
        
        
    def updateMetrics(self, key):
        self.frequencyMap[key] = self.frequencyMap.get(key, 0) + 1
        self.recencyMap[key] = self.recencyMap.get(key, self.recency) + 1
        
        self.recency += 1
        
        freq = self.frequencyMap[key]
        recency = self.recencyMap[key]
        
        heapItem = (freq, recency, key)
        
        heapq.heappush(
            self.minHeap,
            heapItem
        )
        
    def removeLeast(self):
        # the heap top values has to match the state in the maps for it to be valid
        freq, recency, key = heapq.heappop(self.minHeap)
        if key in self.keyValueMap and self.frequencyMap[key] == freq and self.recencyMap[key] == recency:
            del self.frequencyMap[key]
            del self.recencyMap[key]
            del self.keyValueMap[key]
        else:
            self.removeLeast()


sol = LFUCache(2)
sol.get(2)
sol.put(2, 6)
sol.get(1)
sol.put(1, 5)
sol.put(1, 2)
sol.get(1)
print(sol.get(2))