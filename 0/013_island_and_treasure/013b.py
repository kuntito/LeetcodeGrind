from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list):
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])

        queue = deque()
        for ri in range(self.rows):
            for ci in range(self.cols):
                if grid[ri][ci] == 0:
                    queue.append((ri, ci))


        seen = set()
        distance = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                seen.add(node)

                ri, ci = node
                grid[ri][ci] = distance

                self.add_neighbours(node, queue, seen)

            distance += 1
        

    def add_neighbours(self, node, queue, seen):
        start_ri, start_ci = node

        neighbours = [
            (start_ri + 1, start_ci),
            (start_ri - 1, start_ci),
            (start_ri, start_ci + 1),
            (start_ri, start_ci - 1),
        ]

        for nei in neighbours:
            if nei in seen: continue
            ri, ci = nei
            if min(ri, ci) >= 0 and\
                ri < self.rows and\
                ci < self.cols and\
                self.grid[ri][ci] != -1:
                queue.append(nei)
                seen.add(nei)

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