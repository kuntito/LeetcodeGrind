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
# tomorrow has come.

# what am i doing?
# i want to get from topLeft to bottomRight.
# that's one part of the problem.

# there's multiple ways to go from topLeft to bottomRight
# which one do i want?

# let's say we have all the ways.
# or consider one way

# -2 * -3 * 3 * 1 * -5
# what am i looking for here?

# at the first number, `-2`
# i need to have at least `3` so i don't hit zero

# if i had three and hit the second number, `-3`
# i'd need to have at least `4` to not hit zero.

# if i hit the next number, `3`
# now i'm at `7`

# if i hit the next number, now i'm 

# nah, i think my assumption is wrong

# let's go again.
# the first number is `-2`
# so i need at least `3` to not hit zero

# i move to the next number, `-3`
# since i started with `3`, and hit `-2`
# it means, i'm now at `1`

# i can't tackle `-3` with `1`
# so i need to add more to `1`, so i can tackle `-3`
# in this case, i'd do `1 + 3`

# which'd be four. let's stop right there and assume this is a simpler example.
# the path is -2 and -3

# what would i need to start with to make sure i don't hit zero.
# i need `3` so `-2` doesn't wipe me out, now i'm left with `1`
# i need `1 + 3` so `-3` doesn't wipe me out, now i'm left `1`
# and i've explored all the numbers.

# so what's the minimum i need to start with?
# i started with `0` and added `3`
# i had `1` and added `3`

# i think the health i added is the key.
# 3+3 = 6
# i need to start with at least, `6` to not get wiped out by
# -2, -3
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        pass