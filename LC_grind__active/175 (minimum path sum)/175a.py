# https://leetcode.com/problems/minimum-path-sum/description/

# TODO same as path with minimum effort?
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        pass
        # two rows, `currRow` and `bottomRow`
        # both of size `cols`
        
        rows, cols = len(grid), len(grid[0])
        
        bottomRow = [None for _ in range(cols)]
        
        # iterate through grid from the last row upwards
        for ri in range(rows-1, -1, -1):
            curRow = [0 for _ in range(cols)]
            for ci in range(cols-1, -1, -1):
                # at each index,
                # set `currRow[idx] = gridRow[idx] + min(currRow[idx + 1], bottomRow[idx])`
                curRow[ci] = grid[ri][ci]
                
                rightVal = None if ci + 1 == cols else curRow[ci+1]
                bottomVal = bottomRow[ci]
                
                if isinstance(rightVal, int) and isinstance(bottomVal, int):
                    curRow[ci] += min(rightVal, bottomVal)
                elif isinstance(bottomVal, int):
                    curRow[ci] += bottomVal
                elif isinstance(rightVal, int):
                    curRow[ci] += rightVal
                    
            # update bottomRow = currRow
            bottomRow = curRow
                
        
        # return bottomRow[0]
        return bottomRow[0]        
                
    
arr = [
    [[1,3,1],[1,5,1],[4,2,1]],
    [[1,2,3],[4,5,6]],
]
foo = arr[-1]
sol = Solution()
res = sol.minPathSum(foo)
print(res)