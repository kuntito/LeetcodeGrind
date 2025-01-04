# https://leetcode.com/problems/reverse-nodes-in-k-group/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

class Solution:
    def reverseKGroup(self, head: ListNode, k: int):
        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, dummy

        count = 0
        while right.next:
            right = right.next
            count += 1

            if count % k == 0:
                # sol.print(dummy)
                nexxt = right.next
                newHead = left.next
                self.reverse(
                    newHead,
                    right
                )
                left.next = right
                newHead.next = nexxt

                left = newHead
                right = newHead

        return dummy.next
    

    def reverse(self, uno, dos):
        if uno == dos:
            return uno
        
        res = self.reverse(uno.next, dos)
        res.next = uno
        res.next.next = None

        return res.next


    def print(self, node):
        res = []
        while node:
            res.append(node)
            node = node.next

        print(res)
        

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)


one.next = two
two.next = three
three.next = four
four.next = five

sol = Solution()
res = sol.reverseKGroup(one, 2)
sol.print(res)
# a = sol.reverse_group(three, five)
# sol.print(five)