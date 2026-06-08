from typing import List, Optional
import heapq
import itertools

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        minHeap = []
        counter = itertools.count()
        
        for ll in lists:
            curNode = ll
            while curNode:
                # disconnect the curNode from it's neighbor
                # save the neighbor node
                # then set cur's next to None
                neiNode = curNode.next
                curNode.next = None
                
                heapq.heappush(
                    minHeap,
                    (
                        curNode.val,
                        next(counter), # tie breaker for `curNode.val`
                        curNode
                    ),
                )
                
                curNode = neiNode
            
        dummyNode = ListNode()
        prevNode = dummyNode    
        while minHeap:
            _, _, curSmallestNode = heapq.heappop(minHeap)
            
            prevNode.next = curSmallestNode
            prevNode = curSmallestNode
            
        return dummyNode.next