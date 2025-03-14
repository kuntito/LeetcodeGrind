# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        self.rows, self.cols = len(grid), len(grid[0])
        self.grid = grid
        self.fresh_orange_count = 0
        self.minutes = 0
        self.queue = deque()

        for ri in range(self.rows):
            for ci in range(self.cols):
                cell = grid[ri][ci]
                if cell == 2:
                    self.grid[ri][ci] = None
                    self.queue.append((ri, ci))
                elif cell == 1:
                    self.fresh_orange_count += 1

        self.explore_queue()

        return self.minutes if self.fresh_orange_count == 0 else -1


    def explore_queue(self):
        queue = self.queue

        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                item = queue.popleft()
                self.explore_neighbours(item)

            if len(queue):
                self.minutes += 1


    def explore_neighbours(self, item):
        item_ri, item_ci = item
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for nei in neighbours:
            ri, ci = nei[0] + item_ri, nei[1] + item_ci
            if self.is_valid_position(ri, ci) and\
                self.grid[ri][ci] == 1:
                    self.grid[ri][ci] = None
                    self.fresh_orange_count -= 1
                    self.queue.append((ri, ci))


    def is_valid_position(self, ri, ci):
        return ri >= 0 and ri < self.rows and ci >= 0 and ci < self.cols


# grid = [
#     [0, 2]
# ]

# grid = [
#     [2,1,1],
#     [1,1,0],
#     [0,1,1]
# ]

grid = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]

# grid = [
#     [2,1,1],
#     [1,1,1],
#     [0,1,2]
# ]

# grid = [
#     [1, 2]
# ]

sol = Solution()
res = sol.orangesRotting(grid)
print(res)