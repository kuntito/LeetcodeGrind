class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        
        pass
        # this question is a spin-off of `https://leetcode.com/problems/merge-two-sorted-lists/`
        # but with `n` lists
        
        # `lists` is an array of sorted linked lists
        # we can basically reuse the solution
        # pop the last two linked lists from `lists`
        # merge them and append the merged linked list to `lists`
        # keep doing it until `lists` has one element left
        
        while len(lists) > 1:
            uno, dos = lists.pop(), lists.pop()
            merged = self.mergeBoth(uno, dos)
            lists.append(merged)
            
        return lists[0]
        
        
    def mergeBoth(self, uno, dos):
        pass
        # to merge both lists
        # we'd have to pick the smaller head node from each list
        # the idea here is while both lists, `uno` and `dos`
        # have nodes
        # compare both nodes and remove the smaller one
        # and append to the new list
        
        # we would need a pointer, `curr`
        # that points to the current node
        
        # create a dummy linked list node and append all subsequent nodes to it
        # so we could easily address the problem of adding the first node
        
        # when we run out of nodes in either one
        # we can just append the whichever nodes remain in `uno` or `dos` to `curr`
        
        # and we'd return `dummy.next`
        
        dummy = ListNode("dummy")
        curr = dummy
        
        while uno and dos:
            if uno.val < dos.val:
                smaller = uno
                uno = uno.next
            else:
                smaller = dos
                dos = dos.next
                
            curr.next = smaller
            curr = smaller
            
        # the rationale here is if we had two differently sized nodes
        # [0, 2] and [1]
        # the first iter would have "dummy" -> 0
        # the lists would become [2] and [1]
        # the second iter would be "dummy" -> 0 -> 1
        # changing the liste to [2] and []
        
        # since the second list is empty, the while loop ends
        # at this point, we know at most one node still has values
        # but we don't know which
        # so we check both of them
        # whichever list has values, since they're sorted, it means all their nodes
        # have values greater than or equal to `curr.val`
        if uno:
            curr.next = uno
        if dos:
            curr.next = dos
            
        return dummy.next
                