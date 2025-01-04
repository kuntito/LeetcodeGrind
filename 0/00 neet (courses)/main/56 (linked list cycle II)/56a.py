# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.val) if self.val else 'None'


class Solution:
    def detectCycle(self, head):
        if not head: return None
        slow, fast = head, head
        seen = set()

        while fast and fast.next:
            if fast.next in seen:
                return fast.next
            if fast.next.next in seen:
                return fast.next.next
            seen.add(slow)

            slow = slow.next
            fast = fast.next.next
            
        return None
    
one = ListNode(1)
two = ListNode(2)

one.next = two
two.next = one

sol = Solution()
res = sol.detectCycle(one)
print(res.val)