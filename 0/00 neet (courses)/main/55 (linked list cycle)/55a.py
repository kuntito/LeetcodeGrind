# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not (head and head.next): return False

        seen = set()
        slow, fast = head, head.next

        while fast.next and fast.next.next:
            if fast in seen:
                return True

            seen.add(slow)
            slow = slow.next
            fast = fast.next.next


        return False