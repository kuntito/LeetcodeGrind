# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f'({self.val})'

# i'm given a linked list..
# and i want to switch up the order

# easier to show than write..
# consider the linked list..

# original order:
# first => second => third => fourth

# switch up order:
# first => fourth => second => third..

# watched deeps' solution..
# and he reversed the second half of the list..

# and how exactly does this help us..
# since you reversed the second half..

# i imagine you'd be at the end of the list
# say you started with 
# 1 => 2 => 3 => 4

# the second half is 3 => 4
# when reversed, the entire list becomes

# 1 => 2 => 3 <= 4
# this way, we have the start of the list
# 
# we've reversed and would have a reference to the end of the list.
# i can simply connect first to last
# move both pointers forward..

# how do you get to the middle of the list..
# two pointers..
# slow and fast..

# slow moves one node at a time..
# fast moves two nodes at a time..

# idea is fast reaches the end first
# and at that time.. slow should tell us where the middle is..

# i expect different behavior for even and odd lengthed linked lists..

# let's run through it..

# 1 => 2 => 3
# SF

# after one iteration
# 1 => 2 => 3
#     S     F
# fast is at the end.. so if even.. when fast reaches the end..
# slow would be pointing to the second half..

# how about even..
# 1 => 2
# SF

# after one iteration
# 1 => 2
#     S    F
# by the time fast is out of bounds..
# slow is at the start of the second half 




from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # also, address the edge case of a single node
        
        slow, fast = head, head
        
        # i don't think i completely understood how to address
        # odd and even lengthed nodes for the fast pointer
        
        # consider an even ll:
        # 1 -> 2 -> None
        
        # fast would move from 1 -> None
        # fast always ends up at None
        
        # is this true for longer lls:
        # 1 -> 2 -> 3 -> 4 -> None
        # fast would move from 1 -> 3 -> None..
        
        # yes, if even, `fast` always ends up at None
        
        # how about odd..
        # 1 -> None
        # fast would move from.. `1` to ...
        # it wouldn't be able to move twice..
        # so how would i be able to tell if it's odd or not..
        
        # if odd.. you'd end up at a point where..
        # fast.next is None..
        
        # you would never have that with an even node..
        # is that so..
        # 1 -> 2 -> 3 -> 4 -> None..
        # you'd move from 1 -> 3
        # then move from 3 -> None..
        # at no point is fast.next None..
        
        # right, so i want to write the loop in a way
        # that i can tell if ll is odd or even..
        
        # if even.. i know fast ends at None..
        # if odd.. i know fast ends when fast.next is None..
        
        # `while fast and fast.next`
        # if even, `fast` check breaks the loop
        # if odd, `fast.next` breaks the loop..
        
        # in either case, we either end up `fast == None`
        # or `fast.next is None..`
        
        # the while condition is 
        # now, what's the state of `slow` in both conditions..
        while fast and fast.next:
            pass
            
        
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

sol = Solution()
sol.reorderList(one)