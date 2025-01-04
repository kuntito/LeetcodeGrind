# https://leetcode.com/problems/copy-list-with-random-pointer/description/

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head: return None

        clone_map = {None: None}
        curr = head
        while curr:
            clone_map[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = clone_map[curr]
            clone.next = clone_map[curr.next]
            clone.random = clone_map[curr.random]
            curr = curr.next

        return clone_map[head]