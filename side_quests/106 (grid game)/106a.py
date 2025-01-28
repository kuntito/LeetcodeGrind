# https://leetcode.com/problems/grid-game/description/

import heapq

class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        pass
        # find the longest path from (0, 0) to (-1, -1) twice
        # and return the sum of the second iteration
        
        res = self.get_longest_path(grid)
        return res
        
    def get_longest_path(self, grid):
        pass
        # it's a reverse of dijkstra's algorithm
        
        rows, cols = len(grid), len(grid[0])
        dst = (rows-1, cols-1)
        
        origin_val = grid[0][0]
        arr = [
            (                
                -origin_val,
                (0, 0)
            )
        ]
        
        visited = set()
        while arr:
            currVal, currPos = heapq.heappop(arr)
            if currPos == dst:
                return -currVal
            
            # Skip if the node has already been visited
            if currPos in visited:
                continue
            
            # Mark the current node as visited
            visited.add(currPos)
            
            neis = self.get_neighbours(currPos, grid)
            for nei in neis:
                r, c = nei
                neiVal = -grid[r][c]
                neiVal += currVal
                heapq.heappush(
                    arr,
                    (neiVal, (nei))
                )
            
            
    def get_neighbours(self, pos, grid):
        rows, cols = len(grid), len(grid[0])
        ri, ci = pos
        
        neis = [
            (ri, ci + 1),
            (ri + 1, ci),
        ]
        
        return ((r, c) for r, c in neis if r >= 0 and r < rows and c >= 0 and c < cols)
        
arr = [
    [[2,5,4],[1,5,1]],
    [[3,3,1],[8,5,2]],
    [[1,3,1,15],[1,3,3,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.gridGame(foo)
print(res)