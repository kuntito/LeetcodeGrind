# https://leetcode.com/problems/lfu-cache/description/

# use a hashmap to store key value pairs
# however, the value here is a custom LinkedList node

# the custom node is a doubly linked list node that holds
# previous and next references, it also holds the value

# whenever a node is accessed (get or put)
# it is moved to the start of the linked list
# that way the tail of the node is always the lru and lfu


class LFUCache:

    def __init__(self, capacity: int):
        pass
        self.slotsLeft = capacity
        self.head = Node("head")
        self.tail = Node("tail")
        
        self.head.nex, self.tail.prev = self.tail, self.head
        print(self.head)
        # print(self.tail.prev)
        self.hashMap = {}
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            node.value = value
            self.remove(node)
        else:
            if self.slotsLeft == 0:
                lru = self.tail.prev
                del self.hashMap[lru.key]
                self.remove(lru)
            else:
                self.slotsLeft -= 1
            
            node = Node(value, key)
            self.hashMap[key] = node
            
        self.placeAtHead(node)
        
        

    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            self.placeAtHead(node)
            return node.value
            
        return -1
    
    def remove(self, node):
        prev, nex = node.prev, node.nex
        
        prev.nex = nex
        nex.prev = prev
        
    def placeAtHead(self, node):
        prevStart = self.head.nex
        
        self.head.nex = node
        node.prev = self.head
        
        prevStart.prev = node
        node.nex = prevStart
        

class Node:
    def __init__(self, value, key=None, nex=None, prev=None):
        self.value = value
        self.key = key
        self.nex = nex
        self.prev = prev
        
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


sol = LFUCache(3)
sol.put(2, 2)
sol.put(1, 1)
sol.get(2)
sol.get(1)
sol.get(2)
sol.put(3, 3)
sol.put(4, 4)
sol.get(3)
sol.get(2)
sol.get(1)
sol.get(4)

