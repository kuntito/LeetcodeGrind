import heapq

from typing import List


class Solution:
    def minimumTime(
        self,
        grid: List[List[int]]
    ) -> int:
        pass
        # what's the min heap item
        # [availTime, cellPos]
        initItem = (0, (0, 0))
        minHeap = [initItem]
        
        # then i need a value for current time
        curTime = 0
        
        rows, cols = len(grid), len(grid[0])
        finalDest = (rows-1, cols-1)
        
        seen = set()
        while minHeap:
            availTime, cellPos = heapq.heappop(minHeap)
            
            if cellPos is finalDest:
                break
            
            if cellPos in seen:
                continue
            seen.add(cellPos)
            
            # TODO, start here.
            # two concerns, one, the heap item also needs time.
            # currently, i treat time across all possible paths as one variable.
            # each path should have it's path specific time.
            # two, i shouldn't add visited cells to next destination.
            # the algo could probably work without it, but it's cleaner this way
            print(cellPos)
            
            # now, we want to get the next position
            # you check, can i move there?..
            # is my current time >= availTime
            if curTime >= availTime:
                # what happens now?
                # i'd increase current time, 
                # since i'd move to this cell
                curTime += 1
            else:
                # this means i have to wait till i can move to the cell
                # the part the question leaves out,
                # when waiting, is the one second required to move, added on to the time i'm waiting for?
                # i'd assume it isn't unless proven otherwise.
                curTime = availTime
                
            self.addNextPositions(cellPos, minHeap, grid)
            
        return curTime
    
    def addNextPositions(self, cellPos, minHeap, grid):
        rows, cols = len(grid), len(grid[0])
        is_valid = lambda pos: pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols
        
        
        ri, ci = cellPos
        candidates = [
            (ri - 1, ci),
            (ri + 1, ci),
            (ri, ci - 1),
            (ri, ci + 1),
        ]
        
        
        for cand in candidates:
            if is_valid(cand):
                r, c = cand
                heapq.heappush(
                    minHeap,
                    (
                        grid[r][c],
                        cand
                    )
                )                
                
    
arr = [
    [
        [0,1,3,2],
        [5,1,2,5],
        [4,3,8,6]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.minimumTime(foo)
print(res)