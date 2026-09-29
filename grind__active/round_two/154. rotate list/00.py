class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # get the last `k` nodes.
        # connect head's tail to `head`
        

        last_k_nodes, tail = self.get_last(head, k)
        
        tail.next = head
        
        return last_k_nodes
    
    def get_last(self, head, k):
        tail = None
        
        # how do i get the last k nodes.
        # two pointers.
        
        # one is k nodes ahead.
        # they'd move together.
        # when front node reaches last node
        # back node would be pointing to last k nodes
        
        frontNode = head
        for _ in range(k):
            frontNode = frontNode.next
            
        # what if front node is None here.
        # well, there shouldn't be that case.
        
        # a rotation only changes something if it's less than the number of nodes.
        # a 5-elem node, rotated 5 times changes nothing. you have to rotate not 5 times to see a difference.
        
        # more or less.
        # but even more is less.
        
        # since rotating 6 times is the same as rotating once.
        # and so, the actual rotation is (k mod listLen)
            
        while frontNode.next:
            pass
        
        
        