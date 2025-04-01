# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass
        # one approach is to have two pointers, `left`, `right`
        # `right` is initialized to nth node from the start
        # i.e. if the end node is `3`, and the linked list is [1, 2, 3, 4, 5]
        # move right pointer `3` nodes forward, it would be at node `3`
        
        # create a dummy node and point it to `head`
        # place the left node at the dummy node
        # the linked list now looks like this [dummy, 1, 2, 3, 4, 5]
        # left = dummy
        # right = 3
        # the reason for this is we want to remove the nth node from the end of the list
        # we'd iterate both nodes together, such that when the `right` pointer hits the end
        # of the array, the `left` pointer would point to the node before the nth node from the end of the list
        
        # simulating the iterations
        # left = dummy, right = 3
        # left = 1, right = 4
        # left = 2, right = 5
        
        # at this point `right` has reached the end of the list
        # and `left` is pointing to the node before the nth node from the end of the list
        # this way to remove it, we'd identify the `nthNode`
        
        # then do `left.next = nthNode.next`
        # `nthNode.next = None`
        
        # this way we've remove the nthNode from the end
        # we best keep a reference to the head such that we can return it at the end
        
        # TODO what happens when `n` is `0`
        
        
        
        
        
        # now, move both nodes together
        # till the `right` node hits the end
        # when it does
        