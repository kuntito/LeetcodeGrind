# https://leetcode.com/problems/zigzag-iterator/description/

# what's the question? we want to implement a class that is initialized
# with two integer arrays

# the class should implement two functions, `next` and `hasNext`
# the `next` function returns the first element in each array
# it alternates between both arrays
# i.e. [1, 2, 3] and [4, 5, 6]

# if you call `next` thrice, the output should be 1->4->2...
# if you run out of values for one array
# just return the next value of the current filled array

# the `hasNext` function returns a boolean if there is a next value
# in one of the arrays

# TODO rewrite this to account for empty arrays
class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        self.arrOne = v1 if v1 else None
        self.arrTwo = v2 if v2 else None
        self.curr = self.arrOne

        self.idxOne = 0
        self.idxTwo = 0

    def next(self) -> int:
        # every time we call next, we should return the first element
        # of the current array

        # that said, we would need a variable that knows the current array with a value
        # i'd initialize it to `v1`

        # our lives might be easier, if we reverse the arrays to allow for pop operations, do this as an upgrade, the recruiter might question your reasoning for reversing the arrays, it makes the code cleaner but adds overhead runtime

        # let's declare a dummy function for updating the current array
        # what happens if you call next and there's no values? it doesn't say
        # i'd simply return `None`

        # i need two pointers, one on each array
        # every time i call next i want to obtain the element at the current array
        # and increment it's index

        value = None
        if self.curr == self.arrOne:
            value = self.arrOne[self.idxOne]
            self.idxOne += 1
        elif self.curr == self.arrTwo:
            value = self.arrTwo[self.idxTwo]
            self.idxTwo += 1

        self.updateCurr()

        return value

    def updateCurr(self):
        # if the current is array one and array two is valid
        # set current to array two

        # else, either current is array two, and array one is valid
        # set to array one

        # else set curr to None
        if self.curr == self.arrOne:
            if self.idxTwo < len(self.arrTwo):
                self.curr = self.arrTwo
            elif self.idxOne == len(self.arrOne):
                self.curr = None
        elif self.curr == self.arrTwo:
            if self.idxOne < len(self.arrOne):
                self.curr = self.arrOne
            elif self.idxTwo == len(self.arrTwo):
                self.curr = None

    def hasNext(self) -> bool:
        return self.curr is not None

arr = [
    [[1,2], [3,4,5,6]],
    [[1], []],
    [[], [1]],
]
foo, bar = arr[-1]
sol = ZigzagIterator(foo, bar)
print(sol.next())
print(sol.next())

