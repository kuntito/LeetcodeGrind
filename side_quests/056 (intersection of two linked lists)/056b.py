# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

# TODO why doesn't this work?
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        return self.explore(headA, headB, {})
    
    def explore(self, one, two, memo):
        foo = (one, two)
        if foo in memo:
            return memo[foo]
        
        if one == two:
            return one
        if not one:
            return None
        if not two:
            return None
        
        a = self.explore(one.next, two, memo)
        if a:
            memo[foo] = a
            return memo[foo]
        
        memo[foo] = self.explore(one, two.next, memo)
        return memo[foo]