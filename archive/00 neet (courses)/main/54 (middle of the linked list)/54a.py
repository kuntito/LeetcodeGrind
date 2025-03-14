# https://leetcode.com/problems/middle-of-the-linked-list/description/

class Solution:
    def middleNode(self, head):
        if not head: return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow