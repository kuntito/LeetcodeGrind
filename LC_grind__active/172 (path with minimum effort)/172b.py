# https://leetcode.com/problems/path-with-minimum-effort/description/

# TODO what was i doing in `172a.py`
import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        pass

        # use dijkstra
        # the minHeap stores (absDiff, position, minDiffSoFar)
        
        origin = (0, 0)
        seen = set()
        minHeap = [(0, origin, 0)]
        
        rows, cols = len(heights), len(heights[0])
        dst = (rows-1, cols-1)
        while minHeap:
            pass
            _, currPos, minSoFar = heapq.heappop(minHeap)
            seen.add(currPos)
            if currPos == dst:
                return minSoFar
            
            for neiPos in self.get_neis(currPos, heights, seen):
                pass
                # for each neighbour, calculate the abs difference between itself
                # and the curr value
                # append to the min heap
                
                cR, cC = currPos
                currValue = heights[cR][cC]
                
                nR, nC = neiPos
                neiValue = heights[nR][nC]

                neiAbsDiff = abs(currValue - neiValue)
                
                heapq.heappush(minHeap, (
                        neiAbsDiff,
                        neiPos,
                        max(neiAbsDiff, minSoFar) # ensuring each node knows the most effort so far along it's path
                    )
                )
                
            


    def get_neis(self, pos, heights, seen):
        pass
        rows, cols = len(heights), len(heights[0])
        
        r, c = pos
        
        neis = (
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
        )
        
        return [(ri, ci) for ri, ci in neis if ri >= 0 and ri < rows and ci >= 0 and ci < cols and (ri, ci) not in seen]
    
        
arr = [
    [[1,2,2],[3,8,2],[5,3,5]],
    [[1,2,3],[3,8,4],[5,3,5]],
    [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.minimumEffortPath(foo)
print(res)