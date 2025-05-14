# https://leetcode.com/problems/nested-list-weight-sum/description/

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
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
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# what is the question?
# we're given a list

# the list is what is known as a nested list
# what this means is that the list can contain integers or other nested lists

# for example:
# [1, [1, 2]] is a nested list
# [1, [2, [3, 4]]] is also a nested list but it contains anoter nested list `[2, [3, 4]]`



# and we want to implement a function that returns the total depthSum
# what this means is for every integer in the nestedList, we can determine it's depthSum
# by multiplying the value of the integer itself and it's depth within the list

# the total depthSum is the sum of all the individual depth sums

# i understand the question, but how do i approach it
# i'm considering a recursive approach, where i parse every element in the list
# when i encounter another list, i start a recursive call and return the total depthSum
# at that level, the base case would be when all the elements of a list are integers

# in addition, i want to add the current depth as an argument to the recursive call

# TODO, i have completely misunderstood the question
# i need to understand what a nested integer is, what are the arguments being passed
class Solution:
    def depthSum(self, nestedList) -> int:
        return self.exploreDepthSum(nestedList, 1)
    
    def exploreDepthSum(self, lst, depth):
        # if lst.isInteger():
        #     return depth * lst.getInteger()

        total = 0
        
        for elem in lst:
            if elem.isInteger():
                total += (elem.getInteger() * depth)
            else:
                total += self.exploreDepthSum(elem.getList(), depth + 1)
                
        return total
    
arr = [
    [[1,1],2,[1,1]],
    [1,[4,[6]]],
]
foo = arr[-1]
sol = Solution()
res = sol.depthSum(foo)
print(res)
    
