# https://leetcode.com/problems/walls-and-gates/description/

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        pass
        # just to be clear, `rooms` is a grid that can contain only three types of values
        
        # a wall, a gate or an empty room
        
        # the wall is represented with -1
        # the gate is represented with 0
        # and the empty room is represented with (2**31) - 1
        
        # our goal is to fill each empty room with an integer that represents it's distance to the nearest gate
        
        # off the dome, i'm thinking
        # for each empty room, we explore all directions
        
        # we recursively explore all possible directions and record the one with the smallest gate
        
        # on second thought, it might be easier to simply explore the gates
        # or at least, explore starting from the gate
        # we explore all directions, tracking the distance so far
        # whenever we reach an empty room or a room with a higher distance, we update it.
        
        # if the room's distance is lower than or equal to our current distance, we stop the exploration
        
        # this way all the rooms are guaranteed to have the smallest distance to a gate
        
        self.rooms = rooms
        visited = set()
        for ri, row in enumerate(rooms):
            for ci, val in enumerate(row):
                if val == 0:
                    self.explore(ri, ci, rooms, visited)
                    
    def explore(self, ri, ci, visited):
        pass
        pos = (ri, ci)
        if pos in visited:
            return
        
        visited.add(pos)
        # to explore we go in the cardinal directions, the example suggests that we can only move in cardinal directions, NEWS, can you confirm that?
        
        # for each direction, we recursively explore but what we'd do is track the visited cells, so we don't visit the same cell more than once

        # in each function what are we doing?
        # we want to determine what kind of cell, we're at
        # if we're at a wall, we return
        
        visited.remove(pos)