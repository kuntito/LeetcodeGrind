# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __repr__(self):
        return f'({self.val})'

    def __str__(self):
        return self.__repr__(self)

from typing import Optional

# i want to solve this using Floyd's algo..
# i briefly read it, convinced myself i can solve the question using it..
# and now, i have to prove it..

# how's it work.. i confirmed it through a series of diagrams that..
# if i use two pointers:
#   one moving one step at a time
#   another, moving two steps at a time
# if a cycle exists.. the two pointers would meet at some point..

# and if there isn't a cycle.. the two step pointer would reach the end first..
# okay..
# both pointers can start anywhere, the result is the same..
# but for simplicity's sake..

# they'd both start at head..
# and i'd call them `sloth` and `sonic`

# what's the condition for the loop..
# we keep going unless, `sloth == sonic`
# yes, i see the problem.. if they both start at `head`
# the loop would never start..

# hence, sonic should start one step ahead or behind..
# ahead is easier to write, `sonic = head.next`

# okay, the loop keeps going unless,
# `sonic = sloth` or sonic has reached the end..
# so `sonic` must not be None..

# the way i've written this, how am i returning True or False..
# the while loop should run while sonic hasn't reached the end..
# in the while loop if sonic meets sloth..
# return False..

# turns out i was wrong, i couldn't solve it..
# it's giving dunning-kruger
# i have to debug..

# i did it again, i inverted the return Flags..
# i return False for cycles instead of True..

# i'd fix..
# it works, i guess it wasn't dunning or kruger..

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # can `head` be None? the question doesn't say
        # i'd assume it isn't until shown otherwise..
        
        # yes, `head`, can be `None`
        if not head:
            return None
        
        sloth = head
        sonic = head.next
        
        while sonic:
            if sonic == sloth:
                return True
            
            sloth = sloth.next
            
            # now it's possible, `sonic.next.next`, fails
            # reason being.. if we at the last node..
            # next is None, but next.next is ??
            # so.. if sonic.next, sonic.next.next else sonic.next..
            
            sonic = sonic.next.next if sonic.next else sonic.next
            
        return False
        
        
three = ListNode(3)
two = ListNode(2)
zero = ListNode(0)
negFour = ListNode(-4)

three.next = two
two.next = zero
zero.next = negFour
negFour.next = two

sol = Solution()
sol.hasCycle(three)


