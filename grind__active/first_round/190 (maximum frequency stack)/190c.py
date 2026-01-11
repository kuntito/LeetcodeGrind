# https://leetcode.com/problems/maximum-frequency-stack/

import heapq
class FreqStack:
    def __init__(self):
        pass
        
        # use a hashmap of frequencies
        # each pairing is 
        # freq -> dll
        self.freqMap = {}
        
        # each linked list node
        # has val, freq
        
        # use a hashmap to map the val -> node
        self.seenMap = {}
        
        # use a maxheap to store the unique frequencies
        self.maxHeap = []
        
        
    def push(self, val: int) -> None:
        if val not in self.seenMap:
            node = DLNode(val)
            self.seenMap[val] = node
            
        node = self.seenMap[val]
        node.freq += 1
        self.updateFreq(node)
        
    def updateFreq(self, node):
        # you want to remove the node from it's frequency dll
        node.connectNeighbours()
        
        # update the new node frequency and add it to it's respective dll        
        newFreq = node.freq
        
        if newFreq not in self.freqMap:
            self.freqMap[newFreq] = DLL()
            heapq.heappush(self.maxHeap, -newFreq)
            
        dll = self.freqMap[newFreq]
        dll.addLast(node)

    def pop(self) -> int:
        pass
        # grab the mostFrequent value
        mostFreqVal = -1 * self.maxHeap[0]
        
        
        # grab it's dll from the `freqMap`
        dll = self.freqMap[mostFreqVal]
        
        # the dlnode before dll.tail is the one on top
        # remove it
        mostFreqNode = dll.tail.prev
        mostFreqNode.connectNeighbours()
               
        res = mostFreqNode.val

        # if the dll is empty
        # remove it's frequency from the maxHeap
        if dll.isEmpty():
            heapq.heappop(self.maxHeap)
            del self.freqMap[mostFreqVal]
        
        # you should decrease the node's frequency
        # if it's greater than zero, add it to a different dll
        mostFreqNode.freq -= 1
        if mostFreqNode.freq > 0:
            self.updateFreq(mostFreqNode)
        
        print(res)
        return res
        

class DLL:
    def __init__(self):
        self.head = DLNode("head")
        self.tail = DLNode("tail")
        
        self.head.nex = self.tail
        self.tail.prev = self.head
        
    def addLast(self, node):
        prevLast = self.tail.prev
        
        prevLast.nex = node
        node.prev = prevLast
        
        node.nex = self.tail
        self.tail.prev = node
        
    def isEmpty(self):
        return self.head.nex == self.tail
    
    
class DLNode:
    def __init__(self, val, freq=0, nex=None, prev=None):
        self.val = val
        self.freq = freq
        self.nex = nex
        self.prev = prev
        
    def connectNeighbours(self):
        before, after = self.prev, self.nex
        
        if before:
            before.nex = after
            
        if after:
            after.prev = before
            
        self.prev, self.nex = None, None
        
sol = FreqStack()
sol.push(5)
sol.push(7)
sol.push(5)
sol.push(7)
sol.push(4)
sol.push(5)
sol.pop()
sol.pop()
sol.pop()
sol.pop()