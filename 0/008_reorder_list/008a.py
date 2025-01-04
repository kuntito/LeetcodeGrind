# https://leetcode.com/problems/reorder-list/description/

from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return str(self.val) if self.val else 'None'

    def __repr__(self) -> str:
        return str(self)
    
    # def __str__(self) -> str:
    #     temp = ['[']
    #     node = self
    #     while node:
    #         temp.append(str(node.val))
    #         temp.append(',')
    #         node = node.next
    #     else:
    #         temp.pop()
    #     temp.append(']')

    #     return ''.join(temp)


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = deque()
        node = head
        while node:
            queue.append(node)
            node = node.next

        res = ListNode(0)
        temp = res
        while queue:
            top = queue.popleft()
            top.next = None
            temp.next = top
            temp = top

            if queue:
                bottom = queue.pop()
                bottom.next = None
                temp.next = bottom
                temp = bottom



        res.next = None


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)


three.next = four
two.next = three
one.next = two

# print(one)

sol = Solution()
sol.reorderList(one)

print(one)