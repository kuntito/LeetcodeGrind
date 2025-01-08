# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/

# TODO https://neetcode.io/solutions/largest-local-values-in-a-matrix
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        pass
        
        # set the column range as `range(2, cols)`
        # `2` because that's the third index
        
        # set the row range as `range(2, rows)`
        
        # explore the 3x3 grid on each iteration and append it's largest value
        rows, cols = len(grid), len(grid[0])
        
        res = []
        for ri in range(2, rows):
            tmp = []
            for ci in range(2, cols):
                pass
                a = self.explore(ri, ci, grid)
                tmp.append(a)
            res.append(tmp)
            
        return res
    
    def explore(self, end_ri, end_ci, grid):
        start_ri = end_ri-2
        start_ci = end_ci-2
        
        highest = 0
        for ri in range(start_ri, end_ri + 1):
            for ci in range(start_ci, end_ci + 1):
                highest = max(
                    highest,
                    grid[ri][ci]
                )
                
        return highest
    
arr = [
    [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]],
    [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]],
]
foo = arr[-1]
sol = Solution()
res = sol.largestLocal(foo)
print(res)