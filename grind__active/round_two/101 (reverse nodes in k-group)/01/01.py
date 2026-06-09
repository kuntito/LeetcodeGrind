from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(
        self, 
        head: Optional[ListNode], 
        k: int
    ) -> Optional[ListNode]:
        batchStart = head        
        batchIter = self.getBatchIter(batchStart=batchStart)
        
        
        
        # now, i move `batchIter` k times
        for _ in range(k):
            batchIter = batchIter.next
            
            if batchIter is None:
                break
            
        # at this point, batchIter is at node k or is None
        # so i want to reverse and keep the batch connected to the next node.
        if batchIter:
            nextNode = batchIter.next
            
            reversalLastNode = self.reverse(batchStart, batchIter)
            reversalLastNode.next = nextNode
            
            batchStart = nextNode            
            batchIter = reversalLastNode
            
        # TODO, finish this.
        # i've written the frame work for addressing each batch
        # it seems it'd be a recursive function
        # after reversal and reconnection
        
        
            
    def getBatchIter(self, batchStart):
        # batch iter should be a node before the first
        # so, batch iteration stops at the kth node.
        preStartNode = ListNode(0)
        preStartNode.next = batchStart
        
        return preStartNode