# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/


from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
    
        # we're given a circular linked list with values in non-decreasing order, which means the contiguous values either stay the same or increase
        
        # that said, we're given a value `insertVal` and we want to place this appropriately in the linkedlist
        
        # are the list values unique?
        
        # it doesn't say if they're unique, i'd assume duplicates. i think "non-descending order" indicates duplicates
        
        # the `head` node isn't necessarily the head of the linked list, it's merely a value in the linked list
        
        # i'd say we determine the values of the linked list in order
        # once we have this, we can use binary search to find the insertion point of `insertVal`
        
        # but we'd have to handle duplicates
        # the linked list node knows the next node and only the next node
        
        # if i have 1->2->4
        # to insert `3`, i want to know where two is at
        # bin search can help
        # but what if i have 1->2->2->3
        # there's no guarantee which 2, bin search finds
        
        # so, really what i need is the last occurence of every number
        # since the list is sorted this shouldn't be an issue, i'd create an array to store the values
        
        # step 1: obtain the linked list values
        arr, lowestIdx = self.obtainValues(head)
        # print([a.val for a in arr])
        
        # now we need to to apply binsearch to find the insertion point
        # it's possible the value exists in the list
        
        # if the value exists in the list, it means we'd actually find the -
        
        # what does it mean if the value exists in the list
        # and if it doesn't
        # [1, 2, 3], say i wanted to insert `2`
        # binsearch would tell you where the value is or where it should be
        
        # since linked lists only look one way
        # i want to return the `idx - 1`
        # so in both cases where i want to insert to, the search returns index 0:
        
        # [1, 2, 3]
        # [1, 3]
        
        # then i can grab the last occurence of node `1`, break the link with it's neighbour, place a two after one and connect the neighbour
        
        insertIdx = self.binSearch(lowestIdx, arr, insertVal)
        prevNode = arr[insertIdx]
        
        nextNode = prevNode.next
        
        newNode = Node(insertVal)
        prevNode.next = newNode
        newNode.next = nextNode
        
        return head
        
    def binSearch(self, lowestIdx, arr, insertVal):
        left, right = lowestIdx, lowestIdx + len(arr) - 1
        
        while left <= right:
            idx = (left + right) // 2
            actualIdx = idx % len(arr)
            
            value = arr[actualIdx].val
            if value == insertVal:
                return actualIdx - 1
            elif value > insertVal:
                right = idx - 1
            else:
                left = idx + 1
                
        return (left % len(arr)) - 1
        
        
    def obtainValues(self, head):
        # `arr` contains the last of each value
        # in this case, we could only append to arr
        # if the value of the last node is different from the new node
        
        # if the values are the same, simply update the node
        # this way arr would contain all the unique nodes
        # the order is not guaranteed to be low to high
        # but it's circularly guaranteed to be low to high
        # so we need to track the lowest value and it's index
        # so we know where low starts and where it ends
        arr = []
        
        # since it is circular, we know we've reached the end when we see `head` again
        curr = head
        firstTime = True
        lowestIdx = 0
        while True:
            if curr is head and not firstTime:
                break
            
            if firstTime:
                firstTime = False
                
            # if the array has a value and the node value is the same as the current node's value, we remove it, since we want the last occurrence of every node 
            if arr and curr.val == arr[-1].val:
                arr.pop()

            if not arr or curr.val != arr[-1].val:
                arr.append(curr)
                # updating the lowest value
                if curr.val < arr[lowestIdx].val:
                    lowestIdx = len(arr) - 1
            
            curr = curr.next
            
        return arr, lowestIdx
    
one = Node(1)
three = Node(3)
four = Node(4)

one.next = one
# three.next = four
# four.next = one

sol = Solution()
sol.insert(one, 2)