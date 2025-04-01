# https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        pass
    
        # we want to merge two sorted linked lists
        # we'd have to take the smallest head node of each linked list
        # if they're equal, we can take any one
        
        # edge case alert, if either linked list is None
        # just return the other, FIXME can i use XOR `if a ^ b: return a ^ b`
        
        
        # once we know both lists have values, we set two pointers
        # one at the head of each node
        
        # using a while loop, we'd take the smallest head node and 
        # put it in a linked list
        
        # but it's more than likely the lists are of different lengths
        # this would mean, we'd run out of nodes for one of the list
        
        # the simple solution is to perform this check whenver both pointers
        # are valid
        
        # whenever one of them becomes invalid
        # it means the what's left of the other node can be appended to the result
        
        