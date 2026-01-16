# https://leetcode.com/problems/merge-two-sorted-lists/description/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# given two linked lists, two sorted linked lists, i want to merge the nodes into one..
# while keeping them sorted..

# the nodes have numeric values.. in them..
# and that's what's sorted..

# how would you approach this..
# i'd create a dummy head node..
# and have two pointers..

# i'm iterating through both nodes at once..
# initially, both pointers start at the head of both nodes..

# while both pointers are valid, i.e. both pointers point to nodes..
# i'd compare the two nodes..
# whichever one is less, gets appended to the dummy node..
# and i update the dummy node pointer..

# ideally, i want to keep a reference to the dummy pointer somewhere
# so i can return dummyNode.next as the result..
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
        dummyNode = ListNode(0)
        curr = dummyNode
        
        uno, dos = list1, list2
        
        while uno and dos:
            # if uno's value is less than dos's value..
            # make curr point to uno, update curr, update uno
            if uno.val < dos.val:
                curr.next = uno
                curr = uno
                uno = uno.next
            else:
                # at this point, uno and dos, their values are either equal or dos' value is less
                # in which case it wouldn't matter, append dos to curr, update curr
                # update dos
                curr.next = dos
                curr = dos
                dos = dos.next
                
        # at this point, we've run out of uno or dos or both
        # if both, we're good to go, return dummyNode.next
        
        # if run out of uno
        # then it means whatever's left of dos.. can be appended to curr
        if dos: # i can simply write this as opposed to `not uno`, since the while loop guarantees that only one of these can survive till here
            curr.next = dos
        
        # likewise, if run out of dos
        # then it means whatever's left of uno, can be appended to curr
        if uno:
            curr.next = uno
                
        
        return dummyNode.next