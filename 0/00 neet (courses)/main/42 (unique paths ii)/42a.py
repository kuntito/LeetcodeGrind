# https://leetcode.com/problems/unique-paths-ii/description/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] == 1: return 0

        path_grid = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        path_grid[rows-1][cols-1] = 1

        for ri in range(rows-1, -1, -1):
            for ci in range(cols-1, -1, -1):
                if ri == rows-1 and ci == cols-1: continue
                if obstacleGrid[ri][ci] == 0:
                    path_grid[ri][ci] = path_grid[ri+1][ci] + path_grid[ri][ci+1]

        return path_grid[0][0]


obstacles = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]


# obstacles = [
#     [0,0],
#     [0,1]
# ]

# obstacles = [
#     [0,0],
#     [1,1],
#     [0,0]
# ]

sol = Solution()
res = sol.uniquePathsWithObstacles(obstacles)
print(res)