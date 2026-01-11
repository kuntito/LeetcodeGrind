# https://leetcode.com/problems/block-placement-queries/description/

from typing import List

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        pass
        # code needs to be optimized.
        # what's the hold up?
        
        # is there any repeated work? 
        # not sure but i know something that can be sped up?
        
        # `canPlaceBlock`
        # rather than sliding through the range
        # we can start the slider at known obstacles
        
        # ideally we'd start from 0 till block End i.e. range(1, blockEnd)
        # if nothing, we'd go to (nextKnownObstacle + 1, blockEnd)
        
        # perhaps, we can use a two pointer on obstacles
        # uno, dos = 0, nextKnownObstacle
        
        # if the gap can accomodate a block: return True
        # else move uno to dos
        # and dos to the next known obstacle
        # and repeat...
    
arr = [
    [[1,2],[2,3,3],[2,3,1],[2,2,2]],
    [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]],
]
foo = arr[-1]
sol = Solution()
res = sol.getResults(foo)
print(res)