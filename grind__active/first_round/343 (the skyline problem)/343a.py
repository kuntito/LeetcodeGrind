# https://leetcode.com/problems/the-skyline-problem/description/

from typing import List

# i want to implement a function that returns a 2d integer array.
# the function is called, `getSkyline`.

# it takes one argument a 2d integer array, `buildings`.
# each element of `buildings` is a 3-element array.

# where each element represents the properties of a building 
# i.e. [leftEdge, rightEdge, height]

# each building can be placed on a graph to form a vertical bar
# where the top left corner coordinates is (leftEdge, height)
# and top right corner is (rightEdge, height)

# when all buildings are placed, the possibility of overlap occurs.
# and the buildings would merge into one figure.

# my job is to return the skyline as a 2d array.
# the skyline of these buildings is the outline of their combined silhouette.
# it's a border drawn around the visible edges of all the buildings.

# we want to obtain the coordinates of their leftmost corners
# and filter for unique row indices.

# the problem lends itself to sorting
# if i sort all the buildings by rowIdx i.e. leftEdge
# i know which building comes first

# however, not all left edges are valid
# say i have a left edge at (2, 5)
# and another at (2, 6)

# the edge at (2, 6) would eclipse the edge at (2, 5)
# because it's taller

# in a way, i'm better off if i group similar left edges together
# and pick the ones with the highest height
# since these would stand out the most.

# my criteria so far is leftMost Tallest.
# some edges need to be disregarded, consider a left edge that sits in the middle of a taller building.

# how would i disregard this?
# the example given is [2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]

# the first two edges, [2, 9, 10] and [3, 7, 15] are valid since they are one of one, as far as row indices are concerned, so they are the left most and tallest two edges in the skyline

# the next edge, [5, 12, 12] should be disregarded.
# reason being, it's left edge (5, 12) falls in the middle of the previous building.

# it overlaps with the previous building
# and is shorter than it
# so we disregard it.

# you're right, but i think you've jumped the gun a bit
# let's explore the edges one after the other, leftEdge and rightEdge
# and see how we address each situation.


# the first building [2, 9, 10]
# the leftEdge is (2, 10)
# rightEdge is (9, 10)

# looking at the array, there's only one edge at x-coordinate
# therefore (2, 10) must be a valid edge i.e. leftmost and tallest

# the right edge (9, 10), looking at the image, it's invalid
# it overlaps with taller building...

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pass