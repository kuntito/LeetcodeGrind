# https://leetcode.com/problems/lfu-cache/description/

# the idea is to use a hash map to track items
# the value for the hashmap is a linked list node

# the node stores the value, freq, key, prev and next

# we're going to need a heap to store nodes based on frequency
# when we want to make room, we heapify the node based on frequency
# get all the nodes with the same least frequency and remove the one
# closest to the tail of the linked list

# https://neetcode.io/solutions/lfu-cache
# 08:42

# TODO read LC editorial
import heapq

class LFUCache:

    def __init__(self, capacity: int):
        pass
        self.slotsLeft = capacity
        self.hashMap = {}
        self.minHeap = []
        
        self.left = Node("left")
        self.right = Node("right")
        
        # connect the pointer nodes
        # all other nodes go in between them
        self.left.nex, self.right.prev = self.right, self.left
        
    def get(self, key: int) -> int:
        res = -1
        if key in self.hashMap:
            node = self.hashMap[key]
            # update it's frequency
            node.freq += 1
            
            # update it's recency
            self.remove(node)
            self.placeAtHead(node)
            
            res = node.value
    
        print(res)
        return res

    def put(self, key: int, value: int) -> None:
        if key not in self.hashMap:
            if self.slotsLeft == 0:
                self.removeLFU()
            else:
                self.slotsLeft -= 1
            
            node = Node(
                value=value,
                key=key,
                freq=0
            )
            self.hashMap[key] = node
            heapq.heappush(self.minHeap, node)
            
        node = self.hashMap[key]
        # update frequency
        node.freq += 1
        node.value = value
        # TODO how did LRU treat removing new nodes
        # update recency
        self.remove(node)
        self.placeAtHead(node)
        
    def remove(self, node):
        if node.prev and node.nex:
            before = node.prev
            after = node.nex
            
            before.nex = after
            after.prev = before
    

    def placeAtHead(self, node):
        prevHead = self.left.nex
        
        self.left.nex = node
        node.prev = self.left
        
        node.nex = prevHead
        prevHead.prev = node
        
    def removeLFU(self):
        #determine the least frequency
        heapq.heapify(self.minHeap)
        
        leastFreq = self.minHeap[0].freq
        
        candidates = set()
        while self.minHeap and self.minHeap[0].freq == leastFreq:
            node = heapq.heappop(self.minHeap)
            candidates.add(node)
            
        # iterate from the tail backwards
        tail = self.right
        while tail:
            if tail in candidates:
                res = tail
                break
            
            tail = tail.prev
        
        # put nodes back in the heap
        for node in candidates:
            if node == res:
                del self.hashMap[node.key]
                continue
            
            heapq.heappush(self.minHeap, node)
            

class Node:
    def __init__(self, value, key=None, freq=0, nex=None, prev=None):
        self.value = value
        self.freq = value
        self.key = key
        self.nex = nex
        self.prev = prev
        self.freq = freq
        
    # def __str__(self):
    #     return f'({self.value})'
    
    # def __repr__(self):
    #     return str(self)
    
    def __str__(self):
        values = []
        current = self
        while current:
            values.append(current.key)
            current = current.nex
        return str(values)
    
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.freq < other.freq


sol = LFUCache(2)
sol.put(1, 1)
sol.put(2, 2)
sol.get(1)
sol.put(3, 3)
sol.get(2)
sol.get(3)
sol.put(4, 4)
sol.get(1)
sol.get(3)
sol.get(4)