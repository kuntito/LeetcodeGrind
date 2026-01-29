# https://leetcode.com/problems/min-stack/description/

# what are we doing?

# we want to implement a custom stack.
# it has the following operations:
#  push
#  pop
#  top
#  getMin

# push, means append to the stack
# pop, means remove and return the last added element
# top, means return the last added element
# getMin, means return the smallest element in the stack

# the values added would always be integers..
# the `push`, `pop` and `top` are all straightforward operations.
# the `getMin` is where things get crazy..

# it's easy to track the lowest number seen in the stack so far..
# so why not do that?
# use a min heap..

# so what happens when you pop an element from the stack..
# well, you check if that element is at the top of the min heap
# if it is..
# remove it as well

# and if it isn't.. store it somewhere..
# why?
# so we know to ignore it, if it's ever at the top of the min heap

# say your stack is [3, 2, 4]
# minHeap would be something like [2, 3, 4]

# if you pop from the stack, `4` moves out..
# but since `4` is not at the top of the min heap
# we can't exactly remove it from the min heap not without removing the others..

# so we keep it somewhere, so if we eventually pop from the min heap and see `4`
# we know to ignore it..

# wouldn't a set be better for storing the removed values
# a dictionary would be better since numbers can have duplicates

import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []
        self.toRemove = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minHeap, val)

    def pop(self) -> None:
        lastElem = self.stack.pop()
        
        if lastElem == self.minHeap[0]:
            heapq.heappop(self.minHeap)
        else:
            self.toRemove[lastElem] = self.toRemove.get(lastElem, 0) + 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # now we want to return the top element of the minHeap
        # unless that top element exists in `toRemove`
        
        # FIXME 
        # error, while checking if the topmost heap element is to be removed
        # i didn't actually remove the topmost heap element, i only updated
        # the `toRemove` dictionary..
        # i did.. 
        
        # while self.minHeap[0] in self.toRemove:
        #     topElem = self.minHeap[0]
        #     self.toRemove[topElem] -= 1
        
        # instead of 
        
        # while self.minHeap[0] in self.toRemove:
        #     topElem = heapq.heappop(self.minHeap)
        #     self.toRemove[topElem] -= 1
        
        while self.minHeap[0] in self.toRemove:
            topElem = heapq.heappop(self.minHeap)
            self.toRemove[topElem] -= 1
            
            if self.toRemove[topElem] == 0:
                del self.toRemove[topElem]
                
        return self.minHeap[0]
    
sol = MinStack()
sol.push(5)
sol.push(3)
sol.push(4)
sol.getMin()
sol.pop()
sol.pop()
sol.top()
sol.getMin()