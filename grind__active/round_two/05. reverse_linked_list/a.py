# https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# a linked list is a set of back to back `ListNodes`
# say the following chars are nodes

# a -> b -> c -> None
# each node points to the next and the last node points to nothing

# a reversal of this linked list would be
# c -> b -> a -> None

# so how would this work? i remember this from last time
# starting here,

# a -> b -> c -> None

# we start from the leaf node i.e. the node with no child
# c -> None

# now, we want to point it to the node before it..
# so we need to know the node before it

# it's looking like two traversals
# first trav, where we know the OG order
# once we hit the leaf node, we go backwards
# passing the node we last hit

# on each backward traversal, you want to connect the last hit node
# to the curr node in the backward traversal

# i know there's a recursive solution, but i can possibly do this with a while loop and an array
# the first traversal is determined by a boolean, `not is_leaf_found`
# we declare an array, `nodes`
# and append each node as we traverse..

# once we hit the leaf node, we store it as lastHit
# the while loop conditional is now determined by `nodes` not being empty

# we then connect lastHit => nodes.pop()
# we keep doing this until the node is empty

# after which we return lastHit
# so three variables, `is_leaf_found`, `nodes`, `lastHit`

# one tricky part is, we want to return the new head of the reverse node
# technically, this is the leaf node..

# so, i'd need a third variable, `res`
# once, i find the lead node, i'd set `res = leafNode`

# we can't use lastHit, since it keeps updating itself to the curr node in the backwards traversal

# two edge cases, i didn't discuss
# on the backwards traversal, we risk circular linking
# say `a -> b -> None`

# once, we hit leaf `b -> None`
# we store it as `lastHit = b -> None`

# now, we traverse backwards,
# then point last hit to `nodes.pop`

# i just realized, i should only do `nodes.append` for non-leaf nodes
# previously, i was doing it for all nodes..

# nonetheless, back to the thought train

# once we traverse backwards,
# we point lastHit to nodes.pop
# which in this case would be the node, `a -> b -> None`

# pay attention, lastHit = b -> None
# if i point this to nodes.pop, i'd have...

# b -> a -> b -> ... {this will no longer be None, since b now points to `a`}
# b -> a -> b -> a -> b ->

# this is the circular thing i was on about..
# so after we connect lastHit -> nodes.pop()
# we want to make sure nodes.pop().next = None

# don't call the `pop()` method more than once, else, you'd keep popping
# store the value somewhere


# it works but i think the recursive solution is easier
# perhaps, this is what recursion is.. the forward and backward traversals..
class Solution:
    def reverseList(self, head):
        if not head:
            return None

        curr = head
        lastHit = None
        nodes = []
        is_leaf_found = False
        res = None

        while (not is_leaf_found) or nodes:
            if is_leaf_found:
                lastHit.next = nodes.pop()
                lastHit = lastHit.next
                lastHit.next = None
            else:

                if curr.next is None:
                    is_leaf_found = True
                    res = curr
                    lastHit = curr
                else:
                    nodes.append(curr)

                    curr = curr.next

        return res
