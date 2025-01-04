

# for lists
class Solution:
    def mergeKLists(self, lists):
        if not lists: return None

        list_dict = {i : lists[i] for i in range(len(lists)) if lists[i]}
        self.res = None

        while list_dict:
            idx_list_with_largest = next(iter(list_dict))
            for key in list_dict:
                lst = list_dict[key]
                if lst[-1] > list_dict[idx_list_with_largest][-1]:
                    idx_list_with_largest = key

            target_list = list_dict[idx_list_with_largest]
            self.insert(target_list.pop())
            if not target_list:
                del list_dict[idx_list_with_largest]

        return self.res

    def insert(self, item):
        node = ListNode(item)
        if self.res:
            node.next = self.res
            self.res = node
        else:
            self.res = node


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
    
    
# for linked list
class SolutionII:
    def mergeKLists(self, lists):
        if not lists: return None

        list_dict = {i : lists[i] for i in range(len(lists)) if lists[i]}

        self.res = None
        self.last = None
        while list_dict:
            x = next(iter(list_dict))
            for elem_key in list_dict:
                lst = list_dict[elem_key]
                if lst.val <= list_dict[x].val:
                    x = elem_key

            self.insertFirstIntoRes(list_dict[x])
            list_dict[x] = list_dict[x].next
            if list_dict[x] is None:
                del list_dict[x]

        return self.res

    def insertFirstIntoRes(self, item):
        node = ListNode(item.val)
        if self.res:
            self.last.next = node
        else:
            self.res = node
        self.last = node


# for linked list
class SolutionIII:
    def mergeKLists(self, lists):
        return self.explore(lists)
    
    def explore(self, linked_list):
        if len(linked_list) == 0: return None
        if len(linked_list) == 1: return linked_list[0]


        mid = len(linked_list)//2
        left = self.explore(linked_list[:mid])
        right = self.explore(linked_list[mid:])

        return self.merge(left, right)
    
    def merge(self, left, right):
        res = ListNode()
        tail = res

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next


        if left:
            tail.next = left
        if right:
            tail.next = right

        return res.next


# for linked list
class SolutionIV:
    def mergeKLists(self, lists):
        if not lists: return None

        while len(lists) > 1:
            merged_res = []
            for idx in range(0, len(lists), 2):
                left = lists[idx]
                right = lists[idx + 1] if (idx + 1) < len(lists) else None

                merged_res.append(self.merge(left, right))
            
            lists = merged_res

        return lists[0]
    
    def merge(self, left, right):
        res = ListNode()
        tail = res

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next


        if left:
            tail.next = left
        if right:
            tail.next = right

        return res.next

a = ListNode(1)
a.next = ListNode(2)

b = ListNode(3)

linked_lists = [a, b]
foo = SolutionIV()

res = foo.mergeKLists(linked_lists)
print(res)