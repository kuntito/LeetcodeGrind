# https://neetcode.io/problems/reverse-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if head is None: return None

        rev = ListNode(head.val)
        while head.next is not None:
            head = head.next
            new_node = ListNode(head.val)
            new_node.next = rev
            rev = new_node

        return rev