# https://leetcode.com/problems/nested-list-weight-sum-ii/description/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from typing import List


class NestedInteger:
    pass


# what is the question? we are to implement a function
# the function takes a list of nested integers

# what is a nested integer, a nested integer is an object that-
# let's pause on that
# the list we're given at the start contains nested integer
# each element of the list is either a nested integer or a list of nested integers

# the depth of an integer is the number of lists that it is inside of
# that is how far does it go. i.e.
#
# for instance, in [[[1]]] `1` is of depth 3
# the weight of an integer is `maxDepth - (integer depth) + 1`
# `maxDepth` is the deepest integer

# and our job is to implement a function that returns the total sum of each integer multiplied by it's weight

# how do we approach this, for one, we'd need to explore every integer
# and note it's depth, we can store every explored integer and depth in an array
# `intAndDepth`

# while populating the array, we track the deepest integer found
# using this, we can iterate through `intAndDepth` and calculate the weight of each integer.


# then return the total sum
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # to explore all the elements, we'd iterate through each item in the nestedList
        # each item is either an integer or a nestedList

        # we'd use a recursive approach that explores the lists
        # we'd need a two global variables, `intAndDepth` for tracking every integer and it's depth and `maxDepth` for subsequently calculating the weight

        self.maxDepth = 1
        self.intAndDepth = []

        self.explore(nestedList, 1)

        total = sum(
            ((self.maxDepth - depth) + 1) * val for val, depth in self.intAndDepth
        )
        return total

    def explore(self, nestedList, depth):
        self.maxDepth = max(depth, self.maxDepth)

        for item in nestedList:
            if item.isInteger():
                self.intAndDepth.append((item.getInteger(), depth))
            else:
                self.explore(item.getList(), depth + 1)
