class MyLinkedList:
    class Node:
        def __init__(self, val=None) -> None:
            self.val = val
            self.next = None

        def __str__(self) -> str:
            return f'[val={self.val}, next={self.next}]'

        def __repr__(self) -> str:
            return str(self)


    def __init__(self):
        self.last_index = -1
        self.head = None
        self.tail = self.head
        

    def get(self, index: int) -> int:
        res = self.get_node(index)
        return res.val if res else -1


    def addAtHead(self, val: int) -> None:
        node = self.Node(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = self.head
        self.increment_last_index()


    def addAtTail(self, val: int) -> None:
        node = self.Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = self.head
        self.increment_last_index()


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > (self.last_index + 1): return
        
        if index == (self.last_index + 1):
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            new_node = self.Node(val)
            prev_node = self.get_node(index-1)
            node_at_index = prev_node.next

            prev_node.next = new_node
            new_node.next = node_at_index

            self.increment_last_index()


    def deleteAtIndex(self, index: int) -> None:
        if not self.is_valid_index(index): return

        if index == 0:
            og_head = self.head
            self.head = self.head.next

            og_head.next = None
        else:
            prev_node = self.get_node(index-1)
            node_to_delete = prev_node.next

            prev_node.next = node_to_delete.next

            if node_to_delete == self.tail:
                self.tail = prev_node
            node_to_delete.next = None

        self.decrement_last_index()


    def increment_last_index(self):
        self.last_index += 1

    def decrement_last_index(self):
        self.last_index -= 1

    def is_valid_index(self, index):
        return index >= 0 and index <= self.last_index

    def get_node(self, index):
        if not self.is_valid_index(index): return None
        root = self.head
        for idx in range(index + 1):
            if idx == index: return root
            root = root.next


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
    

# the error started at the 18th/19th node
foo = MyLinkedList()
foo.addAtHead(84)
foo.addAtTail(2)
foo.addAtTail(39)
foo.get(3)
foo.get(1)
foo.addAtTail(42)
foo.addAtIndex(1, 80)
foo.addAtHead(14)
foo.addAtHead(1)
foo.addAtTail(53)
foo.addAtTail(98)
foo.addAtTail(19)
foo.addAtTail(12)
foo.get(2)
foo.addAtHead(16)
foo.addAtHead(33)
foo.addAtIndex(4, 17)
foo.addAtIndex(6, 8)
foo.addAtHead(37)
foo.addAtTail(43)
foo.deleteAtIndex(11)
foo.addAtHead(80)
foo.addAtHead(31)
foo.addAtIndex(13, 23)
foo.addAtTail(17)
foo.get(4)
foo.addAtIndex(10, 0)
foo.addAtTail(21)
foo.addAtHead(73)
foo.addAtHead(22)
foo.addAtIndex(24, 37)
foo.addAtTail(14)
foo.addAtHead(97)
foo.addAtHead(8)
foo.get(6)
foo.deleteAtIndex(17)
foo.addAtTail(50)
foo.addAtTail(28)
foo.addAtHead(76)
foo.addAtTail(79)
foo.get(18)
foo.deleteAtIndex(30)
foo.addAtTail(5)
foo.addAtHead(9)
foo.addAtTail(83)
foo.deleteAtIndex(3)
foo.addAtTail(40)
foo.deleteAtIndex(26)
foo.addAtIndex(20, 90)
foo.deleteAtIndex(30)
foo.addAtTail(40)
foo.addAtHead(56)
foo.addAtIndex(15, 23)
foo.addAtHead(51)
foo.addAtHead(21)
foo.get(26)
foo.addAtHead(83)
foo.get(30)
foo.addAtHead(12)

# print(foo)