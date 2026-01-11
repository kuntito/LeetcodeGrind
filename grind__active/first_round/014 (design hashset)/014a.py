# https://leetcode.com/problems/design-hashset/description/

class MyHashSet:
    def __init__(self):
        self.arr = [False] * ((10 **6) + 1)

    def add(self, key):
        self.arr[key] = True

    def contains(self, key):
        return self.arr[key]
    
    def remove(self, key):
        self.arr[key] = False