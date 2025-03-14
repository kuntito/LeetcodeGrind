# https://leetcode.com/problems/design-linked-list/description/

class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.prev =  None
        self.next = None

    def __str__(self) -> str:
        return f'[val={self.val}, next={self.next}]'

    def __repr__(self) -> str:
        return str(self)

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.max_index = -1


    def get(self, index: int) -> int:
        node = self.get_node(index)
        if node:
            return node.val
        return -1

    def get_node(self, index: int):
        if not self.is_valid_index(index): return

        root = self.head
        for i in range(index+1):
            if i == index: return root
            root = root.next

    def is_valid_index(self, index):
        return index >= 0 and index <= self.max_index


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head.prev = node

            self.head = node
        else:
            self.head = node
            self.tail = node
        self.increment_index()        


    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail

            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.increment_index()


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.max_index + 1: return
        
        if index == 0:
            self.addAtHead(val)
        elif index == (self.max_index + 1):
            self.addAtTail(val)
        else:
            og_node_at_index = self.get_node(index)

            prev_node = og_node_at_index.prev
            prev_node.next = None
            og_node_at_index.prev = None

            node = Node(val)
            prev_node.next = node
            node.prev = prev_node

            node.next = og_node_at_index
            og_node_at_index.prev = node

            self.increment_index()


    def deleteAtIndex(self, index: int) -> None:
        if not self.is_valid_index(index): return
        
        if index == 0:
            og_head = self.head
            if og_head.next:
                self.head = og_head.next
                self.head.prev = None
                og_head.next = None
            else:
                self.head = None
                self.tail = None
        elif index == self.max_index:
            og_tail = self.tail
            self.tail = og_tail.prev
            self.tail.next = None
            og_tail.prev = None
        else:
            og_node_at_index = self.get_node(index)
            prev_node = og_node_at_index.prev
            next_node = og_node_at_index.next

            prev_node.next = None
            og_node_at_index.prev = None

            next_node.prev = None
            og_node_at_index.next = None

            prev_node.next = next_node
            next_node.prev = prev_node


        self.decrement_index()
        

    def increment_index(self):
        self.max_index += 1

    def decrement_index(self):
        self.max_index -= 1

    def __str__(self) -> str:
        node_dict = {}
        index = 0
        root = self.head
        while root:
            node_dict[root.val] = index
            root = root.next
            index += 1

        return str(node_dict)
    

    def __repr__(self) -> str:
        return str(self)


foo = MyLinkedList()
foo.addAtIndex(0, 10)
foo.addAtIndex(0, 20)
foo.addAtIndex(1, 30)
foo.get(0)

print(foo)