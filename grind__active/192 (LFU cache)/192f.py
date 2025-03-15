# https://leetcode.com/problems/lfu-cache/description/

# for a start, we want to store key -> values
# a simple hashmap would take of this, let's call it `cache`

# whenever the cache is full, we want to remove the least recently used item among the least frequently used item
# in other words, we'd need to maintain some form of sorting based on frequency
# and a sub sorting based on recency

# the solution here is to create another hashmap
# that maps each unique frequency to the recency of items, whenever an item is accessed (get, put)
# the map would have a freq -> DoublyLinkedList

# going back to the first hashmap
# it should map key -> DoublyLinkedList Node

# this way we'd maintain a global variable of minFreq
# when we make room for new items, we simply access that linked list and remove the first node
# then delete the node from the `cache`

from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.freqMap = defaultdict(DLL)
        self.capacity = capacity
        
        self.minFreq = 0

    def put(self, key: int, value: int) -> None:
        
        # create the node
        # add it to the `cache`
        # add it to the frequency map
        # update minimum frequency, every time you add a new node, set it to `1`
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                self.removeLFU()
            node = Node(key=key, value=value)
            self.cache[key] = node
            self.minFreq = 1
            
        node = self.cache[key]
        node.value = value
        self.updateNodeFreq(node)

    def removeLFU(self):
        lfu = self.freqMap[self.minFreq].removeFirst()
        
        del self.cache[lfu.key]

    def updateNodeFreq(self, node):
        oldFreq = node.freq
                
        # connect node's neighbours
        # and strip node of it's prev and nex connections
        node.connectNeighbours()
        
        node.freq += 1
        newFreq = node.freq
        
        # add node to a new freq dll
        self.freqMap[newFreq].addLast(node)
        
        # if the old frequency was the minimum
        # since we removed that node from the DLL, it stopped being the minFreq
        # the new minFreq is the node.freq
        if oldFreq == self.minFreq and self.freqMap[oldFreq].isEmpty():
            self.minFreq = node.freq
        
        
    def get(self, key: int) -> int:
        res = -1
        if key in self.cache:
            node = self.cache[key]
            self.updateNodeFreq(node)
            
            res = node.value
        # print(res)
        return res




class Node:
    def __init__(self, key, value, freq=0, nex=None, prev=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.nex = nex
        self.prev = prev
        

    def connectNeighbours(self):
        beforeNei, nexNei = self.prev, self.nex
        
        self.prev = None
        self.nex = None
        
        if beforeNei:
            beforeNei.nex = nexNei
            
        if nexNei:
            nexNei.prev = beforeNei
            
    def __str__(self):
        values = []
        current = self
        while current:
            values.append(current.value)
            current = current.nex
        return str(values)
    
    def __repr__(self):
        return str(self)

class DLL:
    def __init__(self):
        self.left = Node(key="left", value=None)
        self.right = Node(key="right", value=None)
        
        # connect the two pointers
        self.left.nex, self.right.prev = self.right, self.left
        
    def isEmpty(self):
        return self.left.nex == self.right
        
        
    def addLast(self, node: Node):
        currLast = self.right.prev
        
        currLast.nex = node
        node.prev = currLast
        
        node.nex = self.right
        self.right.prev = node
    
    def removeFirst(self) -> Node:
        first = self.left.nex
        if first == self.right:
            return -1
        
        newFirst = first.nex
        
        self.left.nex = newFirst
        newFirst.prev = self.left
        
        first.nex = None
        first.prev = None
        
        return first



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
sol.get(2)
sol.put(2, 6)
sol.get(1)
sol.put(1, 5)
sol.put(1, 2)
sol.get(1)
sol.get(2)