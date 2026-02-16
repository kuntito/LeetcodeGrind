# https://leetcode.com/problems/maximum-frequency-stack/

# i want to design a stack that stores integers
# based on frequency and recency.

# the stack has two operations, `push` and `pop`

# `push` adds elements to the stack
# `pop` removes elements from the stack.

# `pop` returns the most frequent element.
# if there's a tie for most frequent element.

# `pop` returns the most recent of those elements.

# knowing the most frequent, most recent element is easy.
# the challenge is once you pop this element.

# how do you get the new most frequent, most recent element.
# can a heap help here?

# a heap based on max frequency?
# each heap node would be (negativeFrequency, recency, number)

# `negativeFrequency` because Python only has min heap.
#  a frequency of -4 would precede a frequency of -2 in a min heap

# i think this solves it.
# and if you add a new number, just add to the heap.

# use a dictionary to track frequency.

# to handle the recency, Python already sorts by the second element
# whenever the heap item is a collection of more than one element
# and the first elements match

# so would i have to negative frequency too?
# i could or just decrement it from the jump
# initialize frequency to `0` then decrement..

# error, i tried to decrement frequency from the heap, `freqHeap`
# instead of `freqMap`

# i'd blame the similarity in naming.., `freqHeap` and `freqMap`
# i changed `freqMap` to `counter`

# this works, however Navdeep has an even cleaner solution O(1)
# see `c.py`
import heapq
class FreqStack:

    def __init__(self):
        self.counter = {}
        self.recency = 0
        self.freqHeap = []

    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1
        elemFreq = self.counter[val]
        
        heapItem = (
            -1 * elemFreq,
            self.recency,
            val
        )
        heapq.heappush(self.freqHeap, heapItem)
        
        self.recency -= 1


    def pop(self) -> int:
        # what we doing here?
        # remove the topmost heap item
        # update the frequency map
        
        topItem = heapq.heappop(self.freqHeap)
        
        negFrequency, recency, val = topItem
        
        # reduce the frequncy from the map
        self.counter[val] -= 1
        
        # `recency` doesn't do anything when popped
        # neither does `negFrequency`
        
        return val

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