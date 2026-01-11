# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        values = []
        current = self
        while current:
            values.append(current.val)
            current = current.next
        return str(values)
    
    def __repr__(self):
        return str(self)
    
class Solution:
    def reverseBetween(self, head:ListNode, left: int, right: int):
        pass
        # get left node and right node
        # create function to reverse nodes
        # connect them to their new neighbours
        
        dummy = ListNode()
        
        dummy.next = head
        
        leftNode, leftNei = None, None
        rightNode, rightNei = None, None
        
        curr = dummy
        count = 0
        while curr:
            if count + 1 == left:
                leftNode = curr.next
                leftNei = curr
            elif count == right:
                rightNode = curr
                rightNei = rightNode.next
            
            curr = curr.next
            count += 1
            
            
        # print(rightNode)
        new_chain = rightNode
        end_chain = self.reverse(leftNode, rightNode)
        # print(leftNei)
        # print(rightNei)
        # print(new_chain)
        
        leftNei.next = new_chain
        end_chain.next = rightNei
        
        return dummy.next
    
    def reverse(self, currNode, stopNode):
        if currNode == stopNode:
            return currNode
        
        revNode = self.reverse(currNode.next, stopNode)
        revNode.next = currNode
        revNode.next.next = None
        
        return revNode.next
    
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

sol = Solution()
res = sol.reverseBetween(one, 2, 4)
print('ans is', res)