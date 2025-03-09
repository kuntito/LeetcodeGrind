# https://leetcode.com/problems/design-hashset/

class Node:
    def __init__(self, key: int=None, nei=None):
        pass
        self.val = key
        self.next = nei

# TODO finish this!
# https://neetcode.io/solutions/design-hashset
# 08:23
class MyHashSet:
    def __init__(self):
        pass
        # since we're expecting at most 1_000_000 values
        # we'd create most 1000 slots 
        # each key would be moded by 1000 to get the hashed key
        # each entry would be stored as a Node
        # and subsequent entries with the same key would be chained to the previous node
        self.thousand = 1000
        self.hashSet = [Node() for _ in range(self.thousand)]
        
    def add(self, key: int) -> None:
        hashedKey = key % self.thousand

        chain = self.hashSet[hashedKey]
        while chain and chain.next:
            if chain.key == key:
                return
            chain = chain.next
            
        chain.next = Node(key=key)
        
    def remove(self, key: int) -> None:
        hashedKey = key % self.thousand


    def contains(self, key: int) -> bool:
        pass