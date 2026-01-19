# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

# i'm given a linked list and want to find out if there's a cycle..
# what's a linked list, a data structure where each element knows the next element
# but only that.. no idea what element comes before or what position the current element is
# within the linked list..

# so, what is this cycle..
# this is when an element's next element is an element we've already seen..

# consider this:
# 1 => 2 => 3 => 1

# the cycle occurs at `3` => `1`
# each number represents a node..

# so, a set.. it seems so.. store all nodes seen..
# you see a node you've seen before.. duplicate..
# return False..

# else, return True

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # how do you iterate through a linked list..
        # while loop..
        
        # pointer is `head`, update head = head.next to keep the loop going..
        # loop ends when head becomes None
        # or we find duplicate..
        
        # i failed??
        # oh, i inverted the return Flags..
        # i want to return True, if i find a duplicate.. a cycle..
        # and return False, if no cycle exists..
        
        # i'd fix..
        
        seen = set()
        while head:
            if head in seen:
                return True
            
            seen.add(head)
            head = head.next
            
        return False