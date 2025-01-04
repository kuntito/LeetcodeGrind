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
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.val != arr.pop():
                return False
            curr = curr.next
        
        return True


a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

sol = Solution()
res = sol.isPalindrome(a)
print(res)