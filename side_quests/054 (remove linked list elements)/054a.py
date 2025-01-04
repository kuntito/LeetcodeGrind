# https://leetcode.com/problems/remove-linked-list-elements/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TODO https://neetcode.io/solutions/remove-linked-list-elements
class Solution:
    def removeElements(self, head, val: int):
        # create a dummy node before `head`
        # loop through the linked list using two pointers
        # `uno` and `dos`

        # initialize `uno` at `dummy`
        # initialize `dos` at `head`
        # when `dos.val` == val
        # set `uno.next` to `dos.next`
        # `dos` becomes `dos.next`

        # when done, return `dummy.next`

        dummy = ListNode(0, head)

        uno, dos = dummy, head

        while dos:
            if dos.val == val:
                # TODO why does this work, why does `uno` point to `dos.next`
                # and not move forward
                # TODO how would 1 -> 6 -> 2 -> 6
                uno.next = dos.next
            else:
                uno = uno.next
            dos = dos.next

        return dummy.next
    
a = ListNode(1)
b = ListNode(2)
c = ListNode(6)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)
g = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

sol = Solution()
sol.removeElements(a, 6)

while a:
    print(a.val)
    a = a.next