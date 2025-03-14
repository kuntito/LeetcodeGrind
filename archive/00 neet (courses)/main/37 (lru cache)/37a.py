# https://leetcode.com/problems/lru-cache/description/

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.collection = {}
        self.lru_dict = {}
        self.count = 0

    def get(self, key: int):
        res = self.get_internal(key)
        print(res)
        return res

    def get_internal(self, key: int) -> int:
        if key in self.collection:
            self.lru_dict[key] = self.get_count()
            return self.collection[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.collection) == self.capacity and key not in self.collection:
            self.remove_lru()

        self.collection[key] = value
        self.lru_dict[key] = self.get_count()


    def remove_lru(self):
        lru = None
        for key in self.lru_dict:
            if lru is None:
                lru = key

            if self.lru_dict[key] < self.lru_dict[lru]:
                lru = key
        
        del self.collection[lru]
        del self.lru_dict[lru]

    def get_count(self):
        self.count += 1
        return self.count

capacity = 2
sol = LRUCache(capacity)

# sol.put(1, 1)
# sol.put(2, 2)
# sol.get(1)
# sol.put(3, 3)
# sol.get(2)
# sol.put(4, 4)
# sol.get(1)
# sol.get(3)
# sol.get(4)

sol.get(2)
sol.put(2, 6)
sol.get(1)
sol.put(1, 5)
sol.put(1, 2)
sol.get(1)
sol.get(2)