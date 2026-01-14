# https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# what am i doing, i want to reverse the linked list.

# what's the approach? recursion.
# what? for each node, start a recursive call, `exploreNode`
# in each recursive call, check if you have a leaf node

# if you do, return leaf node..
# okay, what then happens after a return..
# you want to to point the leaf node to the curr node..
# then point the curr node to None

# then return the curr node

# okay, this summarizes the while loop but how do you get the head of the reversed linked list
# in `b.py`, i used a global variable but apparently, you can return the head of the reversed without using a global variable

# the trick is modify the list starting with the curr node..
# we know the currNode -> nextNode
# now we point to point that nextNode to currNode
# currNode -> nextNode -> currNode -> ...

# now disconnect currNode
# currNode -> None

# okay, in memory, we'd have nextNode -> currNode
# but what do we return?

# the leaf node..
# the restructuring happens in the currNode, nextNode magic
# not in what we return

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        
        return self.explore(head)
        
    
    def explore(self, currNode):
        if currNode.next is None:
            return currNode
        
        revNode = self.explore(currNode.next)
        
        currNode.next.next = currNode
        currNode.next = None

        return revNode