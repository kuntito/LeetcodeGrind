# https://leetcode.com/problems/the-maze/description/

from typing import List

# can i take a minute to understand the question?
# i'm should implement a function `hasPath` that takes three arguments
# a 2d integer array representing a maze
# and two 1d integer arrays, `start` and `destination`

# for context, `maze` represents a grid of `0s` and `1s`
# `0s` are empty spaces while `1s` represent a barrier.

# `start` and `destination` are arrays of length two.
# representing a row idx and col idx.

# we have a ball initially at `start` and wants to get to `destination`
# my job is to find out if the ball can reach `destination`
# or rather if the ball can stop at destination

# the ball can move in cardinal directions, up, down, left and right
# but once the ball moves in a direction, it keeps moving in that direction until it hits a barrier
# once this happens, the ball can move in any other cardinal direction

# the ball can only stop at the destination if the destination is surrounded by two perpendicular barriers and there exists a path from that destination to the ball.

# i think this might be simpler than having to move the ball towards the destination
# so we'd need to ensure the destination has two perpendicular barriers around it
# a barrier is a cell with `1` or a cell that's out of bounds


# once we have this we explore from destination outwards, tracking visited cells
# if we explore all cells and don't hit the ball, then it's not possible

# TODO i failed miserably
# my assumption for `isSurrounded` is False
class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        pass

        self.maze = maze

        # is destination surrounded by two perpendicular barriers
        isSurrounded = self.getSurrounded(destination)
        if not isSurrounded:
            return False

        seen = set()
        start = tuple(start)
        destination = tuple(destination)
        return self.explore(destination, start, seen)

    def explore(self, pos, end, seen):
        rows, cols = len(self.maze), len(self.maze[0])
        r, c = pos
        if r < 0 or r == rows or c < 0 or c == cols or pos in seen:
            return False
        if pos == end:
            return True

        seen.add(pos)

        if self.explore((r - 1, c), end, seen):
            return True

        if self.explore((r + 1, c), end, seen):
            return True
        if self.explore((r, c - 1), end, seen):
            return True
        return self.explore((r, c + 1), end, seen)

    def getSurrounded(self, destination):
        # what would this even look like?
        # get the four walls, check for upRight, rightDown, downLeft, leftUp
        # if any of those are both barriers then yes

        r, c = destination

        up = (r - 1, c)
        right = (r, c + 1)
        down = (r + 1, c)
        left = (r, c - 1)

        upRight = (up, right)
        rightDown = (right, down)
        downLeft = (down, left)
        leftUp = (left, up)

        foo = (upRight, rightDown, downLeft, leftUp)
        for dirOne, dirTwo in foo:
            if self.isBarrier(dirOne) and self.isBarrier(dirTwo):
                return True

        return False

    def isBarrier(self, pos):
        rows, cols = len(self.maze), len(self.maze[0])
        r, c = pos
        return r < 0 or r == rows or c < 0 or c == cols or self.maze[r][c]


arr = [
    [
        [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ],
        [0, 4],
        [3, 2],
    ],
    [
        [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ],
        [0, 4],
        [4, 4],
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.hasPath(foo, bar, baz)
print(res)
