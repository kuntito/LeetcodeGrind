class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f'({self.val})'
        
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # get the last `k` nodes.
        # connect head's tail to `head`
        
        if head is None: return None

        listLen, tail = self.get_len_and_tail(head)
        
        rotateCount = k % listLen
        if rotateCount == 0: return head
        
        lastStop = listLen - rotateCount

        newHead = self.sever_from(
            head,
            lastStop
        )
        
        if tail != head:
            tail.next = head
        
        return newHead
    
    def get_len_and_tail(self, head):
        length = 0
        tail = None
        
        while head:
            length += 1
            
            tail = head
            
            head = head.next
            

        return length, tail
    
    
    def sever_from(self, node, lastStop):
        count = 0
        while node:
            count += 1
            
            if count == lastStop:
                newHead = node.next
                node.next = None
                return newHead
            
            node = node.next
            
arr = [
    [
        ListNode(val=1), 
        1
    ],
]
foo, bar = arr[-1]
            
sol = Solution()
res = sol.rotateRight(foo, bar)

print(res)