# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/description/

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        pass
        # to make sure i understand the question, i'd like 
        # i'd like to clarify some details
        
        # immutable list node is a class, a layer of abstraction over a linked list
        # this layer of abstraction only allows to print the value of the current node and to change the current node to it's next neighbour
        
        # and using this abstraction, we are to print the values of the linked list in reverse order
        
        # i would approach this question by capturing...
        # hmm... we know the structure allows us to explore a linked list in order and print it's values
        
        # but we want to print the values in reverse order
        # i would use recur-
        
        # i want to print the next node
        # before the curr the node
        
        # and before i print that next node
        # i want to print it's own next node
        
        # and so on and so forth
        # it's looking like a recursive problem
        # but it stops at the last node
        # the node without a next door neighbour
        
        # i'd use a recursive function
        # where i explore the child node before the current node
        self.explore(head)
        
    def explore(self, node):
        if not node:
            return
        
        self.explore(node.getNext())
        node.printValue()