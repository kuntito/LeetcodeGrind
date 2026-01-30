# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return f'({self.val})'

# i'm given a linked list..
# and i want to switch up the order

# easier to show than write..
# consider the linked list..

# original order:
# first => second => third => fourth

# switch up order:
# first => fourth => second => third..

# it's almost as though, i have two pointers at the ends of the list
# and i'm creating the list such that
# the first pointer's node comes first
# then the second pointer's node comes next
# then i move both pointers to their original next nodes..

# first => third
# fourth => second

# now i do the same thing..
# but how do i implement this in code..

# i can access the nodes from left to right..
# it's the right to left order that's a bit dicey..

# i mean, i could disconnect all the nodes..
# store them in order in an array then connect them with the new order..

# this'd be much simpler..
# i'd iterate through the entire node..
# recursion might be a better approach..
# because of the backwards traversal..

# on the back travel, i'd disconnect the node and append it to the array
# what array, the tracking array.. i'd pass along with each recursive call

# each call appends it's node to the array..
# and disconnects itself to it's next node..
# but only after exploring the next node..
# base case is the leaf node..

# once we have the array..
# two pointers, left and right
# recreate the linked list with this..

# have a pointer to the head node..
# to be fair just return the original head..
# this wouldn't change..

# made two mistakes..
# one, using an array and not a deque..

# two, after realizing, i should be using a deque..
# i didn't check the append logic..

# the thing is, when recursing through the list..
# i'd go in the order `first => second => third => fourth`

# but on the way up, the order is reversed..
# i'd be appending `fourth => third => second => first`
# which is problematic because i wrote the code as though the order
# was the same..

# so i had to use a deque to appendleft and fix this and the code worked..
# but before claiming victory..
# while iterating through the disconnected array..

# i needed access to the elements at the start and the end..
# at first, with an array, i was thinking of finding the mid point..
# and doing some calculation to figure how many indices, i'd need on the left side
# and how many on the right side..

# while this could be done fairly simply..
# a deque was just more intuitive..
# i could pop left and pop right, as long as there's a right to pop
# and the loop condition would be while the deque is not empty

# also, i needed another variable to connect nodes across iterations..
# each iteration has me connecting the first to last.. if last exists..
# however, i needed something to connect the current last to the next iteration's first-last pair

# that's where `curr` comes in..
# initially set to `dummyNode`
# it always connects to the first node..
# and is updated to last node, if last node exists.. i.e. a node from the end..
# if not, it connects to the node at the start..

# and i simply return head as is..
# the first time i attempted this question, i think there was a different solution.
# i better look at that..

# interviewers might frown against me using a deque..
# what he did was have reverse the second half of the list..

# you start off with:
# 1 => 2 => 3 => 4

# and how does reversing help you
# 1 => 2 => 3 <= 4

# well i imagine, 
# you'd be at `4` after reversing

# since you always know the start of the list as `1`
# you can simply connect `1` to `4`
# then proceed to the next nodes..

# the reversal helps you know the next last node to address..
# so how do we reverse the second half..

# 



from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        orderDeque = deque()
        self.explore(head, orderDeque)
        
        print(orderDeque)
        
        curr = ListNode("dummy")
        while orderDeque:
            first = orderDeque.popleft()
            curr.next = first
            
            if orderDeque:
                last = orderDeque.pop()
                first.next = last
                
                curr = last
            else:
                curr = first
            
        return head
    
    def explore(self, node, orderDeque: deque):
        if not node:
            return
        
        self.explore(node.next, orderDeque)
        
        node.next = None
        
        orderDeque.appendleft(node)
        
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)

one.next = two
two.next = three
three.next = four

sol = Solution()
sol.reorderList(one)