# https://leetcode.com/problems/swim-in-rising-water/description/

import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        minHeap = []
        heapq.heappush(
            minHeap,
            (0, (0, 0))
        )

        seen = set()
        while True:
            maxSoFar, pos = heapq.heappop(minHeap)
            maxSoFar = max(
                maxSoFar,
                grid[pos[0]][pos[1]]
            )

            if pos[0] == rows - 1 and pos[1] == cols - 1:
                return maxSoFar
            
            if pos in seen: continue
            seen.add(pos)

            for nei in self.get_nei(pos, seen, grid):
                heapq.heappush(minHeap, (maxSoFar, nei))
                

    def get_nei(self, pos, seen, grid):
        rows, cols = len(grid), len(grid[0])
        ri, ci = pos

        neighbours = (
            (ri-1, ci),
            (ri+1, ci),
            (ri, ci-1),
            (ri, ci+1),
        )

        return ((r, c) for r, c in neighbours if r >= 0 and r < rows and c >= 0 and c < cols and (r, c) not in seen)
    


arr = [
    [[3,2],[0,1]],
    [[0,2],[1,3]],
    [
        [0,1,2,3,4],
        [24,23,22,21,5],
        [12,13,14,15,16],
        [11,17,18,19,20],
        [10,9,8,7,6]
    ],
    # [
    #     [11,15,3, 2],
    #     [6, 4, 0,13],
    #     [5, 8, 9,10],
    #     [1,14,12, 7]
    # ],
]
foo = arr[-1]
sol = Solution()
res = sol.swimInWater(foo)
print(res)