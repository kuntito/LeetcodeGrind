# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        curr = head

        while curr:
            nxt = curr.next
            while nxt and nxt.val == curr.val:
                nxt = nxt.next

            curr.next = nxt
            curr = nxt

        return head