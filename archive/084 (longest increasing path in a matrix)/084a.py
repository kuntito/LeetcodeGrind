# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        self.matrix = matrix


        memo = {}
        maxLevel = 0
        for ri in range(rows):
            for ci in range(cols):
                pos = (ri, ci)
                maxLevel = max(
                    maxLevel,
                    self.explore(pos, memo)
                )
        
        return maxLevel


    def explore(self, pos, memo):
        if pos in memo:
            return memo[pos]
        
        neighbours = self.get_neighbours(pos)

        maxLevel = 0
        for nei in neighbours:
            maxLevel = max(
                maxLevel,
                self.explore(nei, memo)
            )

        memo[pos] = maxLevel + 1
        return memo[pos]



    def get_neighbours(self, pos):
        rows, cols = len(self.matrix), len(self.matrix[0])
        ri, ci = pos

        neighbours = [
            (ri-1, ci),
            (ri+1, ci),
            (ri, ci-1),
            (ri, ci+1),
        ]

        return ((r, c) for r, c in neighbours if r >= 0 and r < rows and c >= 0 and c < cols and self.matrix[r][c] > self.matrix[ri][ci])
    
    
arr = [
    [[9,9,4],[6,6,8],[2,1,1]],
    [[3,4,5],[3,2,6],[2,2,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.longestIncreasingPath(foo)
print(res)