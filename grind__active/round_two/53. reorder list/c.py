# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f'({self.val})'
        
# what am i doing?
# i want to reorder a linked list.

# if the current order is
# a -> b -> c -> d

# i want to pair the first and last nodes
# and continue to do so till i run out of first or last nodes.

# the new order looks like:
# a -> d -> b -> c

# i'd connect the first and last nodes, `a` and `d`
# then progress, both pointers, to `b` and `c` respectively

# these guys are already connected so no need for further connections.

# and how would this go in code?
# i'd need two pointers, one at each tailend.

# then use that to connect both nodes.
# one problem is linked lists go one way..
# even if you had a pointer at the tail end.
# you couldn't go backwards..

# one idea, i want to implement
# is to reverse half of the linked list.

# get to the mid point
# reverse linked list...
# you'd have your two pointers..

# reorder list.

# the first problem, getting to the mid point.
# you only know the mid point, once you've reached the end.

# how to do this?
# two pointers..
# one moves twice as fast as the other.
# the moment it reaches the end, it'd tell us what we need to find the mid point.

# how do you address, even and odd linked lists node counts..

# well,
# for even
# 1 => 2
# both nodes start at `1`
# on first iteration:
#  slow node moves to `2`
#  fast node goes out of bounds..

# what does this tell us, for even nodes counts
# fast node goes out of bounds.. and leaves slow node at the start of the mid point..

# how about odd node count:
# the simplest case with a mid point is:
# 1 => 2 => 3
# both nodes start at `1`
# on first iteration
# slow node moves to `2`
# fast node reaches the end at `3`
# what does this tell us, for odd node counts..
# fast node reaches the end, and leaves low node at the start of the mid point..

# so we know how to get to the mid point..
# if fast node goes out of bounds or reaches the end, i.e. has no next node..

# what's the while condition..
# while fast and fast.next?

# what happens if you have `fast` but not `fast.next`
# means node count is odd and you've reached the end..

# what happens if you don't have `fast`, means node count is even
# and you've reached the end.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        
        lastNode = None
        while fast and fast.next:
            slow = slow.next
            
            if fast.next.next is None:
                lastNode = fast.next
            fast = fast.next.next
            
        if lastNode is None:
            lastNode = fast
            
        midPoint = slow
        
        self.reverseOnwards(midPoint)
        
        left = head
        right = lastNode
        
        # TODO, see official solution for this..
        # the connecting logic..
        
        # what's the best approach..
        # save the next nodes for each tailend..
        
        # connect the tail ends
        # connect the second tail end (right one) to the next left
        
        while left and right and left.next != right:
            nextLeft = left.next
            nextRight = right.next
            
            left.next = right
            right.next = nextLeft
            
            left = nextLeft
            right = nextRight
            
        return head
        
        
    def reverseOnwards(self, currentNode: ListNode):
        nextNode = currentNode.next
        # sever current node's bond to the next
        currentNode.next = None
        while currentNode and nextNode:
            # holding the next next node in memory
            temp = nextNode.next
            # connecting next node to current node, the reversal
            nextNode.next = currentNode
            
            currentNode = nextNode
            nextNode = temp
                
                
sol = Solution()

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

res = sol.reorderList(one)
print(res)