# https://leetcode.com/problems/lfu-cache/description/


# TODO add doubly linked list to thingy
class DoublyListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
    def __str__(self):
        values = []
        current = self
        while current:
            values.append(current.val)
            current = current.next
        return str(values)
    
    def __repr__(self):
        return str(self)


# use a hashmap to store use frequency for each key
# each key should point to a node in a doubly linked list

# use a doubly linked list to store usage recency
# such that the most recent node is always moved to the front of the linked list 

# update the frequency each time get or put is called
# and update the tail of the linked list, this serves as the least recently used item
class LFUCache:
    def __init__(self, capacity: int):
        pass
        self.capacity = capacity
        self.counter = {}
        
        self.root = DoublyListNode()
        self.head = self.root
        self.tail = self.root
        

    def get(self, key: int) -> int:
        if key not in self.counter:
            return -1
        
        node_freq = self.counter[0]
        node_freq[1] += 1
        
        node = node_freq[0]
        self.place_in_front(node)
        return node.val

        
    def put(self, key: int, value: int) -> None:
        if key not in self.counter:
            self.counter[key] = [DoublyListNode(value), 0]
            
        if len(self.counter) == self.capacity:
            self.remove_last()
            
        node_freq = self.counter[key]
        node_freq[1] += 1
        
        self.place_in_front(node_freq[0])

    def remove_from_list(self, node):
        pass
        previous = node.prev
        after = node.next
        
        if previous:
            previous.next = after
        if after:
            after.previous = previous

    def place_in_front(self, node):
        self.remove_from_list(node)
        
        afterFirst = self.root.next
        
        self.root.next = node
        node.prev = self.root
        
        if afterFirst:
            afterFirst.previous = node
        

