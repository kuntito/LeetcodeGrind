# https://leetcode.com/problems/walls-and-gates/description/


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # grid filled with walls and gates
        # placing the plates in place
        # lord knows, it is no debate

        # we're given a grid, each cell of the grid can contain one of three values

        # -1, 0, or INF
        # the grid is meant to represent a maze where the values have meanings:
        # -1 means an obstacle
        # 0 means a gate
        # and INF, represents a room, INF is a value that defaults to the largest possible integer

        # the aim is to modify INF, to replace it with an integer that represents the distance to it's nearest gate

        # in essence, for every INF, we want to find the nearest gate
        # how do we know the nearest gate, we don't. we'd have to explore every gate...

        # every gate for every room seems a bit tedious
        # rather, why don't we explore every gate outwards
        # we explore all cardinal directions till we hit an obstacle

        # and while exploring, we track the current steps it takes to reach each grid position, if we encounter a room

        # we want to update the room's value if the current steps is less than what's there
        # if the current steps is greater than or equal to the room's value, we avoid the room

        # do we stop the exploration or go to another room?
        # the reasoning here is whichever gate made that room have less steps would have done so for the nearby rooms and so it becomes rather pointless to keep exploring after hitting a room with a higher or equal step

        # how do we track the current step
        # recursion, for every recursive call we increase the count by `1`

        # we initialize it with one though
        # so run through the grid, for every gate
        # start a recursive chain, follow the instructions
        # and c'est finni

        self.rooms = rooms
        for ri, row in enumerate(rooms):
            for ci, val in enumerate(row):
                if val == 0:
                    self.exploreGate(ri - 1, ci, 1)
                    self.exploreGate(ri + 1, ci, 1)
                    self.exploreGate(ri, ci - 1, 1)
                    self.exploreGate(ri, ci + 1, 1)
                    

    def exploreGate(self, ri, ci, curSteps):
        rows, cols = len(self.rooms), len(self.rooms[0])

        if ri < 0 or ri == rows or ci < 0 or ci == cols:
            return
        roomValue = self.rooms[ri][ci]
        if roomValue == -1 or (curSteps >= roomValue):
            return

        self.rooms[ri][ci] = curSteps
        # how do we make sure we don't visit the same room more than once in an exploration

        # i believe the check against current steps handles that
        # if we check more than once, it means the current steps on the second check would be higher than the first, hence return

        self.exploreGate(ri - 1, ci, curSteps + 1)
        self.exploreGate(ri + 1, ci, curSteps + 1)
        self.exploreGate(ri, ci - 1, curSteps + 1)
        self.exploreGate(ri, ci + 1, curSteps + 1)


arr = [
    [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ],
]
foo = arr[-1]
sol = Solution()
sol.wallsAndGates(foo)

for row in foo:
    print(row)