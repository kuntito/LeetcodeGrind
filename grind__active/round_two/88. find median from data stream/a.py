# https://leetcode.com/problems/find-median-from-data-stream/description/

# what's the situation today?

# i want to implement a class that continuously stores integers
# and readily knows the median of all the integers it's stored.

# it has three methods..
# the constructor, `__init__`
# the method to store integers, `addNum`
# and the method that returns the median, `findMedian`

# the median is defined as the middle number
# when all the integers are sorted.

# i.e. in [1, 2, 3]
# `2` is the median

# note, that if the integers are even lengthed..
# i.e. [1, 2, 3, 4]

# the median becomes the average of the two middle numbers
# (2+3)/2

# that said, how are we storing these numbers.
# the brute force would be storing the numbers in an array
# then sorting to find the median when needed.

# i imagine this would result in a TLE, else it wouldn't be a hard question.

# it actually works, what a surprise.
# nonetheless, i know from last time that
# there's a more efficient solution with two heaps.
# i'd implement that in `b.py`

class MedianFinder:
    def __init__(self):
        self.store = []
        

    def addNum(self, num: int) -> None:
        self.store.append(num)

    def findMedian(self) -> float:
        self.store.sort()
        dim = len(self.store)

        isOdd = dim % 2 == 1
        midIdx = dim // 2

        if isOdd:
            return self.store[midIdx]

        numOne = self.store[midIdx-1]
        numTwo = self.store[midIdx]

        return (numOne + numTwo)/2