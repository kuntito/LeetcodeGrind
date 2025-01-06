# https://leetcode.com/problems/design-hashmap/description/

# TODO https://neetcode.io/solutions/design-hashmap
class MyHashMap:

    def __init__(self):
        pass
        # since we're expecting a million and one values (10^6 + 1)
        dim = (10 ** 6) + 1
        self.arr = [None for _ in range(dim)]

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        val = self.arr[key]
        return -1 if val is None else self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)