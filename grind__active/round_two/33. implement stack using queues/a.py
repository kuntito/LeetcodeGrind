# https://leetcode.com/problems/implement-stack-using-queues/

# i want to implement a stack using a queues
# what's a stack, an structure, 
# where elements are stored in the order they are added..

# and when the elements are removed, the order is reversed..
# the last element added is the one removed first..

# i.e. 
# we add a then add b
# we remove b then remove a

# and we want to implement this using queues..
# what's a queue?

# like a stack, it stores elements in the order they're added
# but when elements are removed, they are removed in the order they are added..

# i.e.
# we add a then b
# we remove a then b..

# these two structures are diametrically opposite..
# how am i supposed to implement one with the other..

# they both store data in the same order so i can start there..
# i'd use a queue to store the data

# but now, `pop`, the remove element method..
# for queues.. i'd can only remove the first element..
# i want to remove the last..

# i can only remove the last from a queue, if i remove all the elements..
# i guess.. this what imma have to do then..

# then put the elements back into the queue..
# it's a weird one...

# to remove one element, remove all..
# okay, and how would that go.. how would you add the elements back..

# well, we need to store the elements somewhere when we remove them..
# technically, you can reuse the same queue..

# how? before anything, find the length of the queue.. `n`
# so for the queue.. we'd pop (remove first element)
# and add it back to the queue immediately..

# we'd do this for every element except the nth element..
# we'd know the nth element, since we'd be counting from the jump..

# so.. that's how pop would work..

# top, this is the element last added, do queues allow you
# check the last element? in Python, yes. however i'd have to check the official
# answer to know if i can do `queue[-1]`

# `empty` is a simple one.. return len(queue) == 0

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        itemCount = len(self.queue)
        
        for idx in range(itemCount):
            elem = self.queue.popleft()
            
            if idx == itemCount - 1:
                return elem
            
            self.queue.append(elem)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0

