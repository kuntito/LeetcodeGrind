# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

# i'm given a 2d grid of numbers..

# starting at position (0, 0), i want to get to my destination, the `last row, last column`
# the goal is to find the path to destination with the lowest sum.

# however, it's not just a regular sum
# consider the array..

# [8, 2]
# [3, 5]

# we start at (0, 0), which is `8`
# we can go in the cardinal directions, up, down, left, right

# in our case, left and up, are out of bounds so we can go right
# or go down..

# i'm introducing a concept, called cost.. the cost of moving from one cell
# to the next..

# to move right wards, is to move from, `8 => 2`
# to move downwards, is to move from, `8 => 3`

# the cost is defined as the absolute difference between the former cell and the current cell.
# for `8 => 2`, the cost is |8-2| = `6`
# for `8 => 3`, the cost is |8-3| = `5`

# so it costs lower to try `8 => 3`
# but we don't know if it's the best path since we've not gotten to the destination..
# in essence, we'd have to explore every path to know the shortest...

# memoization can help, since at each cell, we'd be doing the same thing..
# and it's obviously solvable using recursion, since we'd the be doing the same thing at each cell..

# in essence, each cell, would return the mininmum cost to go from there to destination..
# then what, return the minimum of all explored paths.. i don't think this would suffice..

# since, .. since what..
# at each cell you want to know the minimum right..
# if you explore every cell.. and memoize, you optimally determine the minimum at every cell..
# you'd track the costs for each exploration path and add that to minimum of all four explorations
# at that current cell, return that..

# can we go back during exploration.. nah.. don't think that's a good idea..
# [8, 2]
# [3, 5]

# say we go `8 => 2` first..
# technically, you could go `2 => 8 => 3 => 4`, and reach destination
# but you were already at `8`

# if `8 => 3 => 4` is valuable, `8` would find out..
# in essence, we'd need to track visited cells for each exploration..

# and how would we calculate the absolute difference,
# we'd do so .. in each cell, each cell would have a reference to it's parent's value
# and calulate based on that..

# for the first cell, it's parent value would be it's own value
# that way abs diff = 0

# since, we track visited cells for each path we'd have to remove it after exploring the path
# consider
# [1, 2, 3]
# [4, 5, 6]

# if we explore 1 => 2 => 5 => 6, (1, 2, 5) would be visited
# but we need to clear the visited path on our way back up the recursive stack..
# after exploring all the viable paths of course..

# so for our case, we'd go back to `5`, explore 1 => 2 => 5 => 4...
# see, `4` is a dead end, remove it from visited..

# go back to `5`
# there's no where else to go at `5` since we came from `2`
# so we reomve `5` from visited, and go back to `2`
# visited now looks like (1, 2)...

# TODO i've completely misread the question
# back to the drawing board..
# literally speaking, with this question, you need a board..white paper, something..
# sketch out the idea..

# but first, understand what the question is asking..

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.heights = heights
        
        start_ri = 0
        start_ci = 0
        visited = set()
        parentValue = self.heights[start_ri][start_ci]
        curSum = 0
        return self.explore(start_ri , start_ci, visited, parentValue, curSum)
        
    def explore(self, ri, ci, visited, parentValue, curSum):
        mitem = (ri, ci)
        if mitem in visited or self.is_out_of_bounds(ri, ci):
            # highest number possible, so it ensures whatever path found is smaller than this
            # this is one gotcha that can well, getcha, if you're not versed with this
            # in my rationale, i didn't consider what to return if the path was visited
            # since the recursion demands i always compare the results of all explored paths..
            # in essence, we do explore all the paths, but the visited ones would have to be disregarded
            # and this `float("inf")` is one trick to help disregard them
            return float("inf")
        
        absDiff = abs(parentValue - self.heights[ri][ci])
        curSum += absDiff

        rows, cols = len(self.heights), len(self.heights[0])
        if ri == rows - 1 and ci == cols - 1:
            return curSum
        
        visited.add(mitem)        
                
        one = self.explore(ri - 1, ci, visited, self.heights[ri][ci], curSum)
        two = self.explore(ri + 1, ci, visited, self.heights[ri][ci], curSum)
        three = self.explore(ri, ci - 1, visited, self.heights[ri][ci], curSum)
        four = self.explore(ri, ci + 1, visited, self.heights[ri][ci], curSum)
        
        smallestPath = min(one, two, three, four)

        # curSum += smallestPath
        
        visited.remove(mitem)
        
        return smallestPath
        
    def is_out_of_bounds(self, ri, ci):
        rows, cols = len(self.heights), len(self.heights[0])
        
        return ri < 0 or ri == rows or ci < 0 or ci == cols
    
arr = [
    [
        [1,2,2],
        [3,8,2],
        [5,3,5]
    ],
    # [
    #     [8, 2],
    #     [3, 5],
    # ],
]
foo = arr[-1]
sol = Solution()
res = sol.minimumEffortPath(foo)
print(res)