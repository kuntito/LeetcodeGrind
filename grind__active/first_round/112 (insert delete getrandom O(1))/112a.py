# https://leetcode.com/problems/insert-delete-getrandom-o1/description/


# TODO https://neetcode.io/solutions/insert-delete-getrandom-o1
# 07:39
class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        
        idx = len(self.arr)
        self.seen[val] = idx
        self.arr.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if val in self.seen:
            pass
            
            # get the index of `val`
            idx = self.seen[val]
            
            # if the last element in the hashmap is different from val
            last_elem = self.arr[-1]
            if last_elem != val:
                # remove it and place it in val's index
                self.arr[idx] = last_elem
                # update the last element in the hashmap
                self[last_elem] = idx
                # pop it from the array
                self.arr.pop()
            
            # now, delete the val from the hashmap
            del self.seen[val]
            return True
        
        
        return False

    def getRandom(self) -> int:
        pass


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()