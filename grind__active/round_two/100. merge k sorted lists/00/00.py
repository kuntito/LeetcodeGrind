# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TODO this works but deep the `nlogk` approach.
import heapq
class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        minHeap = []
        
        for ll in lists:
            while ll:
                heapq.heappush(
                    minHeap,
                    ll.val
                )
                ll = ll.next
                
        # this serves as a pointer to the first node
        # in the combined node.
        # so i can return `preFirstNode.next`
        # which would point to the first node.
        preFirstNode = ListNode()
        
        iterNode = preFirstNode
        while minHeap:
            val = heapq.heappop(minHeap)
            
            iterNode.next = ListNode(
                val = val
            )
            
            iterNode = iterNode.next

        return preFirstNode.next