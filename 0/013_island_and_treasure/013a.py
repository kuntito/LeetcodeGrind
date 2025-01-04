class Solution:
    def islandsAndTreasure(self, grid: list):
        rows, cols = len(grid), len(grid[0])
        for ri in range(rows):
            row = grid[ri]
            for ci in range(cols):
                item = row[ci]
                if item == 0:
                    seen = set()
                    self.explore_treasure((ri, ci), grid, seen)


    def explore_treasure(self, position, grid: list, seen: set, count=0):
        if position in seen:
            return
        
        if count > 0:
            ri, ci = position
            if count < grid[ri][ci]:
                grid[ri][ci] = count
            else :
                return

        seen.add(position)
        start_ri, start_ci = position
        neighbours = [
            (start_ri - 1, start_ci),
            (start_ri + 1, start_ci),
            (start_ri, start_ci - 1),
            (start_ri, start_ci + 1)
        ]

        for nei in neighbours:
            ri, ci = nei
            if ri == start_ri and ci == start_ci: continue
            if self.is_valid(nei, grid) and grid[ri][ci] > 0:
                self.explore_treasure(nei, grid, seen, count+1)
        seen.remove(position)


    def is_valid(self, pos, grid):
        ri, ci = pos
        rows, cols = len(grid), len(grid[0])
        return ri >= 0 and ri < rows and ci >= 0 and ci < cols


arr = [
    [
        [0,-1],
        [2147483647,2147483647]
    ],
    [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ],
    [
        [2147483647,2147483647,2147483647],
        [2147483647,-1,2147483647],
        [0,2147483647,2147483647]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.islandsAndTreasure(foo)

for row in foo:
    print(row)