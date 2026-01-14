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
# you want to to point the leaf node to the curr node...
# then point the curr node to None

# then return the curr node

# okay, this summarizes the while loop but how do you get the head of the reversed linked list
# global variable??

# also, edgecase, if `head` is None, return None
class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        
        self.res = None
        
        self.explore(head)
        
        return self.res
    
    def explore(self, node):
        if node.next is None:
            self.res = node
            return node
        
        retNode = self.explore(node.next)
        retNode.next = node
        node.next = None
        
        return node