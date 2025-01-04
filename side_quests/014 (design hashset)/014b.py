# https://leetcode.com/problems/design-hashset/description/


class MyHashSet:

    def __init__(self):
        # every element should fall into one of 100 boxes
        self.totalDim = 1_000_000
        self.boxCount = 100
        self.boxSize = self.totalDim // self.boxCount #10_000 elements in each box
        self.one_milli = False

        self.hashset = {}
        for i in range(self.boxCount):
            self.hashset[i] = [False for _ in range(self.boxSize)]

    def add(self, key: int) -> None:
        if key == 1_000_000:
            self.one_milli = True
        else:
            boxIdx, keyIdx = divmod(key, self.boxSize)

            box = self.hashset[boxIdx]
            box[keyIdx] = True

    def remove(self, key: int) -> None:
        if key == 1_000_000:
            self.one_milli = False
        else:
            boxIdx, keyIdx = divmod(key, self.boxSize)

            box = self.hashset[boxIdx]
            box[keyIdx] = False

    def contains(self, key: int) -> bool:
        if key == 1_000_000:
            return self.one_milli
        else:
            boxIdx, keyIdx = divmod(key, self.boxSize)

            box = self.hashset[boxIdx]
            return box[keyIdx]
        

sol = MyHashSet()
sol.add(1)
sol.add(2)
sol.contains(1)
sol.contains(3)
sol.add(2)
sol.contains(2)
sol.remove(2)
sol.contains(2)
