from typing import List


class Solution:
    def largestIsland(
        self,
        grid: List[List[int]]
    ) -> int:
        self.grid = grid
        seen = set()
        
        largest = 0
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val == 0: continue
                
                resLargest = self.exploreIsland(
                    ri,
                    ci,
                    seen,
                    False,
                )
                
                largest = max(
                    largest,
                    resLargest
                )
                    
        return largest
    
    def getRowsAndCols(self):
        return len(self.grid), len(self.grid[0])


    def exploreIsland(self, ri, ci, seen, zero_used):
        pos = (ri, ci)
        if pos in seen:
            return 0
        
        # TODO, the moment you hit a zero what do you do?

        # concern is there's zeros in four directions.
        # each zero, i pick as a one, leads to a different outcome.

        # i want to explore all from scratch.


        val = self.grid[ri][ci]
        if val == 0:
            if zero_used:
                return 0
            else:
                zero_used = True
                
        if val == 1:
            seen.add(pos)
            
        streak += self.exploreIsland(ri - 1, ci, seen, zero_used)
        streak += self.exploreIsland(ri + 1, ci, seen, zero_used)
        streak += self.exploreIsland(ri, ci - 1, seen, zero_used)
        streak += self.exploreIsland(ri, ci + 1, seen, zero_used)
        
        return streak + 1
        
        
        
        
arr = [
    [[1,0],[0,1]],
    [[1,1],[1,0]],
    [[1,1],[1,1]],1
    [
        [1,0,1],
        [0,0,0],
        [0,1,1]
    ],
    [
        [0,1,0],
        [1,0,1],
        [1,0,0]
    ]
]
foo = arr[-1]
sol = Solution()
res = sol.largestIsland(foo)
print(res)