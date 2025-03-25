class Node:
    def __init__(self, val, nex=None, prev=None):
        self.val = val
        self.nex = nex
        self.prev = prev
        
    def connectNeighbours(self):
        before, after = self.prev, self.nex
        
        if before:
            before.nex = after
            
        if after:
            after.prev = before
            
        self.nex, self.prev = None, None
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'({self.val})'
    
class DLL:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
        
        self.head.nex = self.tail
        self.tail.prev = self.head
        
    def addLast(self, val):
        node = Node(val)
        
        currLast = self.tail.prev
        
        currLast.nex = node
        node.prev = currLast
        
        node.nex = self.tail
        self.tail.prev = node
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        comma = ','
        
        arr = []
        tmp = self.head.nex
        
        while tmp != self.tail:
            arr.append(str(tmp))
            tmp = tmp.nex
            
        return '[' + comma.join(arr) + ']'