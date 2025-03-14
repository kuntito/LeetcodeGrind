# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if not self.val: return 'None'

        res = []
        node = self
        while node:
            res.append(str(node.val))
            node = node.next

        return '[' + ','.join(res) + ']'


    def __repr__(self) -> str:
        return str(self)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)

        slow, fast = dummy, head

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        nth_node = slow.next
        slow.next = nth_node.next

        return dummy.head

