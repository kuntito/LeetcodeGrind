# https://leetcode.com/problems/furthest-building-you-can-reach/description/

# TODO TLE, what's wrong?
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        pass
        # say you were to only use bricks
        # how far could you go
        # the idea is to find a way to optimize the brick usage
        # can't use bricks for everything
        
        # bruteforce is explore all possibilities
        # and determine the furthest one
        
        self.heights = heights
        self.furthest = 0
        
        # start from `idx == 1`, since we're comparing each value to it's previous value
        self.explore(1, bricks, ladders)
        return self.furthest
        
    def explore(self, currIdx, bricksLeft, laddersLeft):
        dim = len(self.heights)
        if currIdx == dim:
            return
        
        prev, curr = self.heights[currIdx-1], self.heights[currIdx]
        
        # if the value at `currIdx` is less than or equal to previous
        # simply update `furthest`
        if prev >= curr:
            self.furthest = max(self.furthest, currIdx)
            self.explore(currIdx + 1, bricksLeft, laddersLeft)
        else:        
            # if the value at `currIdx` is greater than the previous
            # explore bricks and explore ladders
            bricksNeeded = curr - prev
            if bricksLeft - bricksNeeded >= 0:
                self.furthest = max(self.furthest, currIdx)
                self.explore(currIdx + 1, bricksLeft - bricksNeeded, laddersLeft)
            if laddersLeft - 1 >= 0:
                self.furthest = max(self.furthest, currIdx)
                self.explore(currIdx + 1, bricksLeft, laddersLeft - 1)

        
arr = [
    [[4,2,7,6,9,14,12], 5, 1],
    [[4,12,2,7,3,18,20,3,19], 10, 2],
    [[14,3,19,3], 17, 0],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.furthestBuilding(foo, bar, baz)
print(res)