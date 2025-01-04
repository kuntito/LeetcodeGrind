# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

# TODO https://neetcode.io/solutions/palindrome-linked-list
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        # if linked list only contains two nodes
        if head.next.next is None:
            return head.val == head.next.val
        
        # find the half way point
        # to reach half way, you need two pointers
        # `slow` and `fast`
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # from `slow`, reverse the linked list
        prev = slow
        curr = slow.next

        
        # once you reached the end
        # start two pointers, `left` and `right`
        # check if their values are equal
        
        


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

sol = Solution()
res = sol.isPalindrome(a)
print(res)