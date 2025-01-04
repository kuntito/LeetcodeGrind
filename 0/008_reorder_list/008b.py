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
    def reorderList(self, head) -> None:
        uno, dos = head, head.next

        while dos and dos.next:
            uno = uno.next
            dos = dos.next.next

        second = uno.next
        uno.next = None
        
        first = head

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev
        while second:
            foo, bar = first.next, second.next

            first.next = second
            second.next = foo

            first = foo
            second = bar
        


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)


three.next = four
two.next = three
one.next = two


sol = Solution()
sol.reorderList(one)
