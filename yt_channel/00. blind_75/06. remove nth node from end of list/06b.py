# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f"({self.val})"
    
    def __repr__(self):
        return str(self)
        
    def printAll(self):
        arr = []
        curr = self
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        res = '[' + ','.join(str(val) for val in arr) + ']'
        print(res)
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass
        # we want to remove the nth node from the end of a linked list
        # first we need to identify the nth node from the end
        
        # the linked list in this question is one way
        # left to right
        
        # so we'd have to go through the list at least once to find the result
        # we could keep track of the nodes in an array
        # such that we can index the target node and remove it
        
        # actually, we'd index the node before the target node
        # then connect this node to the next node after the target
        
        # say our target is `2`
        # we'd get the node before target, `arr[-2 - 1] = arr[-3]`
        # we'd get the node after target, `arr[-2 + 1] = arr[-1]`
        
        # then do, `nodeBefore.next = nodeAfter`]
        # then do, `targetNode.next = None`
        
        # what if there's no node before
        # this would mean, our target node is the first node
        # in this case, we'd ...
        
        # and thus, the dummy node was invented
        # let's place a dummy node at the start of the `arr`
        # such that in this case, the dummy node would act as the defacto before
        # and after all said and done, we'd return dummyNode.next
        # since this would surely point to the head of the linked list
        
        # what if there's no node after
        # if it doesn't exist, simply return `None`
        
        # keep the `dummyNode` in mind when indexing from behind
        
        dummyNode = ListNode("dummy")
        # point the dummyNode to `head`
        dummyNode.next = head
        
        arr = []
        curr = dummyNode
        while curr:
            arr.append(curr)
            curr = curr.next
            
        # our target node is `arr`
        # say we have [1, 2, 3, 4, 5]
        # and `n` is `2`
        # we'd simply do `arr[-2]`
        # but since we have a dummy node
        # ["dummy", 1, 2, 3, 4, 5]
        # we'd still do `arr[-2]`
        # bars!
        
        targetNode = arr[-n]
        nodeBefore = arr[-n - 1]
        
        # TODO this condition is faulty, if `n == 1`
        # it does `-n + 1 == 0` which would point to the start node
        # instead of None, the <len(arr) check is based on positive indexing
        nodeAfter = arr[-n + 1] if (-n + 1) < len(arr) else None
        
        nodeBefore.next = nodeAfter
        targetNode.next = None
        
        return arr[0].next
    
    
    
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

# one.next = two
# two.next = three
# three.next = four
# four.next = five

# one.printAll()
sol = Solution()
res = sol.removeNthFromEnd(one, 1)
res.printAll()