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
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        
        if fast is None:
            return slow.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        nth_node = slow.next
        slow.next = nth_node.next

        return head

    

one = ListNode(1)
two = ListNode(2)

one.next = two

sol = Solution()
res = sol.removeNthFromEnd(one, 1)

print(res)
