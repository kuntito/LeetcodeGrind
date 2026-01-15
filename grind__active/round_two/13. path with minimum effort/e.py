# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

# right, so what we doing?

# we want to traverse from top left to bottom right in the grid
# and we want to find the path with the minimum effort.

# the minimum effort is defined in a mind bendy way. i'd say it's easier to tackle the problem of finding a path first.

# starting at top left, do you know how to find your way to bottom right? or rather, can you find every way it'd take to get to bottom right?

# yeah, it looks like a backtracking approach with a set to track visited cells.

# so why not do that first, let's verify you can do that, then scale up.

# so how would that go, question says we can go in the cardinal directions, up, down, left, right... every cell we move to, the same situation occurs.

# hence, recursion.
# now, we don't want to traverse in a circular manner, so we'd need a set travelling with us, tracking every cell, we've seen..

# we keep going till we hit destination, `bottomLeft`, or till there's no where else to go, then we double back..
# and remove the visited cells..

# when you hit `bottomLeft`, print the path to verify it does what is says..

# okay, all said and done. i can check every path from top left to bottom right..

# what's next? i want to find the minimum path... no, the path with the minimum effort..

# how do we define effort? effort is the .. for any path.. how do you determine the effort of a path..

# the effort of a path is the highest difference between any two nodes on a path.

# say the path is `3 => 4 => 2`
# the highest intenode difference is `2`

# `3 => 4`, has a difference of `1`, absolute difference is what we're calculating..

# `4 => 2`, has an absolute difference of `2`.

# ergo, the highest difference between any two cells is `2`
# the effort of this cell is `2`.

# how do we calculate effort as we traverse.. that's what makes this tricky... what if i define a custom class..

# let me double back, currently, i use an ordered dict to track the paths. the dict keys are the position, cause they're unique, the values are the cell values..

# but i need one more.. the max effort so far. one idea is to combine it with value, somehow, but that would mean, every cell value would have the same max difference, plus, what would updating that look like..

# running through every cell value?
# that's not exactly a sound approach, the custom class would hold two values..

# the dict values and the max path..
# okay, so how would you print this..

# to be fair, the best way would be for the entire class to be the abstraction, no more ordered dict..

# i've added the custom class, now how am i tracking the difference between cells..

# well, the a difference occurs, everytime, you add a cell right?
# means, you can compare the cell with the previous one.. right?
# well, that's true for every cell except the first.

# how is the first cell different? there's no previous cell. what should it's absolute difference be..

# the first cells absolute difference should be zero in that case..
# so, for every add, you want to compare with the previous cell value..

# the update self.maxEffort on a need to basis..
# the array works cleanly for that

# heck, if there's no previous value, leave `self.maxEffort` as is..
# move on... that case, `self.maxEffort` should be initialized to `0` not `float("-inf")`

# the problem with this approach is i use the same instance to store all the max efforts.. not max efforts per path..

# in english, the same TrackPos instance tracks the max effort for all paths not each individual path..

# a more directionally correct approach would have the maxEffort be tracked along with each node, and be popped after node exploration, it would seem, i didn't need to change the ordered dict after all..

# you want to track the max effort at every node, and pop accordingly. one on hand, i could maintain the ordered dict and append the values as (val, maxEffortAtThisPoint), but i think my class implementation is cleaner since..

# i can separate them.. i'd just need another array for maxEffort
# and pop it whenever i'm popping the element..

# and so, technically, using the instance of `TrackPos`, i can track the lowest maxEffort seen..

# this hints another variable...
# `self.lowestMax`

# this would be updated when we reach right bottom..
# another file `e.py`

# you're spiralling, man.. this is not good..
# best approach, 15 mins per question..

# let's stick to this.. you know dijkstra solves this, why are you trying to prove a point to yourself..
# i mean, there's probably a a way you could get your solution to work, you're already on the ball
# or at least close to it but to what end..

# you know it wouldn't be efficient, least, not the way, you've written it..
# you could reinvent the wheel or deeply understan dijkstra..

# i'd say do dijkstra.. and while your argument against 15 min blocks pers question is that sometimes
# you know what to do but it takes a minute to draft your solution..

# since, you always write first.. no problem with that, how about 30 mins at most per question..
# least, this gives you enough time to draft.. whatever it is..

# right?

# okay, let's do that instead..
# but walk around now.. take a break.. come back stronger..
class PosTrack:
    def __init__(self, grid):
        self.grid = grid
        self.seen = set()
        self.arr = []
        
        # well, yes, even if you append as an array you
        # still don't know the max effort along each path..
        # thing is, at right bottom, you want to know the maxEffort for that specific path
        # and update lowest max effort
        self.efforts = []
        
        self.maxForPath = 0
        self.lowestMax = float("inf")
        
    def add(self, pos):
        self.seen.add(pos)
        
        
        r, c = pos
        val = self.grid[r][c]
        
        if self.efforts:
            effort = abs(self.arr[-1] - val)        
            self.efforts.append(effort)
            self.maxForPath = max(effort, self.maxForPath)
        else:
            self.efforts.append(0)
            self.maxForPath = 0

        self.arr.append(val)
        
        
    def remove(self, pos):
        self.seen.remove(pos)
        self.arr.pop()
        self.efforts.pop()
        if self.efforts:
            self.maxForPath = self.efforts[-1]
        
    def has(self, pos):
        return pos in self.seen
    
    def print(self):
        print(self.maxForPath, "=>", self.arr)
    

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.rows, self.cols = len(heights), len(heights[0])
        sr, sc = 0, 0

        track = PosTrack(heights)
        self.explore(sr, sc, track)
        return track.lowestMax
        
    def explore(self, r, c, track):
        pos = (r, c)
        if track.has(pos) or self.is_out_of_bounds(pos):
            return
        
        track.add(pos)
        
        if r == self.rows - 1 and c == self.cols - 1:
            # track.print()
            track.remove(pos)
            
            print(track.maxForPath)
            track.lowestMax = min(track.lowestMax, track.maxForPath)
            
            return
        
        self.explore(r - 1, c, track)
        self.explore(r + 1, c, track)
        self.explore(r, c - 1, track)
        self.explore(r, c + 1, track)
        
        track.remove(pos)
    
    def is_out_of_bounds(self, pos):
        r, c = pos
        return r < 0 or r == self.rows or c < 0 or c == self.cols
    
arr = [
    [        
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5],
    ],
    # [        
    #     [1, 5],
    # ],
]
foo = arr[-1]
sol = Solution()
res = sol.minimumEffortPath(foo)
# print(res)