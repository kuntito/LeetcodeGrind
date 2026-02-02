# https://leetcode.com/problems/minimum-path-sum/

from typing import List

# right, remind me what we doing?
# you have a grid of integers, all greater than or equal to `0`

# you start at topLeft and want to reach bottomRight
# you want to find the lowest path sum..

# path sum is the sum of all the cells along the path you took
# from `topLeft` to `bottomLeft`

# how would this go?
# Dijkstra.

# how so? use a minHeap to store the smallest pathSum explored..
# elaborate..
# you start out `topLeft`

# can only go down or right..
# you pick the one with the lowest path sum..

# at each point, can either go down or right..
# so you pick the one with least path sum..

# path sum is not the least value..
# not saying, pick the lower of `down` and `right` values..
# but consider `down` and `right` in the context they're coming from..

# and how does the minHeap, help, you calculate the pathSums on the go
# append to the minHeap, this ensures, you always access the next smallest path sum

# what does the minHeap item look like?
# [pathSum, cellPos]

# you pop the top most element..
# grab it's neighbours, calculate their path sum..
# parentPathSum + neiValue
# append a new minHeap node.. and neiCellPos

# are we avoiding duplicates..
# in this case, i don't think it matters..

# we'd definitely reach the bottom, every position we take is the next smallest path sum
# and so.. we'd reach the destination, just by following the algo..

# but why did i need `seen` in network delay..
# you wanted to find out all the nodes you could reach starting from origin..
# ergo, you need to know the nodes you'd seen.. 

# here, you want to get to destination, with the least path sum,
# it doesn't matter if you see the same cell twice, it would simply mean..
# i don't even think you could see the same cell twice..

# well, you could, say at some point, it was the next smallest pathSum,
# on exploration, realized, it was too costly..
# minHeap exposes it again with pathSum that's bigger than the first time you saw it..
# but on exploration, it pays off in the long run..

# in this case, you do want to see the same cell again, if it's the smallest next pathSum

# error, left out a comma, when listing items in array
# error, didn't append tuple of [pathSum, neiPos] to minHeap, only appended `pathSum`
# error, the first entry is not `[0, topLeftPos]`, `[topLeftValue, topLeftPos]`

# error, something caused TLE.. find it..

# i think i see the point.

# 1 -> 2 -> 34
# 3 -> 2 -> 1

# my argument for not adding seen was for the example above. you could see the same cell 2, twice but the first path can lead to a greater sum down the line, so you go back to the next best path.

# what i didn't notice is from 2 if you could get to 1, from 3 -> 2 -> 1, you could also get to 1 from 1 -> 2 -> 34

# they all stem from 2, so the first time you see a cell is the best way to get to it, if it tanks, it means there's no better way to do it than what you've tried.

# TODO, it works now, but there's a more optimal solution
# see `https://www.youtube.com/watch?v=pGMsrvt0fpk`
import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        topLeftVal = grid[0][0]
        firstEntry = [topLeftVal, (0, 0)]
        minHeap = [firstEntry]
        
        rows, cols = len(grid), len(grid[0])
        destination = (rows-1, cols-1)
        
        seen = set()
        while True:
            curPathSum, curPos = heapq.heappop(minHeap)
            
            if curPos in seen:
                continue
            seen.add(curPos)
            
            if curPos == destination:
                return curPathSum
            
            neighbours = self.getNeighbours(curPos, grid)
            
            for neiPos in neighbours:
                nR, nC = neiPos
                neiValue = grid[nR][nC]
                
                heapq.heappush(
                    minHeap,
                    (
                        neiValue + curPathSum,
                        neiPos,
                    )
                )
        
    def getNeighbours(self, curPos, grid):
        
        r, c = curPos
        
        candidates = [
            (r + 1, c),
            (r, c + 1)
        ]
        
        rows, cols = len(grid), len(grid[0])
        return [(nR, nC) for nR, nC in candidates if nR >= 0 and nR < rows and nC >= 0 and nC < cols]
    
arr = [
    [[1,3,1],[1,5,1],[4,2,1]],
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
]
foo = arr[-1]
sol = Solution()
res = sol.minPathSum(foo)
print(res)