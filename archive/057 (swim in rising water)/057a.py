# https://leetcode.com/problems/swim-in-rising-water/description/

import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minHeap = []

        prev_map = {}
        seen = set()

        origin = (0, 0)
        foo = (0, origin, None)
        heapq.heappush(minHeap, foo)

        holy_grail = None
        while True:
            node = heapq.heappop(minHeap)
            dist, node, prev =  node

            if node[0] == rows - 1 and node[1] == cols - 1:
                prev_map[node] = prev
                holy_grail = node
                break

            # print(pos)
            if node in seen:
                continue

            seen.add(node)
            prev_map[node] = prev


            for nei in self.get_nei(node, seen, grid):
                r, c = nei
                neiDist = grid[r][c]
                total = dist + neiDist

                heapq.heappush(minHeap, (neiDist, nei, node))


        highest = 0
        while holy_grail:
            ri, ci = holy_grail
            val = grid[ri][ci]
            # print(val)
            highest = max(
                highest,
                val
            )

            holy_grail = prev_map[holy_grail]

        return highest



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
    # [
    #     [0,1,2,3,4],
    #     [24,23,22,21,5],
    #     [12,13,14,15,16],
    #     [11,17,18,19,20],
    #     [10,9,8,7,6]
    # ],
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