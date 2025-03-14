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
    
    def __repr__(self):
        return str(self)
    
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five