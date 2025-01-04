
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        single_row = [0] * cols
        single_row[cols-1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:
                    single_row[c] = 0
                elif c + 1 < cols:
                    single_row[c] += single_row[c + 1]

        return single_row[0]


obstacles = [
    [0,0],
    [0,0]
]

# obstacles = [
#     [0,0],
#     [0,1]
# ]


sol = Solution()
res = sol.uniquePathsWithObstacles(obstacles)
print(res)