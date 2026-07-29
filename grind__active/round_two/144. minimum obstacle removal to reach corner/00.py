import heapq
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        initObstacleCount = grid[0][0]
        
        minHeap = [
            (                
                initObstacleCount,
                (0, 0),
            )
        ]
        
        seen = set()
        finalDestination = self.getFinalDestination(grid)
        
        while minHeap:
            obstacleCount, nextCell = heapq.heappop(minHeap)
            
            if nextCell in seen:
                continue
            
            if nextCell == finalDestination:
                return obstacleCount
            
            seen.add(nextCell)
            self.addDestinations(obstacleCount, nextCell, minHeap, grid)
        
        
    def getFinalDestination(self, grid):
        rows, cols = len(grid), len(grid[0])
        return (rows - 1, cols - 1)
    
        
    def addDestinations(self, obstacleCount, cellPos, minHeap, grid):
        ri, ci = cellPos
        
        left = (ri, ci - 1)
        right = (ri, ci + 1)
        down = (ri - 1, ci)
        up = (ri + 1, ci)
        
        candidates = [left, right, down, up]
        
        destinations = []
        for c in candidates:
            ri, ci = c
            if not self.isValid(ri, ci, grid):
                continue
            
            destinations.append(
                (
                    obstacleCount + grid[ri][ci],
                    (ri, ci)
                )
            )
            
            
        for d in destinations:
            heapq.heappush(
                minHeap,
                d
            )
            
        
    def isValid(self, r, c, grid):
        rows, cols = len(grid), len(grid[0])
        is_valid = r >= 0 and r < rows and c >= 0 and c < cols
        return is_valid   
            