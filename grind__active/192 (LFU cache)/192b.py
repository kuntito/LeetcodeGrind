# https://leetcode.com/problems/lfu-cache/description/

# use a hashmap and a list
# the hashmap stores values (key => [accessNum, Value])
# use a minHeap to store each [accessNum, value]

# set a global variable for access value
# update each node item whenever added or get
# when you need to remove the least frequently used
# heapify the min heap
# remove the top
# update the hashmap
import heapq

class LFUCache:
    def __init__(self, capacity: int):
        pass
        self.hashmap = {}
        self.accessNum = 1
        self.minHeap = []

        self.currCap = 0
        self.maxCap = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        item = self.hashmap[key]
        item[0] = self.accessNum
        
        self.accessNum += 1

        return item[1]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            item = self.hashmap[key]
            item[0] = self.accessNum
            item[1] = value
        else:
            if self.currCap < self.maxCap:
                self.currCap += 1
            else:
                self.removeLeast()
            
            item = [self.accessNum, value, key]
            self.hashmap[key] = item
            self.minHeap.append(item)
            
        
        self.accessNum += 1


    def removeLeast(self):
        heapq.heapify(self.minHeap)
        leastUsed = heapq.heappop(self.minHeap)
        
        key = leastUsed[2]
        del self.hashmap[key]