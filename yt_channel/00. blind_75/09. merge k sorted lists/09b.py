class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        
        allNodes = []
        
        for lst in lists:
            if not lst: continue
            curr = lst
            while curr:
                allNodes.append(curr)
                curr = curr.next
                
        allNodes.sort(key=lambda x: x.val)
        
        dim = len(allNodes)
        for i in range(1, dim):
            prevNode = allNodes[i-1]
            currNode = allNodes[i]
            
            prevNode.next = currNode
            
            # clear the last node's next
            currNode.next = None
            
        return allNodes[0] if allNodes else None
                