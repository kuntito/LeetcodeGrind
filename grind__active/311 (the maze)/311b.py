# https://leetcode.com/problems/the-maze/description/

from typing import List

# we have a maze, a 2d integer array of 0s and 1s
# the 0s represent an empty space, the 1s represent an obstacle

# we have a ball initially at `start`. start is a 2 element array representing coordinates (rowIndex, colIdx). the ball wants to get to detination: (rowIdx, colIdx)

# but the ball moves in a special way. it can move up, left, right and down
# but once it picks a direction, it keeps going in that direction till it hits an obstacle.

# it's worth pointing out, the edges of the grid are classed as obstacles. that is the ball can't go out of bounds, topRow, bottomRow, leftCol and rightCol are the constraints of the ball 

# once the ball, hits an obstacle, it changes direction.
# the question is given `maze`, `start` and `destination`
# can the ball ever stop at the destination
# passing through the destination doesn't count, the ball has to stop there
# that is, it hits an obstacle and can't move any more

# i've taken an alternative approach
# rather, than moving the ball in the hopes of hitting the destination
# we explore from the destination outwards and see if it can hit `start`

# based on the requirements, not all destinations are reachable. for a destination to be reachable. it needs to have a boundary around it.

# consider
# [0, 0, 0]
# [1, D, 1]
# [0, 0, 0]

# where `D` indicates the destination. in this maze, there's no way the ball stops at the destination, it would always pass through.

# however, i'm not sure what happens if `start` and `destination`
# refer to the same position TODO

# a given destination has four positions around it, top, bottom, left and right
# we're only interested in the ones that are obstacles i.e. 1s or out of bounds

# once we know these positions, we start our exploration one step in the opposite direction
# say the example above
# i think my reasoning is False again, perhaps, i'd have to move the ball instead.

# explore the maze as described and only turn when you hit an obstacle
# track visited positions so you don't revisit.
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        start = tuple(start)
        destination = tuple(destination)
        self.maze = maze
        
        seen = set()
        return self.explore(start, destination, seen)
    
    def explore(self, start, destination, seen):
        if start == destination:
            return True
        
        r, c = start
        # TODO
        # we want to know if we reach an obstacle
        # that's what determines a turn
        # write out your thoughts for implementing the function
        
        return False