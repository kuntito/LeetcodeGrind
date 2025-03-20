# https://leetcode.com/problems/maximum-frequency-stack/

import heapq
# the idea is to have a frequency map
# the pairing is `freq -> list of items in the stack`

# a maxHeap to store unique frequencies

# a hashmap that stores `val -> freq`
# when you add an item, if it's new
# create it's frequency list
# create it's hashmap value

# append the value to the frequency list
class FreqStack:
    def __init__(self):
        # map each value to it's frequency
        self.valFreqMap = {}
        # create a frequency stack
        self.freqListMap = {}
        self.maxHeap = []

    def push(self, val: int) -> None:
        self.valFreqMap[val] = self.valFreqMap.get(val, 0) + 1
        
        self.updateFreq(val)
        
    def updateFreq(self, val):
        # create a freq list if it doesn't exist
        # append val
        
        
        freq = self.valFreqMap[val]
        if freq not in self.freqListMap:
            self.freqListMap[freq] = []
            heapq.heappush(self.maxHeap, -1 * freq)
            
        lst = self.freqListMap[freq]
        lst.append(val)

    def pop(self) -> int:
        pass
        topFreq = -1 * self.maxHeap[0]
        
        lst = self.freqListMap[topFreq]
        mostFreqValue = lst.pop()
        
        self.valFreqMap[mostFreqValue] -= 1
        
        if not lst:
            del self.freqListMap[topFreq]
            heapq.heappop(self.maxHeap)
            
        # print(mostFreqValue)
        return mostFreqValue
        

        
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