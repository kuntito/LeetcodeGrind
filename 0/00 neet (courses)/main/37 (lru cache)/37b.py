class Node:
    def __init__(self, key: int = None, val: int = None) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.collection = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        res = self.get_internal(key)
        print(res)
        return res

    def get_internal(self, key: int) -> int:
        if key in self.collection:
            self.make_mru(self.collection[key])
            return self.collection[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if len(self.collection) == self.capacity and key not in self.collection:
            lru_node = self.head.next
            del self.collection[lru_node.key]
            self.remove(lru_node)

        if key in self.collection:
            self.collection[key].val = value
            self.make_mru(self.collection[key])
        else:
            node = Node(key, value)
            self.collection[key] = node
            self.append(node)


    def make_mru(self, node: Node):
        self.remove(node)
        self.append(node)

    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def append(self, node: Node):
        og_last_node = self.tail.prev

        node.next = self.tail
        self.tail.prev = node

        node.prev = og_last_node
        og_last_node.next = node


capacity = 2
sol = LRUCache(capacity)


sol.put(1, 1)
sol.put(2, 2)
sol.get(1)
sol.put(3, 3)
sol.get(2)
sol.put(4, 4)
sol.get(1)
sol.get(3)
sol.get(4)