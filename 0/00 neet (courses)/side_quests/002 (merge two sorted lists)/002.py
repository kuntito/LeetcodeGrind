# https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        current = self
        while current:
            values.append(current.val)
            current = current.next
        return str(values)
    
    def __repr__(self) -> str:
        return str(self)


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        res = ListNode(0)
        tail = res

        while list1 and list2:
            if list1.val <= list2.val:
                node = list1
                list1 = list1.next
                node.next = None
            else:
                node = list2
                list2 = list2.next
                node.next = None

            tail.next = node
            tail = node

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return res.next
    

foo = ListNode(1)
foo.next = ListNode(2)
foo.next.next = ListNode(3)

bar = ListNode(1)
bar.next = ListNode(3)
bar.next.next = ListNode(4)

sol = Solution()
res = sol.mergeTwoLists(foo, bar)

print(res)