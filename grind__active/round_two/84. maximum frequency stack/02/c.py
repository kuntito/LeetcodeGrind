# https://leetcode.com/problems/maximum-frequency-stack/

# i want to design a stack that stores integers
# based on frequency and recency.

# the stack has two operations, `push` and `pop`

# `push` adds elements to the stack
# `pop` removes elements from the stack.

# `pop` returns the most frequent element.
# if there's a tie for most frequent element.

# `pop` returns the most recent of those elements.

# the trick here, shout of Navdeep..
# is to have a stack for each frequency..

# when you push an element, you find out what it's frequency should be
# a hash map comes in handy here..

# once, you have that..
# you simply append that element to the appropriate stack.

# every frequency has it's own stack.
# 1: [], 2: [], 3:[]

# this naturally handles the most frequent element and most recent
# it would always be the last element in the last stack

# okay, but how do you store these frequncy stacks..
# you could put them all in another stack..

# i.e. [[], []]

# the parent stack has frequency stacks for `freq 1` and `freq 2`
# this way each frequency can be accessed by index
# freq 1 is index 0
# freq 2 is index 1

# a hash map helps store the frequencies.. so this checks out..

# error, i used `add` to push an element to a stack
# the correct method is append..

# error, when popping, the last stack isn't always where the result lies.
# it is, at first..
# but check it

# [[1], [2]]..

# when you pop from this, you'd get `2`..
# the parent stack becomes..
# [[1], []]..

# currently i use.. `self.parentStack[-1].pop()`
# this would fail for the current scenario..

# what if we pop empty stacks
# the moment you removed `2` and realized the stack was empty
# remove the stack from parentStack

# what if you had a new element with frequency `3`
# well, that element would need an entry in freq 1, freq 2 first..
# and so the `push` method originally handles this..

# TODO it don't work, figure it out.

import heapq
class FreqStack:

    def __init__(self):
        self.parentStack = []
        self.counter = {}

    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1

        freq = self.counter[val]
        # now we need to know if we add a new stack to `parentStack`
        # or find existing stack.
        
        # what's the giveaway? if freq > len(parentStack)
        # we need to add a new one.
        
        if freq > len(self.parentStack):
            self.parentStack.append([])
            
        relevantStack = self.parentStack[freq - 1]
        relevantStack.append(val)

    def pop(self) -> int:
        lastStack = self.parentStack[-1]
        res = lastStack.pop()
        
        if not lastStack:
            self.parentStack.pop()
            
        return res


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