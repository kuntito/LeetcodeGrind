# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

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

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        pass
        # create a dummy node that points to `head`
        # return `dummy.next`
        
        dummy = ListNode(0)
        dummy.next = head        
    
        # two pointers,
        # pointerOne starts on the first node
        # pointerTwo starts on the second node
        one = head
        two = head.next
        
        
        # for each value at pointerTwo
        # determine the greates common divisor between 
        # pointerOneVal and pointerTwoVal
        # create a ListNode and place inbetween
        # pointerOne and pointerTwo
        # set pointer One to pointerTwo and make way
        while two:
            pass
            divisor = self.get_greatest_divisor(one.val, two.val)
            visorNode = ListNode(divisor)
            
            one.next = visorNode
            visorNode.next = two
            
            one = two
            two = two.next
        
        return dummy.next
    
    
    def get_greatest_divisor(self, numOne, numTwo):
        pass
        smaller = min(numOne, numTwo)
        
        for i in range(smaller, 0, -1):
            if numOne % i == 0 and numTwo % i == 0:
                return i
            
            
eighteen = ListNode(18)
six = ListNode(6)
ten = ListNode(10)
three = ListNode(3)

eighteen.next = six
six.next = ten
ten.next = three

print(eighteen)
sol = Solution()
sol.insertGreatestCommonDivisors(eighteen)
print(eighteen)