# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/


from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        # we want to convert a binary search tree to a doubly linked list
        # i'm not sure i understand the question, the left and right pointers
        # of each node are it's predecessor and it's successor
        
        # so for each node, it's left child should have an edge pointing to it
        # and the node should have an edge pointing to it's right child
        # it alread has that, so we're only concerned with the left?
        
        # i couldn't understant the question from the description, so i read a bit from the editorial and discussions
        
        # we have a bst and want to flatten it and turn it into a circular linked list
        # the order of the nodes should be increasing and every node should be doubly
        # connected to each other
        
        # the tail node connects to the head and the head to the tail
        # by the looks of it, this should benefit from an inorder traversal
        
        # the left most node would be the least node, the head node, if we will
        # and it's parent would be the next highest node
        
        # i'd say traverse the tree inorder
        # and for every node after the first node, doubly connect the nodes
        
        # at the end of it all, connect the tail to the head
        
        arr = []
        self.exploreInOrder(root, arr)
        
        head, tail = arr[0], arr[-1]
        
        tail.right = head
        head.left = tail
        
        return head
        
    def exploreInOrder(self, node, arr):
        if not node:
            return
        
        self.exploreInOrder(node.left, arr)
        
        if arr:
            prev = arr[-1]
            prev.right = node
            node.left = prev
            
        arr.append(node)
        
        self.exploreInOrder(node.right, arr)