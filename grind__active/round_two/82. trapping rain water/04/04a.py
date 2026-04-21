from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftBoundary, rightBoundary = None, None
        leftIdx, rightIdx = 0, len(height) - 1


        while leftIdx <= rightIdx:
            leftVal = height[leftIdx]
            rightVal = height[rightIdx]

            # i'm at two extremes
            # i want to calculate the amount i can store at one of the extremes
            # but which?

            # they say the smaller one, but why?
            # why not the bigger one?

            # what would it look like? if i calculated the bigger one?
            # i need to know it's tallest left boundary
            # and it's tallest right boundary

            # at the starting point, the bigger one is missing one boundary
            # so i have to make do with whichever boundary's available.

            # i'd calculate `availableBoundary - currentPillar`
            # and that'd be the space i can afford at that point

            # so i'd proceed that index.
            # now, we're back at the same question.

            # which to calculate, the bigger one or the smaller one?

            # let's make this concrete with an example
            # [2, 1, 3]

            # `3` is the bigger one, it has no right boundary. 

