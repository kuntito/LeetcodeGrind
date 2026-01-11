# https://leetcode.com/problems/zigzag-iterator/description/

from typing import List


# what's the crack? we're given two integer lists
# `v1` and `v2`

# we want to implement a class with three methods
# the constructor that takes the two lists

# and the methods `next` and `hasNext`

# we want to `next` to alternatively pop and return the first element of either list
# say we have v1 = [1, 2] and v2 = [3, 4]
# if we call next, it should return `1`
# leaving the lists as v1 = [2] and v2 = [3, 4]

# if we call next again, it should pop and return the first element from `v2`
# it should return `2`
# leaving the lists as v1 = [2] and v2 = [4]

# this continues till one of the lists is empty
# in which case, we pop and return from the non-empty list till it becomes empty

# `hasNext` returns a boolean if there's still a character in either list


# how do i implement `next`?
# i need a way to alternate between lists.

# i'd use a variable, `curr`
# and swap accordingly

# TODO this works but the follow-up is "what if you're given `n` lists"
# for one, i'd reverse all the arrays

# i'd need a way to connect them in order
# i'd use a doubly linked list where the head connects to the tail

# each linked list node would represent each of the `n` lists
# and the updateCurr simply moves to the next value in the linked list

# to handle empty lists, after popping and returning
# i'd check if the list is empty
# if yes-

# technically, the updateCurr function should handle this
# first, determine what the next node is, preferably, assign a variable to it

# but before moving to the next node
# it should check if the current node has exhausted all it's values
# if yes, remove that node from the linkedlist and connect the neighbours

# the edgecase would be if we had a single node left
# in that case we don't need a next, we just need to check if the list contains values
# if it doesn't self.curr == None

# our hasNext function would return `self.curr`
# this would be truthy if in python

# and to address empty lists passed in the constructor
# our linkedlist will create nodes in the order which the lists were passed
# avoiding empty lists, self.curr would be initialized to the head of the node.

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        v1.reverse()
        v2.reverse()
        
        self.v1 = v1
        self.v2 = v2

        self.curr = self.v1 if self.v1 else self.v2

    def next(self) -> int:
        # the description doesn't say what happens if we call next and both lists are empty, i'd return None
        if not self.hasNext():
            return
        
        val = self.curr.pop()
        self.updateCurr()
        return val
        
    def updateCurr(self):
        if self.curr == self.v1:
            if self.v2:
                self.curr = self.v2
        elif self.v1: # if curr is `v2` and `v1` is valid, it should swap to `v1`
           self.curr = self.v1

    def hasNext(self) -> bool:
        return self.v1 or self.v2