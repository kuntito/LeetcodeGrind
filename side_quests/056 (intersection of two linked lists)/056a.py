# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

# TODO https://neetcode.io/solutions/intersection-of-two-linked-lists
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        seen = set()
        
        curr = headA
        while curr:
            seen.add(curr)
            curr = curr.next
        

        curr = headB
        while curr:
            if curr in seen:
                return curr
            curr = curr.next

        return None