# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:

        samp = self
        temp = []
        while samp:
            temp.append(str(samp.val))
            samp = samp.next

        return "[" + ", ".join(temp) + "]"
    
    def __repr__(self) -> str:
        return str(self)



class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None: return list2
        if list2 is None: return list1

        if list1.val < list2.val:
            res = ListNode(list1.val)
            list1 = list1.next
        else:
            res = ListNode(list2.val)
            list2 = list2.next

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    list1 = self.add_next(res, list1)
                else:
                    list2 = self.add_next(res, list2)
            elif list1:
                list1 = self.add_next(res, list1)
            elif list2:
                list2 = self.add_next(res, list2)

        return res


    def add_next(self, node, lst):
        temp = node
        while temp.next is not None:
            temp = temp.next

        temp.next = ListNode(lst.val)
        lst = lst.next
        return lst


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(5)

foo = Solution()
res = foo.mergeTwoLists(a, b)
print(res)

