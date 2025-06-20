# https://leetcode.com/problems/dungeon-game/

from typing import List

# i want to implement a function that returns an integer.
# the function is called `calculateMinimumHP` and it takes one argument
# a 2d integer array called `dungeon`.

# the 2d array represents a grid. a grid of integers.
# the story is a princess is kept captive at the bottom right corner
# and our knight, in the the top left corner wants to rescue her.

# each cell of the grid represents modifications to the knights health.
# a positive number increase the knights health, a negative number decreases it.

# zero, i assume is neutral.
# the knight can only travel rightwards or downwards.
# we want to find the minimum pathSum it takes the knight to go from topLeft to bottomRight

# actually, the question says we want to find the minimum health the knight needs to have to rescue the queen.

# i think i should solve based on this not the minimum pathSum.
# i was going to find the minimum pathSum, if negative?, negate it then add `1`
# but i'm now considering a scenario where the knight takes several big hits before getting a power up

# in this case, the knight would've hit `0` before getting the power up.
# and would make the path invalid.

# in other words, i need to find valid paths?? idk, tomorrow's problem
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        pass